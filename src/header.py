
import urllib2
import sys
import os  
import pymongo

host = "127.0.0.1"
port = 27017

def getServerStatus():
    c = pymongo.MongoClient(host, port)
    return c.admin.command('serverStatus', workingSet=True)
