# input-domain-modeling

A Python-based tool for systematic test case generation using input domain modeling techniques. This project helps software testers and developers design efficient, comprehensive test suites by automatically generating combinations of input values based on defined characteristics and blocks.

---

## Table of Contents
- [Usage](#usage)
  - [Command Line](#command-line)
  - [BDD Scenarios](#bdd-scenarios)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Testing & CI](#testing--ci)
- [Acknowledgements](#acknowledgements)

---

## Usage

### Command Line
- Generate test cases by specifying characteristics, abstract blocks, and mode:

  ```bash
  python input_domain_modeling.py \
    --characteristics size:S,M,L color:Red,Green,Blue \
    --abstract_blocks shirt:size,color \
    --mode ACoc
  ```

- Supported modes:
  - `ACoc`: All Combinations of Characteristics
  - `MBCC`: Minimal Base Case Combination
  - `ECC`: Each Choice Coverage
  - `BCC`: Base Case Combination

### BDD Scenarios
- Behavior-driven development scenarios are defined in `features/input_domain_modeling.feature`.
- Run BDD tests with Behave:

  ```bash
  behave
  ```

---

## Features
- **Input Domain Modeling**: Define characteristics and blocks to model input space.
- **Test Case Generation**: Four modes for generating combinations:
  - All combinations (ACoc)
  - Minimal base case (MBCC/BCC)
  - Each choice coverage (ECC)
- **Command Line Interface**: Flexible argument parsing for custom test generation.
- **BDD Support**: Write and execute human-readable test scenarios.
- **Unit Testing**: Comprehensive unit tests for all core logic.
- **Coverage Reporting**: Integrated with coverage tools for quality assurance.

---

## Installation

### Prerequisites
- Python 3.8+
- pip

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Quick Start

1. **Generate Test Cases**
   ```bash
   python input_domain_modeling.py --characteristics size:S,M,L color:Red,Green,Blue --abstract_blocks shirt:size,color --mode ACoc
   ```
2. **Run Unit Tests**
   ```bash
   python -m unittest test_input_domain_modeling.py
   ```
3. **Run BDD Tests**
   ```bash
   behave
   ```

---

## Project Structure
```
Software_testing_b/
│
├── input_domain_modeling.py         # Main test case generator
├── test_input_domain_modeling.py    # Unit tests
├── requirements.txt                 # Python dependencies
├── features/                        # BDD scenarios
│   ├── input_domain_modeling.feature
│   └── steps/                       # Step definitions
│       └── steps.py
├── htmlcov/                         # Coverage reports
└── README.md                        # This file
```

---

## Configuration
- Customize characteristics, blocks, and modes via command line arguments.
- BDD scenarios can be extended in `features/input_domain_modeling.feature`.

---

## Testing & CI
- Run unit tests:
  ```bash
  python -m unittest test_input_domain_modeling.py
  ```
- Run BDD tests:
  ```bash
  behave
  ```
- Coverage reports generated in `htmlcov/`.

---

## Acknowledgements
- [Behave](https://behave.readthedocs.io/en/latest/)
- [Python Coverage](https://coverage.readthedocs.io/)
- Open source contributors

---

input-domain-modeling: Efficient, systematic test case generation for robust software testing.
