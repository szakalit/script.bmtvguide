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
    return super(KeyListener, cls).__new__(cls, 'DialogSetKey.xml', ADDON.getAddonInfo('path'), ADDON.getSetting('Skin'), "720p")
  
  def onInit(self):
    try:
      self.getControl(2).addLabel("Nacisnij klawisz aby zapisac ")
    except:
      self.getControl(2).setLabel("Nacisnij klawisz aby zapisac ")

  def onAction(self, action):
    if action.getId() == 107:
       return
    else:
       self.key = action.getId()
       self.close()

if __name__ == '__main__':
    dialog = KeyListener()
    dialog.doModal()
    key = dialog.key
    del dialog
    ADDON.setSetting(id="info_key", value=str(key))




