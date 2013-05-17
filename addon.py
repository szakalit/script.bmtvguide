#
#      Copyright (C) 2012 Tommy Winther
#      http://tommy.winther.nu
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
import buggalo
import gui
import urllib, urllib2
import re, sys, os
import xbmcaddon, xbmcgui, xbmcplugin, xbmc

buggalo.SUBMIT_URL = 'http://tommy.winther.nu/exception/submit.php'


__scriptname__ = "myvguide"
__scriptID__ = "script.bmtvguide"
__author__ = "myvguide"
__url__ = "myvguide"
__credits__ = ""
__addon__ = xbmcaddon.Addon(__scriptID__)


__language__ = __addon__.getLocalizedString
t = sys.modules[ "__main__" ].__language__

BASE_RESOURCE_PATH = os.path.join( __addon__.getAddonInfo('path'), "resources" )
sys.path.append( os.path.join( BASE_RESOURCE_PATH, "lib" ) )


import main

class Start:
    def __init__(self):
		self.showListOptions()
		
    def Play(self, cid):
		run = main.InitPlayer()
		run.LoadVideoLink(cid)


    def showListOptions(self):
        parser = main.UrlParser()
        params = parser.getParams()
        service = parser.getParam(params, "service")
        cid = parser.getParam(params, "cid")
        if service == None or service == '':
            try:
				w = gui.TVGuide()
				w.doModal()
				del w
            except Exception:
				buggalo.onExceptionRaised()
        elif service == "weebtv":
            self.Play(cid)


init = Start()


