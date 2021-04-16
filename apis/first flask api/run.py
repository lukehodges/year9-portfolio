from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)
count = 1
@app.route('/', methods=['GET'])
def get_tasks():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return {'ip': request.environ['REMOTE_ADDR']}, 200
    else:
        return {'ip': request.environ['HTTP_X_FORWARDED_FOR']}, 200
class HelloWorld(Resource):
	def get(self):
		global  count
		count += 1
		return {"data":f"Hello world count : {count}"}
api.add_resource(HelloWorld,'/helloworld')
if __name__=="__main__":
	from flask import request


	app.run(debug=True,host="0.0.0.0",port="80")
	request.environ.get('HTTP_X_REAL_IP', request.remote_addr)