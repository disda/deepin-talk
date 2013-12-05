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


# DON'T DELETE BELOW CODE!
# Calls XInitThreads() as part of the QApplication construction in order to make Xlib calls thread-safe. 
# This attribute must be set before QApplication is constructed.
# Otherwise, you will got error:
#     "python: ../../src/xcb_conn.c:180: write_vec: Assertion `!c->out.queue_len' failed."
# 
# Qt5 application hitting the race condition when resize and move controlling for a frameless window.
# Race condition happened while Qt was using xcb to read event and request window position movements from two threads. 
# Same time rendering thread was drawing scene with opengl. 
# Opengl driver (mesa) is using Xlib for buffer management. Result is assert failure in libxcb in different threads. 
# 
import os
from PyQt5 import QtCore
if os.name == 'posix':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_X11InitThreads, True) 

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtWidgets, QtGui, QtQuick
from dtalk.utils.xdg import get_qml
from dtalk.controls.managers import ModelManager, ServerManager

class Panel(QtQuick.QQuickView):
    
    hideOtherWindow = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Panel, self).__init__()
        self.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)
        surface_format = QtGui.QSurfaceFormat()
        surface_format.setAlphaBufferSize(8)
        QtWidgets.qApp.focusWindowChanged.connect(self.onFocusWindowChanged)
        self.setColor(QtGui.QColor(0, 0, 0, 0))
        self.setFormat(surface_format)
        self.setFlags(QtCore.Qt.FramelessWindowHint)
        self.set_all_contexts()
        self.setSource(QtCore.QUrl.fromLocalFile(get_qml('Main.qml')))
        
    def set_all_contexts(self):    
        self.root_context = self.rootContext()        
        self.modelManager = ModelManager()
        self.serverManager = ServerManager()
        self.root_context.setContextProperty("modelManager", self.modelManager)
        self.root_context.setContextProperty("serverManager", self.serverManager)
        self.root_context.setContextProperty("windowView", self)        
        
    def onFocusWindowChanged(self, focusWindow):    
        if focusWindow.__class__.__name__ != "QQuickWindow":
            self.hideOtherWindow.emit()
    
    @QtCore.pyqtSlot(result="QVariant")
    def getCursorPos(self):
        return QtGui.QCursor.pos()
        
