from flask import Flask, render_template, request

from magichome import MagicHomeApi

app = Flask(__name__)

light_ip='192.168.2.12'


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/meow')
def meow():
	return 'meow'

@app.route('/ledon')
def led():
	controller1 = MagicHomeApi(light_ip, 0)
	controller1.turn_on()
	return 'Party Lights On'

@app.route('/ledoff')
def ledoff():
	controller1 = MagicHomeApi(light_ip, 0)
	controller1.turn_off()
	return 'Party Lights Off'

@app.route('/ledset')
def ledset():
	controller1 = MagicHomeApi(light_ip, 0)
	rgb = request.args.get('rgb')


controller1.update_device(int(rgb[0:2]), int(rgb[3:5]), int(rgb[6:8]))
	return 'Party Lights Set'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
