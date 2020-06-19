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

from liquidcalc.table import get_table


def test_table() -> None:
    # Setup

    desired: str = """+---------+--------------+------------+
| Index   |   Ingredient | Quantity   |
|---------+--------------+------------|
| a       |          1.1 | b          |
| c       |          2.2 | d          |
+---------+--------------+------------+
Actual Quantity =  12.34 ml
Actual Nicotine =  56.78 mg/ml"""

    # Exercise
    actual: str = get_table([("a", 1.1, "b"), ("c", 2.2, "d")], 12.34, 56.78)

    print(actual)
    # Verify
    assert desired == actual

    # Cleanup - None


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


# vim: set ft=python :
