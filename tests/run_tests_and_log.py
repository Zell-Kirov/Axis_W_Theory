import subprocess
import os
import re

os.makedirs("logs", exist_ok=True)

tests = [
    "test_entity",
    "test_universe",
    "test_blackhole",
    "test_physics_consistency",
    "test_extreme_conditions"
]

summary = {}

print(" Starting the Axis_W validation test suite...\n")

for test in tests:
    path = f"tests/{test}.py"
    log_path = f"logs/{test}.log"

    with open(log_path, "w") as log_file:
        result = subprocess.run(
            ["python", "-m", "unittest", path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        log_file.write(result.stdout)

    # Quick log analysis for stats
    passed = len(re.findall(r"\.\n", result.stdout))
    failed = len(re.findall(r"FAIL:", result.stdout))
    errors = len(re.findall(r"ERROR:", result.stdout))
    total = passed + failed + errors

    summary[test] = {
        "total": total,
        "passed": total - failed - errors,
        "failed": failed,
        "errors": errors
    }

# Final summary in terminal
print(" Test results summary per module:\n")
for test_name, stats in summary.items():
    print(f" {test_name}.py → {stats['passed']} / {stats['total']} tests passed | {stats['failed']} failures | {stats['errors']} errors")

print("\nAll logs are available in the /logs/ folder")
print("You can now compare, version, and publish your scientific validation ")
