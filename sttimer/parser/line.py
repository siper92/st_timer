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


class DebugLine():

    # Fields for the computerized format:
    #   @URL http://xdebug.org/docs/execution_trace

    # level of the function in the execution stack
    FUNCTION_LEVEL_KEY = 0
    # function entry type
    FUNCTION_ENTRY_TYPE_KEY = 2
    ENTRY_TYPE_ENTER = 0
    ENTRY_TYPE_EXIT = 1
    ENTRY_TYPE_RETURN = "R"
    # time since start of the execution
    TIME_INDEX_KEY = 3
    # memory usage at the moment
    FUNCTION_MEMORY_USAGE_KEY = 4
    # function namehow compression works
    FUNCTION_NAME_KEY = 5
    # function type
    FUNCTION_TYPE_KEY = 5
    TYPE_USER_DEFINED = 1
    TYPE_INTERNAL = 0
    # file where the function is located
    FILE_PATH_KEY = 8

    def __init__(self, line=None):
        pass

    def get_level(self, line):
        try:
            return line[self.FUNCTION_LEVEL_KEY]
        except IndexError as e:
            print(e)

    def get_type(self, line):
        try:
            return line[self.FUNCTION_LEVEL_KEY]
        except IndexError as e:
            print(e)

    def get_file_path(self, line):
        try:
            if len(line) > 8:
                return line[self.FILE_PATH_KEY]
            if (len(line) > 2) and \
                    (int(line[self.FUNCTION_ENTRY_TYPE_KEY]) != self.ENTRY_TYPE_EXIT):
                # No file found the the function type is not exit
                print('No file')
            return None
        except IndexError as e:
            print(e)