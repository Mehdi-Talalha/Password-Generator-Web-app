import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>Password Generator</title></head>
    <body>
        <h1>Password Generator is Working!</h1>
        <p>If you see this, the deployment succeeded.</p>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
