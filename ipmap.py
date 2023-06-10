import urllib.request
from urllib.error import HTTPError
import json
import sys

class IPMap():
    def __init__(self):
      self.API_KEY = ''
      self.API_URL = f'https://api.ipgeolocation.io/ipgeo?apiKey={self.API_KEY}'
    
    def banner(self):
       print('''
                    _.-,=_"""--,_
                .-" =/7"   _  .3#"=.
              ,#7  " "  ,//)#d#######=.
            ,/ "      # ,i-/###########=
          /         _)#sm###=#=# #######\\
          /         (#/"_`;\//#=#\-#######\\
        /         ,d####-_.._.)##P########\\
        ,        ,"############\\##bi- `\| Y.
        |       .d##############b\##P'   V  |
        |\      '#################!",       |
        |C.       \###=############7        |
        '###.           )#########/         '
        \#(             \#######|         /
          \B             /#######7 /      /
          \             \######" /"     /
            `.            \###7'       ,'
              "-_          `"'      ,-'
                "-._           _.-"
                    """"---""""
             _   ___   _       __    ___  
            | | | |_) | |\/|  / /\  | |_) 
            |_| |_|   |_|  | /_/--\ |_| 
       ''')

    def resolve(self, ip: str):
        try:
          response = urllib.request.urlopen(self.API_URL + '&ip=' + ip)
          data = response.read().decode()
          json_data = json.loads(data)
          self.banner()
          print(f'''
            IP: {json_data['ip']}
            Country: {json_data['country_name']}
            State/Province: {json_data['state_prov']}
            Continent: {json_data['continent_name']}
            Country Code: {json_data['country_code2']}
            Country Capital: {json_data['country_capital']}
            City: {json_data['city']}
            Zipcode: {json_data['zipcode']}
            Latitude: {json_data['latitude']}
            Longitude: {json_data['longitude']}
            Calling Code: {json_data['calling_code']}
            Country TLD: {json_data['country_tld']}
            ISP: {json_data['isp']}
            Currency Name: {json_data['currency']['name']}
            Time Zone: {json_data['time_zone']['name']}
            Current Time: {json_data['time_zone']['current_time']}
          ''')
        except HTTPError as e:
          print(e)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide an IP address as an argument.')
    else:
        ip = sys.argv[1]
        ipmap = IPMap()
        ipmap.resolve(ip)