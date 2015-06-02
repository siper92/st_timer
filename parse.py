# Copyright (C) 2015  Todor Mitev
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import csv
import sttimer.parser.line as line_parser

parser = line_parser.DebugLine()
list_of_files = []
with open("./trace.89137710.xt") as tsv:
    count = 0
    for line in csv.reader(tsv, dialect="excel-tab"):
        if len(line) < 3:
            continue
        if count < 100 and (len(line) > 3):
            # print(line)
            list_of_files.append(parser.get_file_path(line))
        count += 1
    print(count)

print(list_of_files)
print("end")
