import magichue
from flask import Flask, render_template, request

#docs here: https://pypi.org/project/python-magichue/

app = Flask(__name__)

light_ip = '192.168.2.12'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/meow')
def meow():
    return 'meow'


@app.route('/ledon')
def led():
    magichue.Light(light_ip).on = True
    return 'Party Lights On'


@app.route('/ledoff')
def ledoff():
    magichue.Light(light_ip).on = False
    return 'Party Lights Off'


@app.route('/ledset')
def ledset():
    rgb = request.args.get('rgb')
    if len(rgb) == 9:
        magichue.Light(light_ip).rgb = (int(rgb[0:2]), int(rgb[3:5]), int(rgb[6:8]))
        return 'Party Lights Set'
    if len(rgb) == 12:
        magichue.Light(light_ip).rgb = (int(rgb[0:2]), int(rgb[3:5]), int(rgb[6:8]))
        magichue.Light(light_ip).brightness = int(rgb[9:11])*10
        return 'Party Lights Set With Brightness'
    return 'Party Lights Not Set'

@app.route('/ledrainbow')
def ledrainbow():
    magichue.Light(light_ip).mode = magichue.RAINBOW_CROSSFADE
    magichue.Light(light_ip).speed = 0.75
    return 'Rainbow'


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
