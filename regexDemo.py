import re

# target
text = '<img src="//tva3.sinaimg.cn/mw600/0076BSS5ly8gz4y00due1j30u018z79r.jpg"'

re.findall(r'<img\ssrc="//tva3\.sinaimg\.(.)*\.jpg"', text)
