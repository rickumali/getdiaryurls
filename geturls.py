#
# geturls.py
#

import re

def has_bad_lastchar(s):
	if s[-1] == '.':
		return True
	if s[-1] == ')':
		return True
	if s[-1] == ',':
		return True
	if s[-1] == '\'':
		return True
	if s[-1] == ':':
		return True
	if s[-1] == '"':
		return True
	return False

class FileURLs(object):

	def __init__(self, filename):
		self.filename = filename
		self.url_list = []
		f = open(filename)
		url_re = re.compile(r'https?://[^ ]*')
		for line in f:
			m = url_re.search(line.rstrip())
			if m:
				u = m.group()
				while has_bad_lastchar(u):
					u = u[:-1] # Remove last character
				self.url_list.append(u)
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
