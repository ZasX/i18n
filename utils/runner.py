import os

def get_project_root() -> str:
    """Get the project root (assuming utils/ is one level down from root)."""
    utils_dir = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(utils_dir, '..'))

def get_input_paths(day: str) -> dict[str, str]:
    """Get paths to test and real input files for a given day."""
    project_root = get_project_root()
    input_dir = os.path.join(project_root, "inputs", day)

    return {
        "test_input": os.path.join(input_dir, "test-input"),
        "real_input": os.path.join(input_dir, "input"),
        "test_answer": os.path.join(input_dir, "test-answer"),
    }

def load_input(filepath: str, encoding: str) -> str:
    """Reads input file into a list of lines."""
    with open(filepath, "r", encoding=encoding) as file:
        return file.read()
        return [line[:-1] for line in file.readlines()]

def run_puzzle(day: str, solve_func, encoding="UTF-8"):
    """
    Runs the puzzle solution for the given day.

    - Loads test input.
    - Checks the result against expected output.
    - If the test passes, runs the real input.
    """
    paths = get_input_paths(day)

    test_input = load_input(paths["test_input"], encoding)

    if os.path.exists(paths["test_answer"]):
        with open(paths["test_answer"], "r", encoding="utf-8") as file:
            expected_answer = file.read().strip()
    else:
        raise FileNotFoundError(f"No test-answer file found for day {day}.")

    # Run with test input
    test_result = str(solve_func(test_input))

    print(f"Test result: {test_result} (Expected: {expected_answer})")

    if test_result != expected_answer:
        print("❌ Test failed. Aborting real input.")
        return

    print("✅ Test passed! Running real input...")

    real_input = load_input(paths["real_input"], encoding)
    real_result = solve_func(real_input)

    print(f"🎉 Final result for day {day}: {real_result}")
