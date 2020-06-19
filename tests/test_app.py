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

import sys

from typing import List
from unittest.mock import patch

import pytest

from liquidcalc.app import main


TEST_ARGS: List[str] = [
    sys.argv[0],
    "200.0",
    "--aroma=1.6",
    "--nicotine=10.0",
    "--pg=50.0",
    "--shot=20.0",
    "--vg=40.0",
]


def test_main_no_exception() -> None:
    # Setup - None
    # Exercise - None
    # Verify
    with patch.object(sys, "argv", TEST_ARGS):
        try:
            main()
        except Exception as e:  # pylint: disable=W0703
            pytest.fail(e)

    # Cleanup - None


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


# vim: set ft=python :
