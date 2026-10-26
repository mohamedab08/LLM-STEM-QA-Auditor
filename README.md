# LLM STEM & Quantitative QA Auditor

A benchmark and evaluation framework designed to audit Large Language Model (LLM) outputs across Advanced STEM, Pre-Medical Sciences, and Quantitative Reasoning.

## Features
- **RLHF-Style Pairwise Benchmarking:** Evaluates competing model outputs for step-by-step logical consistency, factual accuracy, and hallucination detection.
- **LaTeX & Mathematical Validation:** Verifies rendering integrity and mathematical precision of quantitative notation.
- **Automated Validation:** Includes a Python verification script (`validator.py`) to audit evaluation datasets for required metrics, score integrity, and syntax rules.

## Data Structure
Evaluations are structured in `evaluations.json` containing:
- High-stakes STEM/Medical prompts
- Pairwise model responses (Response A vs. Response B)
- Detailed human justification and error taxonomy breakdown
