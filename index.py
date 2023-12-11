from flask import Flask, Response, request, render_template
from model import wikicrawler
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return Response(
        content_type='text/json', 
        response=json.dumps({
            'status': 'on',
            'message': 'Welcome to the API. Please use the following endpoints: /data, /data/<key>, /data/<key>/<value>, /data/count/<key>/all'
        })
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('httpcat.html', title="404", image="https://http.cat/404"), 404


@app.route('/update', methods=['POST'])
def update():
    print('Updating database.')
    update = wikicrawler.Webcrawler()
    
    return {
        'status': 'on',
        'message': 'Updating database.'
    }


if __name__ == '__main__':
    app.run(debug=True)