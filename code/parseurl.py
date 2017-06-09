import re, os, lxml.html,  urllib.parse, urllib.request

poemNum = 0
lineNum = 0
wordNum = 0

def getLinks(html):
	'''
	with open(html, 'r', encoding='utf-8') as f:
		links = []
		poem = f.read()
		tree = lxml.html.fromstring(poem)
		atags = tree.xpath('.//div[@class="contents"]/ul[@class="contents"]//a')#[0].get('href')
		for a in atags:
			links.append(a.get('href'))
		print(links)
		return links
	'''
	links = []
	tree = lxml.html.fromstring(html)
	atags = tree.xpath('.//div[@class="contents"]/ul[@class="contents"]//a')#[0].get('href')
	for a in atags:
		links.append(domain + a.get('href'))
	#print(links)
	return links

	

	
def getNextPage(html):
	tree = lxml.html.fromstring(html)
	global w
	w.write(tree.xpath('.//div[@class="navpanel"]//td[@class="left"]//a/text()')[0])
	if tree.xpath('.//div[@class="navpanel"]//td[@class="left"]//a/text()')[0] == "صفحه‌ی بعد":
		print('check')
		nextPageUrl = tree.xpath('.//div[@class="navpanel"]//td[@class="left"]//a')[0].get('href')
		return domain + nextPageUrl
	return False
	#for a in atags:
	#	links.append(domain + a.get('href'))
		
		


def parseURL(url):
	query = urllib.parse.urlparse(url, scheme='', allow_fragments=True).query

	#page=view&mod=classicpoems&obj=home&id=0
	dic = {parameter.split('=')[0] : parameter.split('=')[1] for parameter in query.split('&')}
		
	return dic['obj'], dic['id']


	
def getPoem(html):
	'''
	with open(html, 'r', encoding='utf-8') as f:
		poem = f.read()
		tree = lxml.html.fromstring(poem)
		title = tree.xpath('.//div[@class="title"]//text()')[0]
		verses = tree.xpath('.//div[@class="poem"]//span[@class="verse"]/text()')
		return title, verses
	'''
	tree = lxml.html.fromstring(html)
	title = tree.xpath('.//div[@class="title"]//text()')[0]
	verses = tree.xpath('.//div[@class="poem"]//span[@class="verse"]/text()')
	return title, verses


def openLink(url):
    req = urllib.request.Request(url, data=None, headers={'User-Agent':
                                                         'Mozilla/5.0 (Windows NT 6.3; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36'})

    f = urllib.request.urlopen(req)
    if f.getcode() == 200:
        html = f.read()#.decode('utf-8')
        return html
    else:
        print(url)
        return False
		

def goThrough(myurl):

	global poemNum
	global lineNum
	global wordNum

	#corpus = ''.join((path, 'corpus.txt'))
	#w = open(corpus, 'w', encoding='utf-8')
	newLinks = []
	newLinks.append(myurl)
	#counter = 100
	while newLinks:# and counter:
    
		url = newLinks[0]
		newLinks = newLinks[1:]
		type, id = parseURL(url)
		html = openLink(url)
		if type == 'poem':
			page = 1
			
			title, verses  = getPoem(html)
			#writePoem(title, verses, id)
			poemNum += 1
			if poemNum % 100 == 0:
				print(poemNum)
			for verse in verses:
				w.write(verse)
				lineNum += 1
				w.write('\n')
				wordNum += len(verse.split())
			
			# get next page of the same poem
			nextPageUrl = getNextPage(html)
			while nextPageUrl:
				page += 1
				html = openLink(nextPageUrl)
				title, verses  = getPoem(html)
				for verse in verses:
					w.write(verse)
					lineNum += 1
					w.write('\n')
					wordNum += len(verse.split())
				nextPageUrl = getNextPage(html)
			
		else: 
			newLinks =  getLinks(html) + newLinks
		#counter -= 1
	w.close()

		
def writePoem(title, verses, id):
	
	
	path = ''
	
	name = ''.join((path, id, '.txt'))
	
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	
	with open(name, 'w', encoding='utf-8') as f:
		f.write(title+'\n')
		for num, verse in enumerate(verses, start=1):
			f.write(verse)
			if num%2 != 0:
				f.write('\n')
			else:
				f.write('\t')

				
	
    
				
'''
def getMeta(html):

	links = []
	pathname = tree.xpath('.//div[@class="header_title"]//span[@itemprop="title"]/text()')
	atags = tree.xpath('.//div[@class="header_title"]//a[@itemprop="url"]')
	for a in atags:
		link = a.get('href')
		type, id = parseURL(link)
		links.append((type, id))

	path = parseURL()
	meta = list(zip(links, pathname))
	
	type, id, farsiname
	id	part	part	book	poet
	
	poem_id	metaentry[0]
	
	path = '.'
	if type not 'home':
		path += 
'''


#url = "http://rira.ir/?page=view&mod=classicpoems&obj=home&id=0"
#url = "http://rira.ir/?page=view&mod=classicpoems&obj=poem&id=11571"
#url = "http://rira.ir/?page=view&mod=classicpoems&obj=part&id=22"
#url = "http://rira.ir/?page=view&mod=classicpoems&obj=poet&id=4"
#path = 'poem1.html'
#path2 = r'C:\Users\TK_adm\Documents\HSE\comp_ling_progr\iranica\collect\links.html'
#path3 = r'C:\Users\TK_adm\Documents\HSE\comp_ling_progr\iranica\collect\poet.html'

#writePoem(url):
'''
type, id = parseURL(url)
if type == 'poem':
	title, verses = getPoem(path)
	name = ''.join((id, '.txt'))
	with open(name, 'w', encoding='utf-8') as f:
		f.write(title+'\n')
		for num, verse in enumerate(verses, start=1):
			f.write(verse)
			if num%2!=0:
				f.write('\n')
			else:
				f.write('\t')
elif type == 'part':
	getLinks(path2)
elif type == 'poet':
	getLinks(path3)
'''

path = r"C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\collect\\poems\\"
domain = "http://rira.ir/"
# normal url
#myurl = "http://rira.ir/?page=view&mod=classicpoems&obj=home&id=0"

#to test
myurl = "http://rira.ir/?page=view&mod=classicpoems&obj=part&id=2"
corpus = ''.join((path, 'corpus.txt'))
w = open(corpus, 'w', encoding='utf-8')

goThrough(myurl)

print(poemNum)
print(lineNum)
print(wordNum)
#url = "http://rira.ir/?page=view&mod=classicpoems&obj=home&id=0"	

#url = "http://rira.ir/?page=view&mod=classicpoems&obj=poem&id=11571"
#url = "http://rira.ir/?page=view&mod=classicpoems&obj=poet&id=4"
#url = "http://rira.ir/?page=view&mod=classicpoems&obj=part&id=22"
#url = "http://rira.ir/?page=view&mod=classicpoems&obj=book&id=50"

#print(parseURL(url))



