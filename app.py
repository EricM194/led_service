from flask import Flask, render_template, request

import magichue, time
#docs here: https://pypi.org/project/python-magichue/

app = Flask(__name__)

light_ip = '192.168.2.12'
light = magichue.Light(light_ip)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/meow')
def meow():
    return 'meow'


@app.route('/ledon')
def led():
    light.on = True
    return 'Party Lights On'


@app.route('/ledoff')
def ledoff():
    light.on = False
    return 'Party Lights Off'


@app.route('/ledset')
def ledset():
    rgb = request.args.get('rgb')
    if len(rgb) == 9:
        light.rgb = (int(rgb[0:2]), int(rgb[3:5]), int(rgb[6:8]))
        return 'Party Lights Set'
    if len(rgb) == 12:
        light.rgb = (int(rgb[0:2]), int(rgb[3:5]), int(rgb[6:8]))
        light.brightness = int(rgb[9:11])*10
        return 'Party Lights Set With Brightness'
    return 'Party Lights Not Set'

@app.route('/ledrainbow')
def ledrainbow():
    light.mode = magichue.RAINBOW_CROSSFADE
    light.speed = 1
    return 'Rainbow'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
