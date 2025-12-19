from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LampState:
    on: bool = False
    brightness: int = 50  # 0..100


def clamp_brightness(value: int) -> int:
    return max(0, min(100, value))


def toggle(state: LampState) -> LampState:
    return LampState(on=not state.on, brightness=state.brightness)


def set_brightness(state: LampState, brightness: int) -> LampState:
    return LampState(on=state.on, brightness=clamp_brightness(brightness))


def describe(state: LampState) -> str:
    status = "ON" if state.on else "OFF"
    return f"Lamp is {status} · brightness={state.brightness}%"
