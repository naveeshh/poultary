from flask import Flask, request


app = Flask(__name__)


@app.route('/query_example/')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None
    framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
    website = request.args.get('website')

    return '''<h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}</h1>'''.format(language, framework, website)


@app.route('/form_example')
def form_example():
    return 'dodo'


@app.route('/json_example')
def json_example():
    return 'dodo'


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)


