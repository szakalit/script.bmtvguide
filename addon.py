import buggalo
import gui
import urllib, urllib2
import re, sys, os
import xbmcaddon, xbmcgui, xbmcplugin, xbmc
from strings import *

buggalo.SUBMIT_URL = ''


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
				buggalo.onExceptionRaised()
        elif service == "weebtv":
            self.Play(cid)


init = Start()


