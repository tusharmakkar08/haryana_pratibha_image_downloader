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
	for i in xrange(391,570):
		suffix=str(i)+".jpg"
		url+=suffix
		uopen = urllib.urlopen(url)
		stream = uopen.read()
		di=os.getcwd()+"/../haryana/"
		if not os.path.exists(di):
			os.makedirs(di)
		if os.path.exists(di+str(i-390)+".jpg"):
			continue
		file = open(di+str(i-390)+".jpg",'w')
		file.write(stream)
		file.close()
		time.sleep(1)
		url=url[:-7]
		print "Downloaded Image Number: "+str(i-390)
	return 0

if __name__ == '__main__':
	main()

