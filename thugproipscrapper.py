import urllib
from bs4 import BeautifulSoup

url = 'http://x.bobzent.info/osstatusget.php?game=thugpro'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

for tags in soup.find_all(['h4', 'h6',]):
    print(tags.get_text())




