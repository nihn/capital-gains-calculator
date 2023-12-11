"""Test raw format support."""

from pathlib import Path
import subprocess
import sys


def test_run_with_raw_files_no_balance_check() -> None:
    """Runs the script and verifies it doesn't fail."""
    cmd = [
        sys.executable,
        "-m",
        "cgt_calc.main",
        "--year",
        "2022",
        "--raw",
        "tests/test_data/raw/test_data.csv",
        "--no-pdflatex",
        "--no-balance-check",
    ]
    result = subprocess.run(cmd, check=True, capture_output=True)
    assert result.stderr == b"", "Run with example files generated errors"
    expected_file = Path("tests") / "test_data" / "raw/expected_output.txt"
    expected = expected_file.read_text()
    cmd_str = " ".join([param if param else "''" for param in cmd])
    assert result.stdout.decode("utf-8") == expected, (
        "Run with example files generated unexpected outputs, "
        "if you added new features update the test with:\n"
        f"{cmd_str} > {expected_file}"
    )
