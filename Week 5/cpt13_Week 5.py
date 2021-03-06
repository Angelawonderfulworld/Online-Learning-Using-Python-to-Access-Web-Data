#Extracting Data from XML

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

#We provide two files for this assignment. 
#One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1024588.xml (Sum ends with 23)
#You do not need to save these files to your folder since your program will read the data directly from the URL. 
#Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('Enter - ')

html = urllib.request.urlopen(url).read().decode()
print('Retrieving', url)
print('Retrieved', len(html), 'characters')

total = 0
sum = 0

datatree = ET.fromstring(html)
tags = datatree.findall('comments/comment')

for tag in tags:
    total += 1
    sum += int(tag.find('count').text)

print('Count:', total)
print('Sum:', sum)
