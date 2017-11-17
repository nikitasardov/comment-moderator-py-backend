#!/usr/bin/env python3

from flask import Flask, request, Response
#from flask_cors import CORS
import json
import get_functions
import put_functions


app = Flask(__name__)
#cors = CORS(app)

#app_data
app_data = get_functions.read_data()
print(app_data['comments'])

def to_json(data):
    return json.dumps(data, sort_keys=True, indent=2) + '\n'

def resp(code, data):
    return Response(
        status=code,
#        mimetype="application/json",
        response=to_json(data)
    )

#GET /api/articles
@app.route('/api/articles/')
def get_all_articles():
    articles_array = []
    for article in app_data['articles']:
        a = get_functions.get_article_by_id(article['id'], app_data)
        articles_array.append(a)
    return resp(200, articles_array)

#GET /api/articles/<id>
@app.route('/api/articles/<int:article_id>')
def get_article_id(article_id):
    a = get_functions.get_article_by_id(article_id, app_data)
    return resp(200, a)

#PUT /api/comments/1
@app.route('/api/comments/<int:comment_id>', methods=['PUT'])
def put_comment(comment_id):
    if put_functions.put_comment_info(comment_id, request.form['text'], app_data):
        return resp(200, {'success': True})
    else:
        return resp(500, {'success': False})

#PUT /api/user/1
@app.route('/api/user/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    if put_functions.put_user_info(user_id, request.form['name'], app_data):
        return resp(200, {'success': True})
    else:
        return resp(500, {'success': False})

@app.errorhandler(404)
def page_not_found(error):
    #return 'incorrect api address', 400
    bad_request = {'message':'incorrect api address'}
    return resp(404, bad_request)

@app.errorhandler(500)
def internal_error(error):
    #    e = {'message':'internal error'}
    return resp(500, {'message':'internal error'})

@app.errorhandler(400)
def internal_error(error):

    return 400, request.headers

@app.after_request
def _headers__(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS, PUT'
    response.headers['Content-Type'] = 'application/json; charset=utf-8'

    return response

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4567)
