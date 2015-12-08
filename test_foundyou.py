import unittest
import foundyou


def test_getUrlJson():
    result = foundyou.getUrlJson('http://api.ipify.org?format=json')
    assert result is not None
    assert ('ip' in result) == True
    assert ('location' in result) == False


def test_getMyIp():
    ip = foundyou.getMyIP()
    assert ip is not None
    assert ip.count(".") == 3


def test_getLocationByIp():
    loc = foundyou.getLocationByIP("17.0.0.1")
    assert loc is not None
    assert ('longitude' in loc) == True
    assert ('latitude' in loc) == True
    assert ('longitude' in loc) == True
    assert loc['latitude'] == 37.3042
    assert loc['longitude'] == -122.0946


def test_showLocOnMap():
    url = foundyou.showLocOnMap(37.3042, -122.0946)
    assert url == "https://www.google.com/maps/place/@-122.0946,37.3042"


def test_showPlacesAround():
    url = foundyou.showPlacesAround("coffee", 37.3042, -122.0946)
    assert url == "https://www.google.com/maps/search/coffee/@-122.0946,37.3042"
