import flask
import flask_cors
import memory
import os
import logging

logging.getLogger("werkzeug").setLevel(logging.ERROR)
app = flask.Flask('__main__')
flask_cors.CORS(app)

@app.route('/')
def index():
    return flask.render_template('index.html', base_url=f'http://127.0.0.1:{os.environ['SERVE_PORT']}')

@app.route('/msgs')
def get_msgs():
    offset = int(flask.request.args.get('offset', 0))
    messages = []
    for message in memory.loaded_messages:
        if message['id'] >= offset:
            # messages.append({
            #     'id': message.id,
            #     'author_username': message.author_username,
            #     'content': message.content
            # })
            messages.append(message)
    
    return messages

