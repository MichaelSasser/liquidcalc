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

from liquidcalc import __version__


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=("Calculate a simple liquid mixture."),
        epilog=(
            "Keep in mind, LiquidCalc adds the aroma to the mixture "
            "afterwards. For more informationen have a look at "
            "https://github.com/MichaelSasser/liquidcalc"
        ),
    )

    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument(
        "quantity",
        type=float,
        help="the amount of liquid that should be produced in ml",
    )
    parser.add_argument(
        "-a",
        "--aroma",
        type=float,
        default=1.6,
        help="the percentage of aroma, that will be added",
    )
    parser.add_argument(
        "-p",
        "--pg",
        type=float,
        default=50.0,
        help="the quantity of Propane-1,2-diol (PG) in percent",
    )
    parser.add_argument(
        "-v",
        "--vg",
        type=float,
        default=40.0,
        help="the quantity of Propane-1,2,3-triol (VG) in percent",
    )
    parser.add_argument(
        "-n",
        "--nicotine",
        type=float,
        default=10.0,
        help="The amount of nicotine of 1 ml in the liquid in mg/ml",
    )
    parser.add_argument(
        "-s",
        "--shot",
        type=float,
        default=20.0,
        help="the amount of nicotine of 1 ml in mg/ml",
    )
    return parser


# vim: set ft=python :
