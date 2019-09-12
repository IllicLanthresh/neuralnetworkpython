import requests as re
from lxml import html

baseurl = "http://neuralnetworksanddeeplearning.com/"
page = html.fromstring(re.get(baseurl).content)

for a in page.xpath('//*[@id="toc"]/p[@class="toc_title"]/a[not(@id)] | //*[@id="toc"]/p[@class="toc_not_mainchapter"]/a[not(@id)] | //*[@id="toc"]/p[@class="toc_mainchapter"]/a[not(@id)]'):
    print(baseurl + a.get("href") + " - " + a.text)
