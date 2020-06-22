#!/usr/bin/env sh
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

# Use the dockerfile with:
# podman build . -t liquidcalc:latest && podman run liquidcalc:latest

poetry run python -m cProfile -s cumtime app.py 200
poetry run pre-commit run -a
poetry run pytest --cov
poetry build
ls -la dist


# vim: set ft=sh :
