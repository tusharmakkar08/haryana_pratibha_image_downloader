#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  download.py
#  
#  Copyright 2014 tusharmakkar08 <tusharmakkar08@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import urllib,os,time                              

def main():
	url = "http://haryana.gov.in/pratibha-samman/images/DSC_0"
	# Basic source of downloading
	for i in xrange(391,570):
		# Numbers in range is found by the hardcore method of trial and 
		# error
		suffix=str(i)+".jpg"
		url+=suffix
		uopen = urllib.urlopen(url)
		# For Opening Url
		stream = uopen.read()
		di=os.getcwd()+"/../haryana/"
		if not os.path.exists(di):
			os.makedirs(di)
		# Making of new directory if doesn't exists
		if os.path.exists(di+str(i-390)+".jpg"):
			continue
		# Download if and only if the photo not downloaded earlier
		file = open(di+str(i-390)+".jpg",'w')
		file.write(stream)
		# Writing stream to local system
		file.close()
		time.sleep(1)
		# Sleep because python is too fast to not be detected as an attack
		# on government site :P 
		url=url[:-7]
		print "Downloaded Image Number: "+str(i-390)
	time.sleep(1)
	return 0

if __name__ == '__main__':
	main()

