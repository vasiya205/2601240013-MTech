# Configuration of Mypy, Docker, and GitHub Actions CI/CD

## Objective
To configure static type-checking using `mypy`, containerize a Python application with `Docker`, and automate continuous integration via `GitHub Actions CI/CD`[cite: 3, 41].

## Algorithm
1. Write a typed Python script (`main.py`).
2. Create a `Dockerfile` specifying base images and execution commands.
3. Configure a GitHub Actions workflow YAML file to trigger automated checks on repository pushes.
4. Execute local type checks and container builds.

## Input
* Source file `main.py` containing typed functions and sample execution parameters.

## Output
* Successful `mypy` type validation reports, Docker container build logs, and pipeline execution logs.

## Time & Space Complexity
* **Time Complexity**: $O(S)$ where $S$ is the size of the source codebase processed by type checkers.
* **Space Complexity**: $O(C)$ where $C$ is the disk space occupied by the Docker container image.
