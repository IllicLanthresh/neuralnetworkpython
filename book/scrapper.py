import requests as re
from lxml import html

baseurl = "http://neuralnetworksanddeeplearning.com/"
page = re.get(baseurl)
parsed = html.fromstring(page.content)

for a in parsed.xpath('//*[@id="toc"]/p[@class="toc_title"]/a[not(@id)] | //*[@id="toc"]/p[@class="toc_not_mainchapter"]/a[not(@id)] | //*[@id="toc"]/p[@class="toc_mainchapter"]/a[not(@id)]'):
    print(a.text + " - " + baseurl + a.get("href"))
