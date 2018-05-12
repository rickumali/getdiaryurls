#
# python lister.py
#
import sys
from os import listdir
from re import compile
from geturls import FileURLs
from nestedhtml import NestedHTML

if len(sys.argv) != 2:
	print "Need path to directory of diary entries"
	sys.exit(1)

diary_dir = sys.argv[1]
ary = listdir(diary_dir)
ary.sort()

year_buckets = {}

for filename in ary:
	f = FileURLs(diary_dir + "/" + filename)
	if len(f.urls()) > 0:
		date, ext = filename.split('.')
		if len(date) != 8:
			print "Problem: %s" % filename
			next
		datefmt = compile('(?P<year>[1-2][0-9][0-9][0-9])(?P<month>[0-9][0-9])(?P<day>[0-9][0-9])')
		year = datefmt.search(date).group('year')
		month = datefmt.search(date).group('month')
		day = datefmt.search(date).group('day')
		if year not in year_buckets:
			year_buckets[year] = {}
		if month not in year_buckets[year]:
			year_buckets[year][month] = {}
		if day not in year_buckets[year][month]:
			year_buckets[year][month][day] = f.urls()

o = NestedHTML(year_buckets)
o.dump_html()
