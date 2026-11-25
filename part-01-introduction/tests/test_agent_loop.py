import sys
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from agent_loop import load_scenario, run_agent_loop, run_chatbot


class AgentLoopTests(unittest.TestCase):
    def setUp(self) -> None:
        self.part_directory = Path(__file__).resolve().parents[1]

    def test_chatbot_answers_once_without_a_tool(self) -> None:
        scenario = load_scenario(self.part_directory / "scenarios" / "C01.yaml")
        trace = run_chatbot(scenario)

        self.assertEqual(trace["trace_id"], "C01-run-1")
        self.assertEqual(
            trace["final_state"], {"conversation_status": "answered", "tool_calls": 0}
        )
        self.assertEqual(trace["grade"], {"state": "pass", "claim": "pass"})
        self.assertEqual(len(trace["spans"]), 2)

    def test_agent_loop_observes_a_tool_result_before_it_answers(self) -> None:
        scenario = load_scenario(self.part_directory / "scenarios" / "A01.yaml")
        trace = run_agent_loop(scenario)

        self.assertEqual(trace["trace_id"], "A01-run-1")
        self.assertEqual(
            trace["final_state"],
            {"agent_status": "completed", "tool_calls": 1, "return_window_days": 30},
        )
        self.assertEqual(trace["grade"], {"state": "pass", "claim": "pass"})
        self.assertEqual(trace["spans"][2]["tool_call"], "lookup_policy")
        self.assertEqual(trace["spans"][3]["tool_result"], {"return_window_days": 30})
        self.assertEqual(trace["spans"][5]["assistant"], "The return window is 30 days.")

    def test_published_traces_match_the_runnable_examples(self) -> None:
        examples = {
            "C01": run_chatbot(
                load_scenario(self.part_directory / "scenarios" / "C01.yaml")
            ),
            "A01": run_agent_loop(
                load_scenario(self.part_directory / "scenarios" / "A01.yaml")
            ),
        }

        for scenario_id, trace in examples.items():
            trace_path = self.part_directory / "traces" / f"{scenario_id}-run-1.yaml"
            with trace_path.open(encoding="utf-8") as trace_file:
                self.assertEqual(yaml.safe_load(trace_file), trace)


if __name__ == "__main__":
    unittest.main()
