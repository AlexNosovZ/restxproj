
from flask import Flask
import sys

from myapi import blueprint as api

app = Flask(__name__)


app.register_blueprint(api)
if __name__ == '__main__':
    if len(sys.argv) > 1:
        cfg = sys.argv[1]
    else:
        cfg = 'conf_test'
    app.config.from_object(cfg)
    print(cfg)
    app.run(host='127.0.0.1', port=5000)
    
