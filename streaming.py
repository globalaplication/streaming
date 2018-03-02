#!/usr/bin/env python
import urllib
class Tv(object):
    def __init__(self, channel):
        self.arraystreaming = []
        if channel == "Tv8":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/24/8/tv8"
        socket = urllib.urlopen(channel)
        self.source = socket.readlines()
    def gettag(self, source):
        start = source.find('"')+ len('"')
        end = source.find('"', start)
        return source[start:end]
    def TurkishChr(self, string):
        TrkChr = {"&#252;":"ü", "&#199;":"Ç", "&#231;":"ç", "&#214;":"Ö", "&#246;":"ö"}
        for test in TrkChr:
            string = string.replace(test, TrkChr[test])
        return string
    def streaming(self):
        for test in self.source:
            if test.find('padding-top: 80px') is not -1:
                start = test.find(">") + len(">")
                end = test.find("<", start)
                time = test[start:end]
            if test.find('img alt') is not -1:
                title = self.TurkishChr(self.gettag(test))
                if len(title) is not 0:
                    tag = test.find("src")
                    start = test.find('"', tag) +1
                    end = test.find('"', start)
                    picture = test[start:end]
                    self.arraystreaming.extend([{"Title":title,
                    "Time":time, 
                    "Picture":picture}])
        return self.arraystreaming
                
get = Tv("Tv8")
for get in get.streaming():
    print get["Time"], get["Title"]


