"""Tests for passforge (run with: python -m pytest test_passforge.py -v)."""

import string

import pytest

from passforge import (
    build_pool,
    generate_password,
    score_password,
    strength_label,
)


# --- generator tests ---

def test_default_length():
    assert len(generate_password()) == 16


def test_custom_length():
    assert len(generate_password(length=24)) == 24


def test_length_minimum_enforced():
    with pytest.raises(ValueError):
        generate_password(length=3)


def test_no_symbols_excludes_symbols():
    pwd = generate_password(length=50, use_symbols=False)
    assert all(c.isalnum() for c in pwd)


def test_no_ambiguous_excludes_confusables():
    pool = build_pool(no_ambiguous=True)
    for c in "l1IO0":
        assert c not in pool


def test_password_has_character_variety():
    pwd = generate_password(length=20)
    assert any(c in string.ascii_lowercase for c in pwd)
    assert any(c in string.ascii_uppercase for c in pwd)
    assert any(c in string.digits for c in pwd)


def test_generated_passwords_are_unique():
    passwords = {generate_password() for _ in range(50)}
    assert len(passwords) == 50


# --- strength tests ---

def test_empty_password_is_weak():
    assert strength_label("")[0] == "Weak"


def test_short_password_is_weak():
    assert strength_label("abc")[0] == "Weak"


def test_strong_password_scores_high():
    label, score = strength_label("Xk9#mQ2$vL7&pR4!")
    assert label in ("Strong", "Very Strong")
    assert score > 60


def test_very_long_password_is_very_strong():
    label, score = strength_label("aB3$" * 6)  # 24 chars
    assert label == "Very Strong"
    assert score >= 81


def test_score_capped_at_100():
    assert score_password("Aa1!" * 10) == 100


def test_score_is_deterministic():
    assert score_password("hello123") == score_password("hello123")
