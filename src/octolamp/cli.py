from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from octolamp.core import LampState, describe, set_brightness, toggle

STATE_PATH = Path(".octolamp_state.json")


def load_state() -> LampState:
    if not STATE_PATH.exists():
        return LampState()
    try:
        data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        return LampState(on=bool(data.get("on", False)), brightness=int(data.get("brightness", 50)))
    except Exception:
        # If file is corrupted, reset safely
        return LampState()


def save_state(state: LampState) -> None:
    STATE_PATH.write_text(
        json.dumps({"on": state.on, "brightness": state.brightness}, indent=2),
        encoding="utf-8",
    )


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="octolamp", description="A tiny lamp CLI.")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status", help="Show current lamp status")

    sub.add_parser("toggle", help="Toggle ON/OFF")

    b = sub.add_parser("brightness", help="Set brightness 0..100")
    b.add_argument("value", type=int, help="Brightness value (0..100)")

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    state = load_state()

    if args.cmd == "status":
        print(describe(state))
        return 0

    if args.cmd == "toggle":
        state = toggle(state)
        save_state(state)
        print(describe(state))
        return 0

    if args.cmd == "brightness":
        state = set_brightness(state, args.value)
        save_state(state)
        print(describe(state))
        return 0

    print("Unknown command", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
