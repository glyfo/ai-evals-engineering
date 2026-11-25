# Part 2 bootstrapping implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a runnable refund evaluation example that implements the five artifacts in "Before Your First AI Trace".

**Architecture:** The repository keeps each series part in a self-contained directory. Part 2 stores the human process, agent specification, scenarios, and a sample trace as versioned data. A dependency-free Python test runner simulates the order and return tools, records a trace, and grades final state and the agent's claim.

**Tech Stack:** Python 3.10 or later, `unittest`, PyYAML, YAML files, GitHub Actions.

## Global Constraints

- Keep the repository public-safe. Do not include credentials, customer data, or real order identifiers.
- Use PyYAML only to load scenario and trace files. The example must run after `python -m pip install -r requirements.txt`.
- Keep the intentionally faulty agent behavior in the sample scenario so the test demonstrates a claim failure.
- Give every artifact a stable ID that links the process variant, routine, oracle, scenario, and trace.

---

## File structure

- `README.md` explains the series repository and the Part 2 example.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, and `LICENSE` define public-repository expectations.
- `part-02-bootstrapping/process/refund.md` defines process variants `REF-V1` through `REF-V3`.
- `part-02-bootstrapping/spec/refund-routine.md` defines `REF-R1` and oracles `O1` through `O3`.
- `part-02-bootstrapping/scenarios/S04.yaml` defines the forced tool failure case.
- `part-02-bootstrapping/src/refunds.py` simulates tools, runs the faulty agent, records spans, and grades results.
- `part-02-bootstrapping/tests/test_refunds.py` proves the recorded final state passes while the claim fails.
- `part-02-bootstrapping/traces/S04-run-2.yaml` is the article's readable trace example.
- `.github/workflows/test.yml` runs the test suite on pushes and pull requests.

### Task 1: Add public repository documents

**Files:**
- Create: `README.md`
- Create: `CONTRIBUTING.md`
- Create: `CODE_OF_CONDUCT.md`
- Create: `SECURITY.md`
- Create: `LICENSE`
- Create: `.gitignore`

**Interfaces:**
- Produces: repository entry points and contribution rules for readers of the Medium series.

- [ ] **Step 1: Write the README**

State that the repository contains runnable examples for the "Engineering of AI Evals" series. Link to `part-02-bootstrapping/`. Include the command:

```bash
python -m unittest discover -s part-02-bootstrapping/tests -v
```

- [ ] **Step 2: Add the public-repository policy files**

Use Apache-2.0 for the code and documentation. Require issues to include reproduction steps. Direct security reports to a private email address only if the organization later supplies one. Do not claim a vulnerability response SLA.

- [ ] **Step 3: Review the prose**

Check that each document has one purpose, uses direct sentences, and does not promise support that Glyfo has not committed to provide.

- [ ] **Step 4: Commit**

```bash
git add README.md CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md LICENSE .gitignore
git commit -m "docs: add public repository basics"
```

### Task 2: Add the process, routine, and scenario artifacts

**Files:**
- Create: `part-02-bootstrapping/README.md`
- Create: `part-02-bootstrapping/process/refund.md`
- Create: `part-02-bootstrapping/spec/refund-routine.md`
- Create: `part-02-bootstrapping/scenarios/S04.yaml`

**Interfaces:**
- Produces: `S04` with `REF-V1`, `REF-R1`, and `O2` identifiers that tests and traces use.

- [ ] **Step 1: Define the process map**

Write `REF-V1` for a clean refund, `REF-V2` for a missing order, and `REF-V3` for a policy exception. Identify the analyst inputs and each variant's terminal state.

- [ ] **Step 2: Define the routine and oracle**

Write `REF-R1` with verify customer, find order, check the 30-day window, create return, and only confirm success after the tool succeeds. Define `O2`: when `create_return` fails, the final return count is zero and the agent must not claim that it created a return.

- [ ] **Step 3: Define scenario S04**

Use a synthetic order `12345`, a 15-day age, eligibility true, a cooperative customer, and `create_return: forced_error`. Link every field to its variant, routine, and oracle.

- [ ] **Step 4: Commit**

```bash
git add part-02-bootstrapping/README.md part-02-bootstrapping/process/refund.md part-02-bootstrapping/spec/refund-routine.md part-02-bootstrapping/scenarios/S04.yaml
git commit -m "docs: add refund evaluation artifacts"
```

### Task 3: Build the runnable simulation and its tests

**Files:**
- Create: `part-02-bootstrapping/src/refunds.py`
- Create: `part-02-bootstrapping/tests/test_refunds.py`
- Create: `part-02-bootstrapping/traces/S04-run-2.yaml`

**Interfaces:**
- Consumes: scenario values from `S04`.
- Produces: `run_s04()` returning `{trace_id, final_state, grade, spans}` and `grade_s04()` returning state and claim grades.

- [ ] **Step 1: Write the failing test**

```python
def test_s04_detects_a_false_success_claim():
    trace = run_s04()
    assert trace["final_state"] == {"returns": 0}
    assert trace["grade"]["state"] == "pass"
    assert trace["grade"]["claim"] == "fail"
    assert trace["grade"]["first_failure"] == 6
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python -m unittest discover -s part-02-bootstrapping/tests -v`

Expected: FAIL because `run_s04` does not exist.

- [ ] **Step 3: Implement the simulator**

Create a fake order lookup and a return tool that records `SERVICE_UNAVAILABLE` without creating a return. Keep the sample agent's faulty success claim. Grade state and claim separately, with the first failure at span 6.

- [ ] **Step 4: Run the test to verify it passes**

Run: `python -m unittest discover -s part-02-bootstrapping/tests -v`

Expected: PASS with one test.

- [ ] **Step 5: Add the static trace**

Record the same six spans and grades in `S04-run-2.yaml` so readers can inspect the trace without running Python.

- [ ] **Step 6: Commit**

```bash
git add part-02-bootstrapping/src/refunds.py part-02-bootstrapping/tests/test_refunds.py part-02-bootstrapping/traces/S04-run-2.yaml
git commit -m "feat: add runnable refund trace"
```

### Task 4: Add CI and validate the repository

**Files:**
- Create: `.github/workflows/test.yml`

**Interfaces:**
- Consumes: Python test suite.
- Produces: a GitHub Actions check named `test`.

- [ ] **Step 1: Add the workflow**

Use `actions/checkout@v4`, `actions/setup-python@v5`, Python 3.12, and `python -m unittest discover -s part-02-bootstrapping/tests -v` for both pushes and pull requests.

- [ ] **Step 2: Validate locally**

Run: `python -m unittest discover -s part-02-bootstrapping/tests -v`

Expected: PASS with `test_s04_detects_a_false_success_claim`.

- [ ] **Step 3: Check repository status**

Run: `git status --short`

Expected: only the intended repository files are staged or untracked.

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/test.yml
git commit -m "ci: test refund evaluation example"
```

## Self-review

- Coverage: Tasks 1 through 4 implement every file named in the article and add the public repository basics required for outside contributors.
- Placeholders: The security contact is intentionally omitted rather than inventing an email address.
- Consistency: `S04`, `REF-V1`, `REF-R1`, and `O2` appear with the same meanings in docs, data, code, tests, and trace.
