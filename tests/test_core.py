from octolamp.core import LampState, clamp_brightness, describe, set_brightness, toggle


def test_clamp_brightness():
    assert clamp_brightness(-10) == 0
    assert clamp_brightness(0) == 0
    assert clamp_brightness(50) == 50
    assert clamp_brightness(100) == 100
    assert clamp_brightness(999) == 100


def test_toggle():
    s = LampState(on=False, brightness=50)
    s2 = toggle(s)
    assert s2.on is True
    assert s2.brightness == 50


def test_set_brightness():
    s = LampState(on=True, brightness=10)
    s2 = set_brightness(s, 120)
    assert s2.on is True
    assert s2.brightness == 100


def test_describe():
    assert "OFF" in describe(LampState(on=False, brightness=33))
