#CALVARY SOUTHAMPTON ITUNES PODCAST - xml writer


# Installations: pip install beautifulsoup4
#Mac/Linux: sudo apt-get install python-qt4

import bs4 as bs        #beautifulsoup4 for web scraping
import urllib.request   #for web scraping
import os
import ftplib
import time
from tkinter import *
root = Tk()

#clear terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

def get_podcast_xml():
	# Getting Information from pod1.xml : 
	xml_feed1 = 'http://www.southamptonchurch.co.uk/pod1.xml'
	sauce1 = urllib.request.urlopen(xml_feed1).read()
	soup1 = bs.BeautifulSoup(sauce1,'xml')
	pod1 = soup1.find_all('item') #storing all <item> (s) in the variable called "pod1"
	pod1 = str(pod1) #converting beautifulsoup object into a string

	label = Label(root, text = "Step 1/5 Complete - Information collected from previous pod1.xml").grid(row=2,column=1,sticky=W)

	# Getting the latest sermon from faithlife 
	xml_feed2 = 'https://sermons.faithlife.com/api/channels/7663604/feed'
	sauce2= urllib.request.urlopen(xml_feed2).read()
	soup2 = bs.BeautifulSoup(sauce2,'xml')
	faithlife = soup2.find('item') #storing first <item> as "faithlife"
	faithlife = str(faithlife) #converting beautifulsoup object into a string
	time.sleep(1)
	label = Label(root, text = "Step 2/5 Complete - Information collected from faithlife").grid(row=3,column=1,sticky=W)

	# CREATING THE XML FILE:
	created_name = '\pod1.xml' 


	if os.name == 'nt':
		desktop = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
		query_if_windows = "windows"
	else:
		desktop = str(os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop'))
		query_if_windows = "not windows"

	filename = desktop + created_name
	# filename = 'C:/Users/Olive/Desktop/' + created_name
	time.sleep(1)
	label = Label(root, text = "Step 3/5 Complete - Identified if windows or non windows").grid(row=4,column=1,sticky=W)

	text_file = open(filename,"w")

	# Writing the top section of the xml file (doesn't change):
	text_file.write('<rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" version="2.0">\n')
	text_file.write('<channel>\n')
	text_file.write('<title>Calvary Chapel Southampton</title>\n')
	text_file.write('<description>')
	text_file.write('Bible study, sermons and preaching, verse by verse with Calvary Chapel Southampton.\n')
	text_file.write('</description>\n')
	text_file.write('<link>http://www.calvarysoton.co.uk</link>\n')
	text_file.write('<category>Christianity</category>\n')
	text_file.write('<copyright>2019 Calvary Chapel Southampton</copyright>\n')
	text_file.write('<docs>http://blogs.law.harvard.edu/tech/rss</docs>\n')
	text_file.write('<language>en-gb</language>\n')
	text_file.write('<lastBuildDate>Sun, 20 Jan 2019 09:08:02 +0100</lastBuildDate>\n')
	text_file.write('<managingEditor>admin@calvarysoton.co.uk (Calvary Southampton)</managingEditor>\n')
	text_file.write('<pubDate>Sun, 20 Jan 2019 09:08:00 +0100</pubDate>\n')
	text_file.write('<generator>\n')
	text_file.write('FeedForAll Mac v2.1 (2.1.0.1) unlicensed version; http://www.FeedForAll.com/\n')
	text_file.write('</generator>\n')
	text_file.write('<itunes:subtitle>\n')
	text_file.write('Bible Study and Sermons from Calvary Chapel Southampton\n')
	text_file.write('</itunes:subtitle>\n')
	text_file.write('<itunes:summary>\n')
	text_file.write('Verse by Verse Bible Studies from Calvary Chapel Southampton Morning Service. Archived sermons from guest speakers available at www.calvarysoton.co.uk/\n')
	text_file.write('</itunes:summary>\n')
	text_file.write('<itunes:category text="Religion &amp; Spirituality">\n')
	text_file.write('<itunes:category text="Christianity"/>\n')
	text_file.write('</itunes:category>\n')
	text_file.write('<itunes:category text="Religion &amp; Spirituality">\n')
	text_file.write('<itunes:category text="Other"/>\n')
	text_file.write('</itunes:category>\n')
	text_file.write('<itunes:category text="Religion &amp; Spirituality">\n')
	text_file.write('<itunes:category text="Spirituality"/>\n')
	text_file.write('</itunes:category>\n')
	text_file.write('<itunes:keywords>\n')
	text_file.write('Bible, bible study, sermon, calvary chapel, gospel, preaching, teach, england, southampton church, Simon Lawrenson, UK,\n')
	text_file.write('</itunes:keywords>\n')
	text_file.write('<itunes:author>Calvary Southampton</itunes:author>\n')
	text_file.write('<itunes:owner>\n')
	text_file.write('<itunes:email>mail@calvarychapelsouthampton.co.uk</itunes:email>\n')
	text_file.write('<itunes:name>Calvary Chapel Southampton</itunes:name>\n')
	text_file.write('</itunes:owner>')
	text_file.write('<itunes:image href="http://www.southamptonchurch.co.uk/images/ccpodcast_2014.jpg"/>\n')
	text_file.write('<itunes:explicit>no</itunes:explicit>\n')
	text_file.write('<image>\n')
	text_file.write('<url>\n')
	text_file.write('http://www.southamptonchurch.co.uk/images/ccpodcast_2014.jpg\n')
	text_file.write('</url>\n')
	text_file.write('<title>Calvary Southampton</title>\n')
	text_file.write('<link>http://www.calvarysoton.co.uk</link>\n')
	text_file.write('<description>Firmly Planted Bible Study Podcast</description>\n')
	text_file.write('<width>144</width>\n')
	text_file.write('<height>300</height>\n')
	text_file.write('</image>\n')

	text_file.write("\n")
	text_file.write("\n")
	text_file.write("\n")

	text_file.write(faithlife) #writing in the <item> contents of faithlife xml feed 

	text_file.write("\n")
	text_file.write("\n")
	text_file.write("\n")

	text_file.write(pod1) #writing in the <item> contents of pod1.xml (archive xml)

	text_file.write('</channel>\n')
	text_file.write('</rss>\n')

	text_file.close()
	time.sleep(1)
	label = Label(root, text = "Step 4/5 Complete - new pod1 xml file written to desktop").grid(row=5,column=1,sticky=W)

	# Uploading to server
	ftp = ftplib.FTP('home680705515.1and1-data.host')  
	ftp.login('u89215005-ollie','N0rw1chc1ty!')        #ollie's credentials, created by Simon
	ftp.cwd('/studies') 
	myfile = open(filename,'rb')
	ftp.storbinary('STOR ' + 'pod1.xml', myfile) #previously used 'storlines', but had a maximum line size of 8192. stbordinary reads and stores in binary 
	ftp.quit

	time.sleep(5)
	label = Label(root, text = "Step 5/5 Complete - uploaded to southamptonchurch.co.uk server").grid(row=6,column=1,sticky=W)

label = Label(root, text="Two requirements before this program is run: 1. The latets sermon is uploaded from proclaim 2. Internet Connection").grid(row=0,column=1,sticky=W)
Button(root,text="Run program to update pod1.xml and upload to server",command=get_podcast_xml).grid(row=1,column=1,sticky=W)
root.mainloop()