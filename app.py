from flask import Flask, jsonify,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', message='Hello World!')

@app.route('/about')
def about():
    return render_template('index.html', message='About')

@app.route('/api/v1/login')
def login():
    return jsonify({'message': 'Login'})
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=9000)
