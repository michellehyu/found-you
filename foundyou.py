from urllib import request as urllibReq
import json
import webbrowser


class FindYouErrors(Exception):
    pass


def getUrlJson(url):
    '''
        this is a helper funtion to get json response from url
    '''
    try:
        result = json.loads(urllibReq.urlopen(url).read().decode('utf-8'))
        return result
    except:
        raise


def getMyIP():
    '''
        this function gets public ip from ipify.org
    '''
    try:
        ip_info = getUrlJson('https://api.ipify.org?format=json')
        if 'ip' in ip_info:
            return ip_info['ip']
        else:
            raise FindYouErrors("invalid ip returned")
    except:
        print("cannot get ip")
        raise


def getLocationByIP(ip):
    '''
        this function gets the location information of the ip
    '''
    try:
        url = 'http://freegeoip.net/json/' + ip
        loc_info = getUrlJson(url)
        if 'latitude' in loc_info and 'longitude' in loc_info:
            return loc_info
        else:
            raise FindYouErrors("invalid location info returned")
    except:
        print("cannot get longitude and latitude")
        raise


def showLocOnMap(lon, lat):
    '''
        this funciton shows the longitude and latitude
        on google maps in a browser
    '''
    url = 'https://www.google.com/maps/place/@{lat},{lon}'.format(lat=lat, lon=lon)
    webbrowser.open(url)
    return url


def showPlacesAround(types, lon, lat):
    '''
        this funciton shows the types of places around the
        longitude and latitude on google maps in a browser
    '''
    url = 'https://www.google.com/maps/search/{types}/@{lat},{lon}'.format(types=types, lat=lat, lon=lon)
    webbrowser.open(url)
    return url


def main():
    '''
        this main program shows two webpages:
            the user location
            the stores around the user
    '''
    try:
        ip = getMyIP()
        loc = getLocationByIP(ip)
        showLocOnMap(loc['longitude'], loc['latitude'])
        showPlacesAround("stores", loc['longitude'], loc['latitude'])
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
