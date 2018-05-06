#
# geturls.py
#

import re

class FileURLs(object):

	def __init__(self, filename):
		self.filename = filename
		self.url_list = []
		f = open(filename)
		url_re = re.compile(r'https?://[^ ]*')
		for line in f:
			m = url_re.search(line.rstrip())
			if m:
				self.url_list.append(m.group())
			else:
				pass

	def urlcount(self):
		return len(self.url_list)

	def urls(self):
		return self.url_list

if __name__ == "__main__":
	from sys import argv

	if len(argv) != 2:
		print "Need filename!"
		exit(1)
	
	f = FileURLs(argv[1])
	print f.urlcount()
	print f.urls()
