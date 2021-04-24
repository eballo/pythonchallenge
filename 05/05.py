# http://www.pythonchallenge.com/pc/def/peak.html

# <peakhell src="banner.p"/>
# <!-- peak hell sounds familiar ? -->
from urllib.request import urlopen
import pickle

raw_banner = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
# print(raw_banner.read().decode())

banner_data = pickle.load(raw_banner)
print(banner_data)

# value = banner_data[0]
# k,v = value[0]
# print(k * v)

for line in banner_data:
    print("".join([k * v for k, v in line]))
