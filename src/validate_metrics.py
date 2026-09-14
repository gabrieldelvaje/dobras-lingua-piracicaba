#!/usr/bin/env python3
"""Validate the metrics used in the Piracicaba tongue-rolling carousel."""

from __future__ import annotations

import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "respostas_pesquisa.csv"


def wilson_interval(successes: int, n: int, z: float = 1.95996398454) -> tuple[float, float]:
    p = successes / n
    denominator = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denominator
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denominator
    return center - half, center + half


def main() -> None:
    with DATA.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 79, f"Expected 79 responses, found {len(rows)}"

    santa_rita = [
        r for r in rows
        if r["resposta_mora_em_piracicaba_original"].strip().casefold() == "santa rita"
    ]
    assert len(santa_rita) == 1, "Expected exactly one 'santa rita' response"
    assert santa_rita[0]["mora_em_piracicaba_normalizado"] == "Sim"

    piracicaba = [r for r in rows if r["mora_em_piracicaba_normalizado"] == "Sim"]
    others = [r for r in rows if r["mora_em_piracicaba_normalizado"] == "Não"]
    yes = [r for r in piracicaba if r["consegue_dobrar_lingua"] == "Sim"]
    no = [r for r in piracicaba if r["consegue_dobrar_lingua"] == "Não"]

    assert len(piracicaba) == 73
    assert len(others) == 6
    assert len(yes) == 55
    assert len(no) == 18

    p = len(yes) / len(piracicaba)
    lower, upper = wilson_interval(len(yes), len(piracicaba))

    assert round(p * 100, 1) == 75.3
    assert round(lower * 100, 1) == 64.4
    assert round(upper * 100, 1) == 83.8

    print("Validation passed")
    print(f"Total responses: {len(rows)}")
    print(f"Piracicaba sample: {len(piracicaba)}")
    print(f"Other cities: {len(others)}")
    print(f"Tongue rollers in Piracicaba: {len(yes)}/{len(piracicaba)} = {p:.1%}")
    print(f"Wilson 95% CI: {lower:.1%} to {upper:.1%}")


if __name__ == "__main__":
    main()
