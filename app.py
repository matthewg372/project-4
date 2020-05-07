from flask import Flask


DEBUG=True
PORT=8000

app = Flask(__name__)
app.secret_key = "ajhskdjasdhkasdjhkaiudhajugjhgdjhsgfhgjskdhjkfhjashd"


@app.route('/')
def testing():
	return 'hello working'


if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)