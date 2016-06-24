#! python3
#xkcd.py - Downloads every single xkcd comic

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd comic', exist_ok = True) #Makes folder in \xkcd comic

while not url.endswith('#'):
	print('Downloading page %s...' %url) #What url is being downloaded
	res=requests.get(url)
	res.raise_for_status()
	
	soup = bs4.BeautifulSoup(res.text,"html.parser")
	comicElem = soup.select('#comic img') #Selects the img element from comic class
	if comicElem == []:
		print('Could not find the comic image.')
	else:
		comicUrl = comicElem[0].get('src')
		
		print('Downloading image %s...' %(comicUrl))
		res = requests.get(comicUrl) #Downlaods img file
		res.raise_for_status
		imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
		for chunk in res.iter_content(1000000):
			imageFile.write(chunk)
			imageFile.close()
			
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com'+ prevLink.get('href')

print('Done')
