import bs4 as bs
import urllib.request
from urllib.request import urlopen

def getPrice():
	sauce = urllib.request.urlopen('https://finance.yahoo.com/quote/INDIGO.NS?p=INDIGO.NS&.tsrc=fin-srch').read()
	soup = bs.BeautifulSoup(sauce,'lxml')
	price=soup.find('div',{"class":"My(6px) Pos(r) smartphone_Mt(6px)"}).find('span').text
	return price


while(True):
	print("The current price is : " + str(getPrice()))