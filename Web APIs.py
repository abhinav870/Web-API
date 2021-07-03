from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
# Creating an app within flask

api = Api(app)
# Wrapping Our app in the API
# This also initializes the fact that we are using restful API

# reqparse is a module containing RequestParser class
video_put_args = reqparse.RequestParser()
# we are making a RequestParser object. This obj will automatically parse through the request being sent and make sure
# that it fits the guidelines that we will define and has the correct info in it
# if it fits, then it will allow us to grab all the info easily
# using a method called parse_args defined inside put() [inside the class Video]

video_put_args.add_argument("name",type=str,help="Name of the Video is required",required = True)
# this tells us that we are receiving some arguments (from the request being sent using API)
# "name" is the name of the argument, "type" is its datatype
# "help" is the error msg that is displayed when a wrong request is sent
# required = True makes it compulsory to send the arguments, otherwise the error message is displayed

video_put_args.add_argument("views",type=int,help="Views of the Video are required",required = True)
video_put_args.add_argument("likes",type=int,help="Likes on the Video are required",required = True)

videos = {}

# prevents server from crashing if video id doesn't exist
def abort_if_video_id_not_present(video_id):
	if video_id not in videos:
		abort(404,message="Video ID doesn't exist")

# prevents inserting a new video whose video_id matches with an existing video_id
def abort_if_video_id_present(video_id):
	if video_id in videos:
		abort(409,message="Video ID already exists")

# inheriting our HelloWorld from Resource
class Video(Resource):

	def get(self, video_id):
		abort_if_video_id_not_present(video_id)
		return videos[video_id]

	def put(self, video_id):

		abort_if_video_id_present(video_id)

		# args is a dictionary
		args = video_put_args.parse_args()
		# gets us the 3 arguments namely: name,views,likes iff API is sending correct arguments
		# otherwise it displays us an error msg

		videos[video_id] = args
		# video_id sent as API request will be made as key inside the videos dictionary
		# And its value will be the argument sent by the API request

		return videos[video_id], 201
		# returning 201 is a convention meaning that our request was successfully processed

	def delete(self,video_id):

		# to prevent deletion of a video which doesn't exist
		abort_if_video_id_not_present(video_id)

		# deletes the video with a given video_id
		del videos[video_id]

		# returning 204 means deleted successfully
		return "",204

api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)



