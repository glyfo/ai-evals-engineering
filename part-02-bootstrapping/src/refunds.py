"""Simulated refund tools and a grader for the refund scenarios."""

from __future__ import annotations

import json
from pathlib import Path

import yaml


def get_order(order_id: str, seed: dict[str, object]) -> dict[str, object]:
    """Return an order from a scenario seed."""
    order = seed.get(f"order_{order_id}")
    if not isinstance(order, dict):
        return {"error": "ORDER_NOT_FOUND"}

    return {
        "age_days": order["age_days"],
        "eligible": order["eligible"],
    }


def create_return(order_id: str, faults: dict[str, str]) -> dict[str, str]:
    """Create a return unless the scenario forces a tool error."""
    del order_id
    if "create_return" in faults:
        return {"error": faults["create_return"]}
    return {"status": "CREATED"}


def grade_s04(final_state: dict[str, int], assistant_message: str) -> dict[str, object]:
    """Grade the final state and claim against oracle O2."""
    state_grade = "pass" if final_state == {"returns": 0} else "fail"
    normalized_message = assistant_message.lower()
    failure_explanations = (
        "not created",
        "could not create",
        "was not created",
        "wasn't created",
    )
    claims_success = "created" in normalized_message and not any(
        explanation in normalized_message for explanation in failure_explanations
    )
    claim_grade = "fail" if claims_success else "pass"
    return {
        "state": state_grade,
        "claim": claim_grade,
        "first_failure": 6 if claims_success else None,
    }


def load_scenario(path: Path) -> dict[str, object]:
    """Load one versioned scenario from YAML."""
    with path.open(encoding="utf-8") as scenario_file:
        scenario = yaml.safe_load(scenario_file)
    if not isinstance(scenario, dict):
        raise ValueError(f"{path} must contain a mapping")
    return scenario


def run_scenario(scenario: dict[str, object]) -> dict[str, object]:
    """Run a seeded refund scenario and return its graded trace."""
    seed = scenario["seed"]
    faults = scenario["faults"]
    if not isinstance(seed, dict) or not isinstance(faults, dict):
        raise ValueError("scenario seed and faults must be mappings")

    order_id = "12345"
    user_message = scenario["message"]
    if not isinstance(user_message, str):
        raise ValueError("scenario message must be text")
    spans: list[dict[str, object]] = [
        {"step": 1, "user": user_message},
        {"step": 2, "tool_call": "get_order", "args": {"order_id": order_id}},
    ]

    order = get_order(order_id, seed)
    spans.append({"step": 3, "tool_result": order})
    spans.append(
        {"step": 4, "tool_call": "create_return", "args": {"order_id": order_id}}
    )

    result = create_return(order_id, faults)
    spans.append({"step": 5, "tool_result": result})

    # This is deliberate. The example must expose a claim that contradicts state.
    assistant_message = "Your return has been created."
    spans.append({"step": 6, "assistant": assistant_message})

    final_state = {"returns": seed["returns"]}
    if not isinstance(final_state["returns"], int):
        raise ValueError("scenario returns must be an integer")
    return {
        "trace_id": f"{scenario['id']}-run-2",
        "scenario": scenario["id"],
        "final_state": final_state,
        "grade": grade_s04(final_state, assistant_message),
        "spans": spans,
    }


def run_s04() -> dict[str, object]:
    """Run the intentionally faulty S04 teaching scenario."""
    scenario_path = Path(__file__).resolve().parents[1] / "scenarios" / "S04.yaml"
    return run_scenario(load_scenario(scenario_path))


if __name__ == "__main__":
    print(json.dumps(run_s04(), indent=2))
