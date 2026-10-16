# Vulnerability Report Prioritization Engine

## Problem statement

Security teams receive far more reported vulnerabilities than they can remediate in a single release window. This project ranks reported vulnerabilities by risk and selects the best set of items to remediate under a limited budget.

## Motivation

The goal is to blend computation, transparent scoring, and explainable decision support. The engine demonstrates a realistic security prioritization workflow for a college project while being technically solid and testable.

## Objectives

- Accept vulnerability CSV data
- Validate records and detect duplicate IDs
- Calculate risk using a transparent scoring model
- Rank vulnerable items greedily
- Optimize remediation under budget using dynamic programming
- Present explainable results in a professional dashboard
- Include unit, integration, and property-based tests
- Build a repeatable CI, Docker, and documentation workflow

## Features

- CSV ingestion with validation
- Weighted risk formula with centralized configuration
- Greedy ranking for urgency assessment
- 0/1 knapsack optimization for budget-constrained selection
- Streamlit dashboard with charts and export buttons
- Timing instrumentation and complexity display
- Comprehensive pytest plus Hypothesis coverage

## System architecture

The application is organized around a small domain model, scoring strategy, algorithms, services, and UI.

- Data validation and file loading: `app/data/`
- Risk model: `app/strategies/`
- Ranking and knapsack logic: `app/algorithms/`
- Orchestration: `app/services/`
- Dashboard: `app/ui/`
- Tests: `tests/`

## Workflow

1. Load vulnerability CSV records.
2. Validate each row and reject malformed or duplicate data.
3. Calculate each vulnerability risk score.
4. Rank using greedy sorting by risk.
5. Select the best set under budget with dynamic programming.
6. Render results in the dashboard.
7. Export ranked CSV, plan CSV, and JSON summary.

## Risk formula

Risk Score = 0.45 * Severity + 0.30 * Exploitability + 0.25 * Asset Criticality.

This formula lives in a single centralized configuration dict: `app/strategies/base.py`.

## Greedy algorithm

The greedy approach sorts vulnerabilities by descending risk, then by asset criticality, exploitability, and vulnerability ID. This is appropriate for quick ranking when the goal is to answer: *Which vulnerability should be addressed first?*

Time complexity: O(n log n)

## Dynamic programming

The 0/1 knapsack algorithm chooses a combination of vulnerabilities that maximizes total risk reduction while respecting the remediation budget. This addresses the budget question: *Which combination provides the maximum total benefit under a limit?*

Time complexity: O(nB)
Space complexity: O(B)

## Data structures

The project uses dataclasses, tuples, dictionaries, lists, sets, comprehensions, iterators, and generators. These structures keep the application efficient and readable.

## OOP architecture

The core design includes:

- `Vulnerability`: an immutable domain entity
- `RemediationPlan`: selected remediation items and totals
- `PrioritizationEngine`: orchestration layer
- `RiskScoringStrategy`: abstract strategy for scoring
- `WeightedRiskScoringStrategy`: concrete implementation

This demonstrates strategy-based composition and maintainable design.

## Functional programming

The project uses pure functions, higher-order processing, list comprehensions, and generators. The scoring function is pure and deterministic, while the data loader yields rows with a generator-based workflow.

## Concurrency

The loader supports multiple CSV files and uses `ThreadPoolExecutor` for independent I/O-bound reads. The project explains why this is appropriate: the workload is file I/O rather than CPU-bound number crunching. Python's GIL is not a barrier for this use case, whereas multiprocessing is better suited for heavy CPU-bound work.

## Testing

The project uses `pytest`, `Hypothesis`, and coverage tracking. Tests cover unit logic, CSV ingestion, end-to-end workflow, and property-based invariants.

## Complexity analysis

- Greedy ranking: O(n log n)
- Dynamic programming: O(nB)
- Space: O(B) for DP; O(n) for ranking storage

## AI-assisted development

This project was developed using a specification-first workflow: the requirements were translated into modules, implementation tasks, and validation steps. AI assisted with scaffolding, refactoring, and test generation, while human review and runtime verification were used to confirm correctness. AI-generated code was never accepted without testing and review.

## Docker

The project includes a Dockerfile and `.dockerignore` so it can run inside a container.

## CI/CD

The GitHub Actions workflow runs Ruff, mypy, pytest, and coverage generation for every push and pull request.

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Running locally

```bash
python -m streamlit run app/main.py
```

## Running tests

```bash
pytest
```

## Sample output

The engine produces a ranked table, chart summaries, a remediation plan, and explainability notes. Sample data is stored in `data/sample_vulnerabilities.csv`.

## Future enhancements

- Integrate with real vulnerability scanners
- Add authentication and role-based access control
- Add a database-backed historical dashboard
- Support custom scoring policies per business unit
- Add export to PDF and Excel formats

## Files created

```text
app/
  __init__.py
  main.py
  algorithms/
  data/
  models/
  services/
  strategies/
  ui/
  utils/

data/
  sample_vulnerabilities.csv
docs/
  algorithms.md
  architecture.md
  ai-assisted-development.md
  presentation.md
  testing.md
  computational-thinking.md
tests/
```
