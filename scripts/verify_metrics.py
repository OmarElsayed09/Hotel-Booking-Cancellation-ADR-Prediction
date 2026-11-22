"""Validate recorded training metrics and write a provenance report.

This DOES NOT recompute model quality without training or the held-out dataset.
"""
import hashlib
import json
import platform
import subprocess
from pathlib import Path

def validate():
    source = Path("models/metrics_summary.json")
    payload = json.loads(source.read_text(encoding="utf-8"))
    report = {
        "type": "stored_metrics_integrity",
        "independently_recomputed": False,
        "metrics_file": str(source),
        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "python_version": platform.python_version(),
        "git_commit": subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=False
        ).stdout.strip() or None,
        "top_level_keys": sorted(payload),
    }
    return report

if __name__ == "__main__":
    result = validate()
    output = Path("artifacts/metrics-integrity.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
