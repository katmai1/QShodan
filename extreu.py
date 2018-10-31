from bs4 import BeautifulSoup

# <div class="search-result">
#<div class="ip"><a href="http://52.79.127.121:8081">52.79.127.121</a>
#</div>
#<div class="search-result-summary"><span>ec2-52-79-127-121.ap-northeast-2.compute.amazonaws.com</span><br/><a class="os" href="/search?query=dir-300+org%3A%22Amazon.com%22">Amazon.com</a>
#<div></div><span>Added on 2018-10-31 09:23:36 GMT</span><br/><img src="https://static.shodan.io/shodan/img/flags/16/KR.png" title="Korea, Republic of"/><a class="city" href="/search?query=dir-300+country%3A%22KR%22">Korea, Republic of</a>,
#<a class="city" href="/search?query=dir-300+city%3A%22Incheon%22">Incheon</a>
#<div class="clear"></div>
#<a class="details" href="/host/52.79.127.121">Details</a><br/><br/><span class="badge" style="color:white">cloud</span>
#</div>

class Extreu:
    
    def __init__(self,  raw_html):
        self.raw_html = raw_html
        self.bs = BeautifulSoup(raw_html,  "html5lib")
        self.results = self.bs.find_all("div", class_="search-result")
        self._raw_ips = self.bs.find_all("a",  class_="details") 
    
    @property
    def ips(self):
        lista = []
        for a in self._raw_ips:
            ip = a['href'].replace("/host/",  "")
            if self.validate_ip(ip):
                lista.append(ip)
        return lista
    
    def validate_ip(self,  ip):
        splited = ip.split('.')
        if len(splited) != 4:
            return False
        for x in splited:
            if not x.isdigit():
                return False
            i = int(x)
            if i < 0 or i > 255:
                return False
        return True
