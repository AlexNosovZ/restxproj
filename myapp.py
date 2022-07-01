from flask import Flask
# ,request
# from flask_restx import Api,Resource
from myapi import blueprint as api

# api = Api()

app = Flask(__name__)
# api.init_app(app)
# parser = api.parser()
# parser.add_argument('message', type=int, help='message!!!', required=True, location='form')

# @api.route('/echo')
# class Echo_cls(Resource):
#     @api.expect(parser)
#     def post(self):
#         args = parser.parse_args()
#         print(args)
#         return 'echo ' + request.form.get('message')

app.register_blueprint(api)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,debug=True)
# from flask import Flask, request
# from flask_restx import Api, Resource

# api = Api()

# app = Flask(__name__)
# api.init_app(app)


# @api.route('/echo')
# class Echo(Resource):
#     def post(self):
#         return 'echo ' + request.form.get('message')


# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=5055, debug=True)