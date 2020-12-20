from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
class FilePool:
    index=0
    def new():
        index+=1
        return index-1
class Roldo(Resource):
    def post(self):
        with audio_file=open("tmp"+FilePool.new()+".wav",'wb')
            audio_file.write(request.json['audio'])
            return ia(audio_file.path)

api.add_resource(Roldo, '/roldo')  

if __name__ == '__main__':
     app.run(port='5000')