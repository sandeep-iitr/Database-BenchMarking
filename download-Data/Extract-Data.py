#Extracts the zip file data
import glob
import os
import csv
import zipfile
import io
   
path = '/media/sandeep/2Tb/sandeep/Research/Database-BenchMarking/Download_data/*.zip'   
DataFile=open('/media/sandeep/2Tb/sandeep/Research/Database-BenchMarking/Download_data/data-GDELT/LA_Data_Extracted.txt','w')#file to write Data to

files=glob.glob(path)   
for file in files: 
 try:    
  #print(file)
  zip = zipfile.ZipFile(file)
  name = file.split('.zip')
  name = name[0].split('Download_data/')
  StrFile=str(zip.read(name[1]),'utf-8')
  data = io.StringIO(StrFile)
  reader = csv.reader(data,delimiter='\t')



#format of Data is: in the file Schema-Gdelt.txt

#Extracting Events in Los Angeles
#SELECT * FROM `gdelt-bq.full.events` where  ActionGeo_Lat BETWEEN 33.83
#    AND 34.61 AND ActionGeo_Long BETWEEN -118.63 AND -116.87 
 
  for row in reader:
   #row 56 and row 57 containts ActionGeo_Lat and ActionGeo_Long
   if row[56] !='' and row[57] !='':
    lat=float(row[56])
    lng=float(row[57])
    #Events around Los Angeles
    if (33.83 <= lat <= 34.61) and (-118.63 <= lng <= -116.87):
     #print("lat: %f , lng: %f, Date :%s, Actor1Name :%s, Source: %s"%(lat,lng,row[59],row[6],row[60]))
     line=[row[0],str(lat),str(lng),row[59],row[6],row[60]]
     s1='\t'.join(line)
     DataFile.write(s1+"\n")
     print(line)
  #break
 except:
  continue
