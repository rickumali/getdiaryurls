getdiaryurls
============

This is a small Python hack which traverses a whole directory full of
date-stamped text files, and retrieves all the URLs from those files. It
then writes the URLs into a bookmark file.

There's a lot more refinement that this program could use, but for now
it works for me.

## Usage

This programs assumes that you have a directory full of files with the
filename pattern of YYYYMMDD.txt. Call the program using:

```
python getdiaryurls.py subdirectory > bookmarks.html
```

Then import the bookmarks.html file into your favorite browser. It will
create a bunch of bookmark subdirectories like:

```
YEAR 2018
  MONTH 01 
    DAY 01
    DAY 02
      http://www.site_a.com/
      http://www.site_b.com/
      ...
```

