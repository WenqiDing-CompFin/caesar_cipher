"""Unit tests for the Caesar cipher module."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from caesar_cipher import decrypt, encrypt  # noqa: E402


def test_known_example_shift_three():
    assert encrypt("information security", 3) == "lqirupdwlrq vhfxulwb"
    assert decrypt("lqirupdwlrq vhfxulwb", 3) == "information security"


def test_roundtrip_for_multiple_shifts():
    for shift in range(1, 26):
        text = "The quick brown fox jumps over the lazy dog."
        assert decrypt(encrypt(text, shift), shift) == text


def test_non_letters_are_preserved():
    assert encrypt("hello, world! 123", 1) == "ifmmp, xpsme! 123"


def test_case_is_preserved():
    assert encrypt("AbC", 1) == "BcD"


def test_negative_shift_wraps_correctly():
    assert encrypt("abc", -1) == "zab"


def test_non_ascii_text_is_preserved_and_roundtrips():
    text = "中文 café Ångström! Hello"
    encoded = encrypt(text, 3)
    assert encoded == "中文 fdié Åqjvwuöp! Khoor"
    assert decrypt(encoded, 3) == text
