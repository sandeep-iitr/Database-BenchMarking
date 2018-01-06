# importing the requests library
import requests
import sys


import os
import shutil

global dump

def download_file(url):
    global dump
    #url = "http://randomsite.com/file.gz"
    file = requests.get(url, stream=True)
    dump = file.raw

def save_file(name):
    global dump
    location = os.path.abspath("/media/sandeep/2Tb/sandeep/Research/Database-BenchMarking/Download_data/data-GDELT/"+name)
    with open(name, 'wb') as location:
        shutil.copyfileobj(dump, location)
    del dump


# api-endpoint
URL = "http://data.gdeltproject.org/gdeltv2/masterfilelist.txt"
 
# sending get request and saving the response as response object
r = requests.get(url = URL)
 
# extracting data in json format
#print(r.text)
for line in r.iter_lines():
 #print(line)
 try:
  size,has,link = str(line,'utf-8').split(" ")
  if 'export' in link:
   #print(link)
   download_file(link)
   name=link.split('gdeltv2/')
   save_file(name[1])
   #break
 except:
    #print("Error:", sys.exc_info()[0])
    #print(line)
    continue
