from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('https://www.ncr.com/company/executive-leadership-team').text

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(source, 'lxml')
print(soup.pretify())

browser = mechanicalsoup.StatefulBrowser
soup_config={'features': 'lxml'},  # Use the lxml HTML parser
raise_on_404=True,
user_agent='MyBot/0.1: mysite.example.com/bot_info',

browser.open(url)
# ...
browser.close()
with open('simple.HTML') as HTML_file:
    soup = BeautifulSoup(HTML_file, 'lxml')
vp_name = soup.find('div', class_ = 'leadership-team_wrapper_cntr_leaders-grid_leader_info_designation')
print(vp_name)

import csv
from datetime import datetime

with open('index.csv') as csv_file:
    writer = csv.writer(csv)
    writer.writerow([name, position, datetime.now()])
