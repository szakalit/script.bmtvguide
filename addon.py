import gui
import urllib, urllib2
import re, sys, os
import xbmcaddon, xbmcgui, xbmcplugin, xbmc
from strings import *

import main

class Start:
    def __init__(self):
		self.Run()
		
    def Play(self, cid):
		run = main.InitPlayer()
		run.LoadVideoLink(cid)


    def Run(self):
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
				pass
        elif service == "weebtv":
            self.Play(cid)



init = Start()
ADDON.setSetting(id="off", value='True')


