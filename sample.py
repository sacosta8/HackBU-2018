import bs4 as bs
import urllib.request
import json

page = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
sauce = urllib.request.urlopen(page)
soup = bs.BeautifulSoup(sauce,"html.parser")
table = soup.find('table')
company_dictionary = {}
for row in table.findAll("tr"):
	cells = row.findAll("td")
	if(len(cells) == 8):
		abb = cells[0].find(text=True)
		name = cells[1].find(text=True)
		company_type = cells[3].find(text=True)
		company_headquarters = cells[5].find(text=True)
		company_dictionary[name] = [abb,company_type,company_headquarters]
values = [{"Company Name":k,"Company info":v} for k,v in company_dictionary.items()]
with open('data.txt', 'w') as outfile:
	json.dump(values,outfile,indent=4)
