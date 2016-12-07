from bs4 import BeautifulSoup
import urllib.request
import os, sys

username = str(sys.argv[1])
try:
	html = urllib.request.urlopen('https://github.com/{0}?tab=repositories'.format(username))
except:
	print('User not found!!!')
	sys.exit(0)
html = str(html.read())

soup = BeautifulSoup(html, 'html.parser')
repositories = soup.findAll('a', {'itemprop':'name codeRepository'})
if len(repositories)==0:
	print('User {0} has no repositories'.format(username))
	sys.exit(0)
	
for i in repositories:
	link = 'https://github.com'+i['href']
	os.system('git clone '+link)
# print(html.count('name codeRepository'))