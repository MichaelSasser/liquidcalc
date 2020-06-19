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

from typing import List
from typing import Tuple

from tabulate import tabulate  # pylint: disable=E0401


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


def get_table(
    ingredients: List[Tuple[str, float, str]], quantity: float, nicotine: float
) -> str:
    table: str = tabulate(
        ingredients,
        headers=("Index", "Ingredient", "Quantity", "Unit"),
        tablefmt="psql",
        floatfmt="5.1f",
    )

    table += (
        f"\nActual Quantity = {quantity:6.2f} ml\n"
        f"Actual Nicotine = {nicotine:6.2f} mg/ml"
    )
    return table


# vim: set ft=python :
