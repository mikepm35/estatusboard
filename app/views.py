from flask import render_template, jsonify
from app import application
import urllib2, json
from os import listdir
from os.path import isfile, join
import config

@application.route('/')
@application.route('/index')
def index():
    imgpath = 'app/static/img/'
    imgfiles = [f for f in listdir(imgpath) if isfile(join(imgpath, f))]
    imgfullpath = []
    for i in imgfiles:
        imgfullpath.append('/static/img/'+i)
    imgfullpath_json = json.dumps(imgfullpath)

    return render_template("index.html", imgfullpath=imgfullpath_json)

@application.route('/getweather')
def getweather():
    wu_url_hourly = "http://api.wunderground.com/api/" + config.WUNDERGROUND_APIKEY + "/hourly/q/" + config.STATE_CODE + "/" + config.CITY + ".json"
    wu_url_daily = "http://api.wunderground.com/api/" + config.WUNDERGROUND_APIKEY + "/forecast/q/" + config.STATE_CODE + "/" + config.CITY + ".json"

    result_hourly = urllib2.urlopen(wu_url_hourly).read()
    data_hourly = json.loads(result_hourly)
    temp = data_hourly['hourly_forecast'][0]['temp']['english']
    # rain = data['hourly_forecast'][0]['pop']

    result_daily = urllib2.urlopen(wu_url_daily).read()
    data_daily = json.loads(result_daily)
    rain = data_daily['forecast']['simpleforecast']['forecastday'][0]['pop']
    icon = data_daily['forecast']['simpleforecast']['forecastday'][0]['icon_url']

    return jsonify(temp=temp, rain=rain, icon=icon)
