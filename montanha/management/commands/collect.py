# -*- coding: utf-8 -*-
#
# Copyright (©) 2010-2013 Gustavo Noronha Silva
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.core.management.base import BaseCommand, CommandError


full_scan = False
debug_enabled = False


class Command(BaseCommand):
    args = "<source> [mandate_start_year]"
    help = "Collects data for a number of sources"

    def handle(self, *args, **options):
        global debug_enabled
        global full_scan

        if "debug" in args:
            debug_enabled = True

        if "full-scan" in args:
            full_scan = True

        if "almg" in args:
            from almg import ALMG
            almg = ALMG(debug_enabled, full_scan)
            almg.update_legislators()
            almg.update_data()
