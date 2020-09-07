import flask
from flask import jsonify
import requests
import re

# simple bash.org.pl dumper
def get_quotes():
  bash = requests.get('http://bash.org.pl/text')
  return re.findall(r'\#(\d+).*\n([\s\S]*?)\n+%\n', bash.text)

# convert dumped data to dictionary list 
def quotes_dict_list(data): 
  return [{'id': data[i][0], 'text': data[i][1]} for i in range(0, len(data))]

# define Flas application
app = flask.Flask(__name__)

# main route
@app.route('/', methods=['GET'])
def home():
    return '''<h1>bash.org.pl microservice</h1>
<p>This is sample dummy API microservice scraping bash.org.pl for latest quotes</p>'''

# dummy route to return 100 latest the available quotes.
@app.route('/api/v1/resources/quotes', methods=['GET'])
def api_100():
    return jsonify(quotes_dict_list(get_quotes())[:100])

# route to return all of the available quotes.
@app.route('/api/v1/resources/quotes/all', methods=['GET'])
def api_all():
    return jsonify(quotes_dict_list(get_quotes()))

if __name__ == '__main__':
  app.run()