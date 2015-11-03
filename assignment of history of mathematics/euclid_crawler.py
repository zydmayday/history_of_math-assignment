import requests
import bs4
import re
import urllib2
from mechanize import Browser

url = 'http://aleph0.clarku.edu/~djoyce/elements/bookI/'

all_props_url = [["propI1.html","I.1"],["propI2.html","I.2"],["propI3.html","I.3"],["propI4.html","I.4"],["propI5.html","I.5"],["propI6.html","I.6"],["propI7.html","I.7"],["propI8.html","I.8"],["propI9.html","I.9"],["propI10.html","I.10"],["propI11.html","I.11"],["propI12.html","I.12"],["propI13.html","I.13"],["propI14.html","I.14"],["propI15.html","I.15"],["propI16.html","I.16"],["propI17.html","I.17"],["propI18.html","I.18"],["propI19.html","I.19"],["propI20.html","I.20"],["propI21.html","I.21"],["propI22.html","I.22"],["propI23.html","I.23"],["propI24.html","I.24"],["propI25.html","I.25"],["propI26.html","I.26"],["propI27.html","I.27"],["propI28.html","I.28"],["propI29.html","I.29"],["propI30.html","I.30"],["propI31.html","I.31"],["propI32.html","I.32"],["propI33.html","I.33"],["propI34.html","I.34"],["propI35.html","I.35"],["propI36.html","I.36"],["propI37.html","I.37"],["propI38.html","I.38"],["propI39.html","I.39"],["propI40.html","I.40"],["propI41.html","I.41"],["propI42.html","I.42"],["propI43.html","I.43"],["propI44.html","I.44"],["propI45.html","I.45"],["propI46.html","I.46"],["propI47.html","I.47"],["propI48.html","I.48"]]


def get_proposition_name(body):
	return body.find('h1').text

def get_related_threoms(body):
	# post_name = get_proposition_name(body)
	theorem_dict = {"defs": [], "posts": [], "cns": [], "props": []}
	theorems = body.find_all('div', {'class' : 'just'})
	for theorem in theorems:
		all_a = theorem.find_all('a')
		for a in all_a:
			txt = a.text
			if 'Post' in txt and txt not in theorem_dict['posts']:
					theorem_dict['posts'].append(txt)
			elif 'Def' in txt and txt not in theorem_dict['defs']:
				theorem_dict['defs'].append(txt)
			elif 'C.N' in txt and txt not in theorem_dict['cns']:
				theorem_dict['cns'].append(txt)
			elif re.search(r'I\.\d', txt) and txt not in theorem_dict['props']:
				theorem_dict['props'].append(txt)
	return theorem_dict

def get_page(url):
	""" loads a webpage into a string """
	src = ''

	req = urllib2.Request(url)

	try:
		response = urllib2.urlopen(req)
		chunk = True
		while chunk:
			chunk = response.read(1024)
			src += chunk
		response.close()
	except IOError:
		print 'can\'t open',url 
		return src

	return src

# response = requests.get('http://aleph0.clarku.edu/~djoyce/elements/bookI/propI2.html')
# print response.text
# response = requests.get('http://aleph0.clarku.edu/~djoyce/elements/bookI/propI3.html')
# print response.text

all_props = {}

for x in all_props_url:
	this_url = url + x[0]
	br = Browser()
	response =br.open(this_url)
	html = response.read()
	soup = bs4.BeautifulSoup(html, 'html.parser')
	all_props[x[1]] = get_related_threoms(soup)

print all_props

