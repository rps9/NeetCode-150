from rich.console import Console

console = Console(highlight=False)

def test(func, test_cases):
    for i, case in enumerate(test_cases):
        args = case.get("args", [])
        expected = case.get("expected_result")

        # Normalize args to tuple if not already
        if not isinstance(args, (list, tuple)):
            args = (args,)
        elif isinstance(args, list):
            args = tuple(args)

        try:
            result = func(*args)
            passed = result == expected
        except Exception as e:
            result = f"Exception: {type(e).__name__} - {e}"
            passed = False

        color = "bold green" if passed else "bold red"

        console.print(f"[{color}]Test Case {i + 1}")
        for j, arg in enumerate(args):
            console.print(f"[{color}]Input {j + 1}: {arg!r}")
        console.print(f"[{color}]Output: {result!r}")
        console.print(f"[{color}]Expected: {expected!r}")
        console.print(f"[{color}]Test Passed: {passed}")
        console.print("[dim]-" * 40)
