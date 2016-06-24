#! python3
# lucky.py - Opens several Google search results

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:])) #Downloads the search page
res.raise_for_status() #Checks for validity

#Retrieve top search result links
soup = bs4.BeautifulSoup(res.text,"html.parser")

#Opens browser tab for each result
linkElems = soup.select('.r a') #Finding all <a> class elements that have r CSS class
numOpen = min(5, len(linkElems)) #Opens first 5 results or how many is in there
for i in range(numOpen):
	webbrowser.open('http://google.com'+linkElems[i].get('href'))
	