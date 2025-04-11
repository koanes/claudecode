# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build Commands
- Install dependencies: `pip install -r requirements.txt`
- Run tests: `pytest`
- Run single test: `pytest path/to/test.py::test_function`
- Type checking: `mypy .`
- Linting: `flake8`

## Code Style Guidelines
- Document every external import with its purpose
- For each specialized method, explain how it works with examples and line references
- For all formulas or calculations:
  ```python
  # Calculate adjusted risk score
  # Purpose: Normalizes risk based on historical patterns and applies weighting factors
  # Formula explanation: 
  #   - Base risk (0-100) is adjusted for market volatility (vol_factor)
  #   - Time decay applied (1/log(days_active+1)) to reduce importance of older events
  #   - Weight factors calibrated to historical outcomes
  # Exceptions/Edge cases:
  #   - For new accounts (days_active < 7), use alternative calculation
  #   - If volatility > 30%, cap the adjustment factor at 1.5
  risk_score = base_risk * vol_factor * (1/math.log(days_active+1)) * weight
  ```
- Add SIPOC-style comments for each code block (Supplier-Input-Process-Output-Customer)
- Use descriptive variable names that explain their purpose
- Break complex operations into smaller, well-named functions
- Include explicit type hints
- Handle errors with clear messages explaining the failure cause