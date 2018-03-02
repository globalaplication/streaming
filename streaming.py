#!/usr/bin/env python
import urllib
class Tv(object):
    def __init__(self, channel):
        if channel == "TV8":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/24/8/tv8"
        if channel == "D":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/94/0/kanal-d"
        if channel == "CNN":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/20/1/cnn-turk" 
        if channel == "STAR":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/90/2/star-tv"
        if channel == "SHOW":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/92/3/show-tv"
        if channel == "ATV":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/83/4/atv"      
        if channel == "TRT1":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/15/5/trt-1" 
        if channel == "FOX":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/87/7/fox" 
        if channel == "360":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/30/9/360" 
        if channel == "BLOOMBERG":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/295/10/bloomberg-ht"      
        if channel == "AHABER":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/365/11/a-haber" 
        if channel == "KANAL7":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/95/12/kanal-7" 
        if channel == "24TV":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/105/13/24-tv" 
        if channel == "HABERTURK":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/22/14/haberturk" 
        if channel == "BEYAZTV":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/321/16/beyaz-tv"   
        if channel == "TEVE2":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/132/33/teve2"   
        if channel == "NTVSPOR":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/127/27/ntv-spor" 
        if channel == "SPORTSTV":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/329/30/sports-tv" 
        if channel == "TRT3SPOR":
            channel = "http://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/17/26/trt-3---spor" 
        self.arraystreaming = []
        socket = urllib.urlopen(channel)
        self.source = socket.readlines()
    def gettag(self, source):
        start = source.find('"')+ len('"')
        end = source.find('"', start)
        return source[start:end]
    def TurkishChr(self, string):
        TrkChr = {"&#252;":"ü", "&#199;":"Ç", "&#231;":"ç", "&#214;":"Ö", "&#246;":"ö",
            "&#220;":"Ü", "&#39;":"'"
        }
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
                
get = Tv("TV8")
for get in get.streaming():
    print get["Time"], get["Title"]
