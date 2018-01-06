#Extracts the zip file data
import glob
import os
import csv
import zipfile
import io
   
path = '/media/sandeep/2Tb/sandeep/Research/Database-BenchMarking/Download_data/*.zip'   
files=glob.glob(path)   
for file in files:     
 #print(file)
 zip = zipfile.ZipFile(file)
 name = file.split('.zip')
 name = name[0].split('Download_data/')
 StrFile=str(zip.read(name[1]),'utf-8')
 data = io.StringIO(StrFile)
 reader = csv.reader(data,delimiter='\t')

#format of Data is:
#
 for row in reader:
  print(row)
 break
