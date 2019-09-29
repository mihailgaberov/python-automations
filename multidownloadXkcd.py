#! python3

# multidownloadXkcd.py - Downloads XKCD comics using multiple threads. 

import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok = True) 

# store comics in ./ xkcd 
def downloadXkcd(startComic, endComic): 
  for urlNumber in range(startComic, endComic): 
  # Download the page. 
  print('Downloading page http://xkcd.com/%s...' % (urlNumber)) 
  res = requests.get('http://xkcd.com/%s' % (urlNumber)) 
  res.raise_for_status()