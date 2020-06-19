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
from typing import List

import pytest

from liquidcalc.parser import init_parser


TEST_NS: List[str] = [
    "200.0",
    "--aroma=1.6",
    "--nicotine=10.0",
    "--pg=50.0",
    "--shot=20.0",
    "--vg=40.0",
]


def test_parser_quantity() -> None:
    # Setup
    ns: Namespace = init_parser(TEST_NS)
    desired: float = 200.0

    # Exercise
    actual: float = ns.quantity

    # Verify
    assert desired == pytest.approx(actual, 0.01)

    # Cleanup - None


def test_parser_aroma() -> None:
    # Setup
    ns: Namespace = init_parser(TEST_NS)

    desired: float = 1.6

    # Exercise
    actual: float = ns.aroma

    # Verify
    assert desired == pytest.approx(actual, 0.01)

    # Cleanup - None


def test_parser_pg() -> None:
    # Setup
    ns: Namespace = init_parser(TEST_NS)

    desired: float = 50.0

    # Exercise
    actual: float = ns.pg

    # Verify
    assert desired == pytest.approx(actual, 0.01)

    # Cleanup - None


def test_parser_vg() -> None:
    # Setup
    ns: Namespace = init_parser(TEST_NS)

    desired: float = 40.0

    # Exercise
    actual: float = ns.vg

    # Verify
    assert desired == pytest.approx(actual, 0.01)

    # Cleanup - None


def test_parser_nicotine() -> None:
    # Setup
    ns: Namespace = init_parser(TEST_NS)

    desired: float = 10.0

    # Exercise
    actual: float = ns.nicotine

    # Verify
    assert desired == pytest.approx(actual, 0.01)

    # Cleanup - None


def test_parser_shot() -> None:
    # Setup
    ns: Namespace = init_parser(TEST_NS)

    desired: float = 20.0

    # Exercise
    actual: float = ns.shot

    # Verify
    assert desired == pytest.approx(actual, 0.01)

    # Cleanup - None


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


# vim: set ft=python :
