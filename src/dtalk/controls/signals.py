#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 ~ 2014 Deepin, Inc.
#               2011 ~ 2014 Hou ShaoHui
# 
# Author:     Hou ShaoHui <houshao55@gmail.com>
# Maintainer: Hou ShaoHui <houshao55@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from dtalk.dispatch import Signal

blink_trayicon = Signal(providing_args=['icon'])
still_trayicon = Signal(providing_args=[])
unreaded_message = Signal(providing_args=['jid', 'msg'])
show_message = Signal(providing_args=['jid', 'loaded'])
raise_window = Signal(providing_args=[])
roster_request_add = Signal(providing_args=[])
open_add_friend_dialog = Signal(providing_args=['friend'])
