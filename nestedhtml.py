#
# nestsedhtml.py
#

class NestedHTML(object):

	"""
	This assumes a dict with three leves
	YEAR -> MONTH -> DAY -> Array of URLs
	""" 
	def __init__(self, h):
		self.h = h

	def dump_html(self):
		print """<!DOCTYPE NETSCAPE-Bookmark-file-1>
    <TITLE>Bookmarks</TITLE>
    <H1>Bookmarks</H1>
    <DL>
"""
		for year in sorted(self.h):
			print """
    <DT><H3 FOLDED>YEAR %s</H3>
    <DL><P>
""" % year
			month_buckets = self.h[year]
			for month in sorted(month_buckets):
				print """
        <DT><H3 FOLDED>MONTH %s</H3>
        <DL>
""" % month
				for day in sorted(self.h[year][month]):
					print """
            <DT><H3 FOLDED>DAY %s</H3>
            <DL>
""" % day
					for link in self.h[year][month][day]:
						print """
                <DT><A HREF="%s">%s</A>
""" % (link,link)
					print """
            </DL>
"""
				print """
        </DL>
"""
			print """
    </DL>
"""
		print """
</HTML>
"""

	def dump_raw(self):
		for year in sorted(self.h):
			month_buckets = self.h[year]
			for month in sorted(month_buckets):
				print year, month, self.h[year][month]

	def dump_lastchar(self):
		for year in sorted(self.h):
			month_buckets = self.h[year]
			for month in sorted(month_buckets):
				day_buckets = self.h[year][month]
				for day in sorted(day_buckets):
					day_array = self.h[year][month][day]
					for url in day_array:
						print url[-1]
