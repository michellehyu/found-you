from urllib import request as urllibReq
import json
import webbrowser

def getUrlJson(url):
    result = json.loads(urllibReq.urlopen(url).read().decode('utf-8'))
    return result

def getMyIP():
    ip_info = getUrlJson('https://api.ipify.org?format=json')
    return ip_info['ip']

def getLocationByIP(ip):
    url = 'http://freegeoip.net/json/' + ip
    loc_info = getUrlJson(url)
    return loc_info

def showLocOnMap(lon, lat):
    webbrowser.open('https://www.google.com/maps/place/{lat},{lon}'.format(lat=lat, lon=lon))

ip = getMyIP()
loc = getLocationByIP('73.225.219.177')
showLocOnMap(loc['longitude'], loc['latitude'])
