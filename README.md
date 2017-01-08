# estatusboard
Small python application that shows weather and time over a custom background.

Built for raspberry pi with the official 800x480 display.

Based on the popular Magic Mirror project:  https://github.com/MichMich/MagicMirror

# Setup
* Clone repo to the raspberry pi (recommended to use virtualenv)
* Install Flask
* Obtain Weather Underground api key:  https://www.wunderground.com/weather/api/
* Edit config.py file with key and location information
* Add files to /static/img folder (viewed as "cover")
* Run the application and navigate to Pi browser to http://127.0.0.1:5000

# Tips If Managing via ssh
* Install gnu screen and xdotool
* Open one screen to run the estatusboard application
* Open another screen and run the epiphany (or other) browser
```
export DISPLAY=":0"
epiphany http://127.0.0.1:5000 &
```
* Exit screen and then force the display fullscreen
```
export DISPLAY=":0"
xdotool key F11
```
