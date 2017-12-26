import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# looks very poorly formatted
soup = bs.BeautifulSoup(sauce, 'lxml') # 'html' coupd also be used
# formats the source code

# print(soup)
soup.title # Gives as a tag
soup.title.string # Gives a string
soup.title.text
soup.p # gives everything under first paragraph tag

soup.find_all('p') # gives all the <p> tags


for paragraph in soup.find_all('p'):
    (paragraph.string)

# We see a lot of NONE
# This is because .string returns None for tags which have any childrentags

for paragraph in soup.find_all('p'):
    paragraph.text # .text overcomes that problem

# Some websites don't have text under paragraph tags..

soup.get_text()
# print(soup.get_text())
# This will get all the text regardless of the tags

# Find all the links in a website
for url in soup.find_all('a'):
    # print(url) # Gives entire tag
    # print(url.text) # Gives the text portion of tag
    (url.get('href')) # This gives hyperlink


# Navigation bar
nav = soup.nav
# print(soup.nav) # Everything under the <NAV> comes

# Find URLs in NavBar
for url in nav.find_all('a'):
    (url.get('href'))


body = soup.body # access body
for paragraph in body.find_all('p'):
    (paragraph.text)


# Finding specific div
for div in soup.find_all('div', class_ = 'body'):
    (div.text)

# Parsing through Table:

table = soup.table
# soup.find('table')  # same as earlier command
# when using .find(), only first incidence returned
# with find_all(), every instance is returned

table_rows = table.find_all('tr')
# print(table_rows)
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    (row)

# First line is blank because it is <th>


############# Pandas Version of grabbing table ##############
import pandas as pd
df = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header = 0)
# print(df) # got the table only


# XML files - used mostly to have links, between tags | Site Maps
# Readingthe sitemap

sauce_xml =  urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml')
soup_xml = bs.BeautifulSoup(sauce_xml, 'xml')
# print(soup_xml)

for url in soup_xml.find_all('loc'): # url is in <loc>
    (url.text)



# Scrapping JS dynamic data
'''
 <p>Javascript (dynamic data) test:</p>
  <p class='jstest' id='yesnojs'>y u bad tho?</p>
  <script>
     document.getElementById('yesnojs').innerHTML = 'Look at you shinin!';
  </script>
'''
# Here 'y u bad' is written originally
# But when page opened, browser runs the script tag and displays something else

js_test = soup.find('p', class_ = 'jstest')
#   print(js_test) # Here, the entire <p>tag comes

# We didn't get the script, because we are not a client
# So, we need to mimic being a client
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebPage

class Client(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()
url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup_js = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('p', class_ = 'jstest')
print(js_test)
