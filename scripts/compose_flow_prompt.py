"""Append the one fixed template selected for a whole video to a scene prefix."""

from argparse import ArgumentParser
from hashlib import sha256
import json
from pathlib import Path


def find_project_root(script_path: Path) -> Path:
    """Find the repository root from either the root or bundled skill copy."""
    for candidate in script_path.resolve().parents:
        if (candidate / "workflow" / "assets").is_dir() and (
            candidate / "scripts" / "compose_flow_prompt.py"
        ).is_file():
            return candidate
    raise ValueError(f"could not locate project root from {script_path}")


def compose_prompt(
    scene_path: Path,
    profile_path: Path,
    output_path: Path,
    *,
    project_root: Path | None = None,
    override_path: Path | None = None,
) -> bytes:
    """Compose prefix + immutable template + optional scene-specific priority block."""
    root = (project_root or find_project_root(Path(__file__))).resolve()
    profile = json.loads(profile_path.read_text(encoding="utf-8-sig"))
    template_info = profile.get("prompt_template")
    if isinstance(template_info, dict):
        template_path = template_info.get("path")
        expected_hash = template_info.get("sha256")
    else:
        template_path = profile.get("template_path")
        expected_hash = profile.get("template_sha256")
    if not template_path or not expected_hash:
        raise ValueError(
            "profile must provide prompt_template.path/sha256 or legacy "
            "template_path/template_sha256"
        )

    framework = (root / template_path).resolve()
    if not framework.is_relative_to(root):
        raise ValueError("template must be inside this project")
    prefix = scene_path.read_bytes()
    fixed = framework.read_bytes()
    if not prefix.strip():
        raise ValueError("scene prefix is empty")
    actual_hash = sha256(fixed).hexdigest()
    if actual_hash.casefold() != str(expected_hash).strip().casefold():
        raise ValueError("fixed template changed since this video's profile was locked")

    override = override_path.read_bytes() if override_path else b""
    if override_path and not override.strip():
        raise ValueError("scene override is empty")
    inputs = {scene_path.resolve(), profile_path.resolve(), framework.resolve()}
    if override_path:
        inputs.add(override_path.resolve())
    if output_path.resolve() in inputs:
        raise ValueError("output must not overwrite an input")

    composed = prefix.rstrip(b"\r\n") + b"\r\n\r\n" + fixed
    if override:
        composed += b"\r\n\r\n" + override.rstrip(b"\r\n")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(composed)
    if fixed not in composed:
        raise RuntimeError("fixed template was not preserved in composed prompt")
    return composed


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--scene", required=True, type=Path, help="Scene-specific prefix")
    parser.add_argument("--profile", required=True, type=Path, help="One locked template for the whole video")
    parser.add_argument("--output", required=True, type=Path, help="Full Flow prompt to write")
    parser.add_argument(
        "--override",
        type=Path,
        help="Optional scene-specific priority block appended after the unchanged template",
    )
    args = parser.parse_args()

    try:
        composed = compose_prompt(
            args.scene,
            args.profile,
            args.output,
            override_path=args.override,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(f"Wrote {args.output}; fixed framework preserved: True")


if __name__ == "__main__":
    main()
