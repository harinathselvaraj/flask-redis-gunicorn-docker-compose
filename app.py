from flask import Flask
from redis import Redis

application = Flask(__name__)
redis = Redis(host='redis', port=6379)

@application.route("/")

def index():
    redis.incr('hits')
    return 'This Flask application has got %s time(s).' % redis.get('hits')

if __name__ == "__main__":
    # application.run(host="0.0.0.0", debug=True)
    application.run(host="0.0.0.0")