#!/usr/bin/env python
# liquidcalc
# Copyright (c) 2020  Michael Sasser <Michael@MichaelSasser.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

from argparse import Namespace

import pytest

from liquidcalc.calc import Calc


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"

TEST_NS: Namespace = Namespace(
    aroma=1.8, nicotine=10.0, pg=50.0, quantity=200.0, shot=20.0, vg=40.0,
)


def test_parser_prop_quantity() -> None:
    # Setup
    desired: float = 203.6

    # Exercise
    calc: Calc = Calc(TEST_NS)

    actual: float = calc.quantity

    # Verify
    assert desired == pytest.approx(actual, 0.01)

    # Cleanup - None


def test_parser_prop_nicotine() -> None:
    # Setup
    desired: float = 9.82318271119843

    # Exercise
    calc: Calc = Calc(TEST_NS)

    actual: float = calc.nicotine

    # Verify
    assert desired == pytest.approx(actual, 0.01)

    # Cleanup - None


def test_parser_prop_shot() -> None:
    # Setup
    desired: float = 100.0

    # Exercise
    calc: Calc = Calc(TEST_NS)

    actual: float = calc.shot

    # Verify
    assert desired == pytest.approx(actual, 0.01)

    # Cleanup - None


def test_parser_prop_pg() -> None:
    # Setup
    desired: float = 50.0

    # Exercise
    calc: Calc = Calc(TEST_NS)

    actual: float = calc.pg

    # Verify
    assert desired == pytest.approx(actual, 0.01)

    # Cleanup - None


def test_parser_prop_vg() -> None:
    # Setup
    desired: float = 40.0

    # Exercise
    calc: Calc = Calc(TEST_NS)

    actual: float = calc.vg

    # Verify
    assert desired == pytest.approx(actual, 0.01)

    # Cleanup - None


def test_parser_prop_h2o() -> None:
    # Setup
    desired: float = 10.0

    # Exercise
    calc: Calc = Calc(TEST_NS)

    actual: float = calc.h2o

    # Verify
    assert desired == pytest.approx(actual, 0.01)

    # Cleanup - None


def test_parser_prop_aroma() -> None:
    # Setup
    desired: float = 3.6

    # Exercise
    calc: Calc = Calc(TEST_NS)

    actual: float = calc.aroma

    # Verify
    assert desired == pytest.approx(actual, 0.01)

    # Cleanup - None


def test_parser_str() -> None:
    # Setup
    desired: str = (
        "Calc(quantity=203.6 ml, "
        "nicotine=9.82318271119843 mg/ml, "
        "shot=100.0 ml, "
        "pg=50.0 ml, "
        "vg=40.0 ml, "
        "h2o=10.0 ml, "
        "aroma=3.6 ml)"
    )

    # Exercise
    calc: Calc = Calc(TEST_NS)

    actual: str = str(calc)

    # Verify
    assert actual == desired

    # Cleanup - None


def test_parser_repr() -> None:
    # Setup
    desired: str = (
        "Calc("
        "quantity=200.0 ml, "
        "shot=20.0 mg/ml, "
        "nicotine=10.0 %, "
        "pg=50.0 %, "
        "vg=40.0 %, "
        "aroma=1.8 %"
        ")"
    )

    # Exercise
    calc: Calc = Calc(TEST_NS)

    actual: str = repr(calc)

    # Verify
    assert actual == desired

    # Cleanup - None


# vim: set ft=python :
