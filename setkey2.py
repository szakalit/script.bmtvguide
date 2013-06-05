#
#      Copyright (C) 2013 Szakalit
#      
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
import datetime
import os
import xbmc
import xbmcgui
import source as src
import ConfigParser
from strings import *
import datetime
import threading
import time
import ConfigParser

import xbmc
from xbmcgui import Dialog, WindowXMLDialog

import source as src
from notification import Notification
from strings import *
import re, sys, os
import streaming

class KeyListener(WindowXMLDialog):

  def __new__(cls):
    return super(KeyListener, cls).__new__(cls, 'DialogSetKey2.xml', ADDON.getAddonInfo('path'), ADDON.getSetting('Skin'), "720p")
  
  def onInit(self):
    self.key = 0
    self.a_info = 0
    self.a_stop = 0
    self.a_pp = 0
    self.a_pm = 0
    pass

  def onAction(self, action):
       self.getControl(7001).setLabel(str(action.getId()))
       self.getControl(7002).setLabel(str(action.getButtonCode()))
       self.getControl(7003).setLabel(str(action.getAmount1()))
       self.getControl(7004).setLabel(str(action.getAmount2()))

       self.getControl(7001).setAnimations([('Conditional', 'effect=fade start=0 end=100 time=1000 condition=False pulse=True')])
       self.getControl(8001).setAnimations([('Conditional', 'effect=fade start=0 end=100 time=1000 condition=False pulse=True')])
       self.getControl(9001).setAnimations([('Conditional', 'effect=fade start=0 end=100 time=1000 condition=False pulse=True')])



  def onClick(self, controlId):
        if controlId == 9001:
            self.getControl(7001).setAnimations([('Conditional', 'effect=fade start=0 end=100 time=1000 condition=True pulse=True')])
            self.getControl(8001).setAnimations([('Conditional', 'effect=fade start=0 end=100 time=1000 condition=True pulse=True')])
            self.getControl(9001).setAnimations([('Conditional', 'effect=fade start=0 end=100 time=1000 condition=True pulse=True')])
        if controlId == 9099:
            self.close()


if __name__ == '__main__':
    dialog = KeyListener()
    dialog.doModal()
    del dialog





