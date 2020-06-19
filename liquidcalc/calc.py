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


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


class Calc(object):
    def __init__(self, args: argparse.Namespace) -> None:
        self._quantity: float = float(args.quantity)
        self._aroma: float = float(args.aroma)
        self._pg: float = float(args.pg)
        self._vg: float = float(args.vg)
        self._nicotine: float = float(args.nicotine)
        self._shot: float = float(args.shot)

    @property
    def aroma(self) -> float:
        return self._aroma * self._quantity / 100.0

    @property
    def shot(self) -> float:
        return self._quantity * self._nicotine / self._shot

    @property
    def pg(self) -> float:
        return self._pg * (self._quantity - self.shot) / 100.0

    @property
    def vg(self) -> float:
        return self._vg * (self._quantity - self.shot) / 100.0

    @property
    def h2o(self) -> float:
        return self._quantity - self.shot - self.pg - self.vg

    @property
    def quantity(self) -> float:
        # test: self._quantity + aroma
        return self.pg + self.vg + self.h2o + self.shot + self.aroma

    @property
    def nicotine(self) -> float:
        return self.shot * self._shot / self.quantity

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            "("
            f"quantity={self.quantity} ml, "
            f"nicotine={self.nicotine} mg/ml, "
            f"shot={self.shot} ml, "
            f"pg={self.pg} ml, "
            f"vg={self.vg} ml, "
            f"h2o={self.h2o} ml, "
            f"aroma={self.aroma} ml"
            ")"
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            "("
            f"quantity={self._quantity} ml, "
            f"shot={self._shot} mg/ml, "
            f"nicotine={self._nicotine} %, "
            f"pg={self._pg} %, "
            f"vg={self._vg} %, "
            f"aroma={self._aroma} %"
            ")"
        )


# vim: set ft=python :
