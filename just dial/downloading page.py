import requests
from bs4 import BeautifulSoup as bs
from contact_number import contact_number
from company_address import address,name
import json

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
domain = 'https://www.justdial.com'
city = 'Indore'
category = 'Fast-Food'
surl = domain+'/'+city+'/'+category+'/page-'
stop = 0
pageno = 0

while stop != 1:
    pageno = pageno+1
    url = surl+str(pageno)
    print(url)
    page = requests.get(url, headers=agent)
    if page.status_code == 200:
        soup = bs(page.content, 'html.parser')
        html_code = soup.prettify()
        all_companies = soup.findAll('div', attrs={"class": " col-sm-5 col-xs-8 store-details sp-detail paddingR0"})
        all_companies_list = []
        for company in all_companies:
                all_companies_list.append(company)

                company_name = company.select('h2 span a span')
                final_name = name(company_name).encode("utf-8")

                company_address = company.findAll('span', {'class': 'cont_fl_addr'})
                final_address = address(company_address).encode("utf-8")

                company_number = company.findAll('span', {'class': 'mobilesv'})
                final_number = contact_number(company_number).encode("utf-8")

                json_data = '''{"name": "'''+str(final_name)+'''", "address": "'''+str(final_address)+'''", "number": "'''+str(final_number)+'''"},\n'''
                # print(json.loads(str(json_data)))
                with open('people.json', 'a') as writeFile:
                    writeFile.write(json_data)
                writeFile.close()
    else:
        stop = 1
        print('ERROR: '+'page.status_code')
