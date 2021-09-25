import re 
import urllib.request

warnings_uri= 'https://forecast.weather.gov/product.php?site=CRH&issuedby=AKQ&product=SMW&format=TXT'

with urllib.request.urlopen(warnings_uri) as source:
    warnings_text = source.read()

print(warnings_text[:80])

document = warnings_text.decode('utf-8')
print(document[:80])

title_pattern = re.compile(r'\<h3\>(.*?)\</h3\>')
print(title_pattern.search(document))