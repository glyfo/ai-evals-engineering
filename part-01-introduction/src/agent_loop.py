"""Deterministic examples of a chatbot turn and a minimal agent loop."""

from __future__ import annotations

import json
from pathlib import Path

import yaml


def load_scenario(path: Path) -> dict[str, object]:
    """Load a scenario mapping from YAML."""
    with path.open(encoding="utf-8") as scenario_file:
        scenario = yaml.safe_load(scenario_file)
    if not isinstance(scenario, dict):
        raise ValueError(f"{path} must contain a mapping")
    return scenario


def chatbot_reply(message: str) -> str:
    """Return a fixed response without calling a tool."""
    if message.lower() == "hello":
        return "Hello. I answer one message at a time."
    return "I answer one message at a time."


def lookup_policy(seed: dict[str, object]) -> dict[str, int]:
    """Return the synthetic return-window policy."""
    return_window_days = seed.get("return_window_days")
    if not isinstance(return_window_days, int):
        raise ValueError("scenario return_window_days must be an integer")
    return {"return_window_days": return_window_days}


def grade_chatbot(
    final_state: dict[str, object], assistant_message: str
) -> dict[str, object]:
    """Grade the final state and the chatbot claim separately."""
    state_grade = "pass" if final_state == {
        "conversation_status": "answered",
        "tool_calls": 0,
    } else "fail"
    claim_grade = (
        "pass"
        if assistant_message == "Hello. I answer one message at a time."
        else "fail"
    )
    return {"state": state_grade, "claim": claim_grade}


def grade_agent_loop(
    final_state: dict[str, object], assistant_message: str
) -> dict[str, object]:
    """Grade the final state and the agent claim separately."""
    state_grade = "pass" if final_state == {
        "agent_status": "completed",
        "tool_calls": 1,
        "return_window_days": 30,
    } else "fail"
    claim_grade = (
        "pass" if assistant_message == "The return window is 30 days." else "fail"
    )
    return {"state": state_grade, "claim": claim_grade}


def run_chatbot(scenario: dict[str, object]) -> dict[str, object]:
    """Run a chatbot that answers once and does not use a tool."""
    message = scenario.get("message")
    if not isinstance(message, str):
        raise ValueError("scenario message must be text")
    assistant_message = chatbot_reply(message)
    final_state = {"conversation_status": "answered", "tool_calls": 0}
    return {
        "trace_id": f"{scenario['id']}-run-1",
        "scenario": scenario["id"],
        "spans": [
            {"step": 1, "cycle": 1, "user": message},
            {"step": 2, "cycle": 1, "assistant": assistant_message},
        ],
        "final_state": final_state,
        "grade": grade_chatbot(final_state, assistant_message),
    }


def run_agent_loop(scenario: dict[str, object]) -> dict[str, object]:
    """Run an explicit observe-decide-act loop with one policy lookup."""
    message = scenario.get("message")
    seed = scenario.get("seed")
    if not isinstance(message, str) or not isinstance(seed, dict):
        raise ValueError("agent-loop scenario needs text message and mapping seed")

    spans: list[dict[str, object]] = [{"step": 1, "cycle": 1, "user": message}]
    state: dict[str, object] = {
        "agent_status": "running",
        "observation": message,
        "tool_calls": 0,
        "tool_result": None,
    }
    cycle = 0

    while state["agent_status"] != "completed":
        cycle += 1
        if state["tool_result"] is None:
            spans.append({"step": 2, "cycle": cycle, "decision": "lookup_policy"})
            spans.append(
                {
                    "step": 3,
                    "cycle": cycle,
                    "tool_call": "lookup_policy",
                    "args": {"topic": "return_window"},
                }
            )
            tool_result = lookup_policy(seed)
            state["tool_result"] = tool_result
            state["observation"] = tool_result
            state["tool_calls"] = 1
            spans.append({"step": 4, "cycle": cycle, "tool_result": tool_result})
            continue

        tool_result = state["tool_result"]
        if not isinstance(tool_result, dict):
            raise ValueError("agent loop requires a policy result")
        return_window_days = tool_result.get("return_window_days")
        if not isinstance(return_window_days, int):
            raise ValueError("policy result must contain return_window_days")
        spans.append({"step": 5, "cycle": cycle, "decision": "respond"})
        assistant_message = f"The return window is {return_window_days} days."
        spans.append({"step": 6, "cycle": cycle, "assistant": assistant_message})
        state["agent_status"] = "completed"

    final_state = {
        "agent_status": state["agent_status"],
        "tool_calls": state["tool_calls"],
        "return_window_days": state["tool_result"]["return_window_days"],
    }
    return {
        "trace_id": f"{scenario['id']}-run-1",
        "scenario": scenario["id"],
        "spans": spans,
        "final_state": final_state,
        "grade": grade_agent_loop(final_state, assistant_message),
    }


def run_examples() -> dict[str, dict[str, object]]:
    """Run the chatbot and agent-loop teaching scenarios."""
    scenario_directory = Path(__file__).resolve().parents[1] / "scenarios"
    return {
        "chatbot": run_chatbot(load_scenario(scenario_directory / "C01.yaml")),
        "agent_loop": run_agent_loop(load_scenario(scenario_directory / "A01.yaml")),
    }


if __name__ == "__main__":
    print(json.dumps(run_examples(), indent=2))
