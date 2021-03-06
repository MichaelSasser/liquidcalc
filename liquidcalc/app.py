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

import argparse
import sys

from typing import List
from typing import Tuple

from .calc import Calc
from .parser import init_parser
from .table import get_table


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


def main() -> int:
    parser: argparse.Namespace = init_parser(sys.argv[1:])
    calc: Calc = Calc(parser)

    ingredients: List[Tuple[str, float, str]] = []

    if calc.shot != 0.0:
        ingredients.append(("Shot", calc.shot, "ml"),)
    if calc.pg != 0.0:
        ingredients.append(("Propane-1,2-diol (PG)", calc.pg, "ml"),)
    if calc.vg != 0.0:
        ingredients.append(("Propane-1,2,3-triol (VG)", calc.vg, "ml"),)
    if calc.h2o != 0.0:
        ingredients.append(("H\N{SUBSCRIPT TWO}O (Water)", calc.h2o, "ml"),)
    if calc.aroma != 0.0:
        ingredients.append(("Aroma", calc.aroma, "ml"),)

    if len(ingredients) == 1:
        print("If you set all ingredients to 0.0, there is nothing to do.")
        return 1

    print(get_table(ingredients, calc.quantity, calc.nicotine))
    return 0


# vim: set ft=python :
