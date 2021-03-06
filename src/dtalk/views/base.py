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

from PyQt5 import QtGui, QtQuick, QtCore, QtWidgets
        
class BaseView(QtQuick.QQuickView):
    
    def __init__(self, parent=None):
        super(BaseView, self).__init__(parent)
        self.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)
        surface_format = QtGui.QSurfaceFormat()
        surface_format.setAlphaBufferSize(8)
        self.setColor(QtGui.QColor(0, 0, 0, 0))
        self.setFormat(surface_format)
        self.setFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.Window)
        self.root_context = self.rootContext()        
        self.setContextProperty("windowView", self)        
        
    setContextProperty = property(lambda self: self.root_context.setContextProperty)    
    
    @QtCore.pyqtSlot(result="QVariant")
    def getCursorPos(self):
        return QtGui.QCursor.pos()
    
    @QtCore.pyqtSlot()
    def doMinimized(self):
        self.showMinimized()
        
    def showCenter(self):    
        screenSize = QtWidgets.QApplication.desktop().geometry().size()
        x = (screenSize.width() - self.width()) / 2
        y = (screenSize.height() - self.height()) /2
        self.setPosition(x, y)
        self.show()
        
    def showRightSide(self):    
        screenSize = QtWidgets.QApplication.desktop().geometry().size()
        x = screenSize.width() - self.width() - 80
        y = (screenSize.height() - self.height()) /2
        self.setPosition(x, y)
        self.show()
        
    def showIt(self):    
        self.showCenter()
        self.requestActivate()

