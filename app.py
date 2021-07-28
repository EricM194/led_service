import magichue
import os
from flask import Flask, render_template, request

# docs here: https://pypi.org/project/python-magichue/

app = Flask(__name__)

try:
    led_ip = os.environ['LED_IP']
except KeyError:
    print('env variable "LED_IP" was not provided')
    quit()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ledon')
def led():
    magichue.Light(led_ip).on = True
    return 'LED Lights On'


@app.route('/ledoff')
def ledoff():
    magichue.Light(led_ip).on = False
    return 'LED Lights Off'


@app.route('/ledset')
def ledset():
    rgb = request.args.get('rgb')
    if len(rgb) == 9:
        magichue.Light(led_ip).rgb = (int(rgb[0:2]), int(rgb[3:5]), int(rgb[6:8]))
        return 'LED Lights Set'
    if len(rgb) == 12:
        magichue.Light(led_ip).rgb = (int(rgb[0:2]), int(rgb[3:5]), int(rgb[6:8]))
        magichue.Light(led_ip).brightness = int(rgb[9:11]) * 10
        return 'LED Lights Set With Brightness'
    return 'LED Lights Not Set'


@app.route('/ledrainbow')
def ledrainbow():
    magichue.Light(led_ip).mode = magichue.RAINBOW_CROSSFADE
    magichue.Light(led_ip).speed = 0.75
    return 'Rainbow'


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
