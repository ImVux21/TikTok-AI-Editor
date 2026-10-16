"""Compatibility entry point; delegate to the single maintained composer."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[4]
    runpy.run_path(str(root / "scripts" / "compose_flow_prompt.py"), run_name="__main__")
