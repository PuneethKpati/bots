import requests
import json
import time


class API:
	def __init__(self):

		# Get the authorisation token retrieved from the cookies or HTTP headers 
		file = open('auth_token.txt', 'r')
		token = file.readlines()
		self.token = token[0]

		# we require this header mainly for the Authorisation
		# I replicated this format from the original HTTP request I sent to retrive the API data
		self.headers = {
			'Connection': 'close',
			'Accept': 'application/json, text/plain, */*',
			'Authorization': 'Bearer ' + self.token,
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
			'Origin': 'https://homework.zookal.com',
			'Sec-Fetch-Site': 'same-site',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Dest': 'empty',
			'Referer': 'https://homework.zookal.com/',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
		}

		self.questions = {}	# dictionary to hold the JSON object of all current questions
		self.seen = []		# list of all active and seen questions


	# main function for the file that does the repetitive crawling
	# it is currently timed out at 20 seconds, 
	# TO-DO: make the time of sleep value dependant on object
	def crawl_new_questions(self):
		new_seen = []
		requestNo = 0 
		# Keep sending requests FOREVER MWAHAHAHHA
		while True:
			# keeping track of the number of reuqests for sanity
			print('Request number: ', requestNo)
			# get the current state of questions 
			new_questions = self.get_questions()
			# if a question has been seen before, ignore it
			# else call for an alert with the new question
			for question in new_questions:
				new_seen.append(question['id'])
				if question['id'] in self.seen:
					continue
				else:
					self.alert(question)
			# update the state of questions and the seen list of questions
			# this allows us to ignore questions that are no longer active
			self.questions = new_questions
			self.seen = new_seen
			# update the request number
			requestNo += 1

			# Don't send a request for 20 seconds
			time.sleep(2)

		return

	# sends a request to Zookal Api and retrieves the JSON data 
	# Converts the HTTP string text to JSON readable format
	# returns the list of all active questions' JSON objects
	def get_questions(self):
		# send the request with the proper headers
		resp = requests.get('https://api.homework.zookal.com/api/v1/questions?per=100&page=1', headers=self.headers)
		# convert the http response text into JSON objects for easier data management 
		obj = json.loads(resp.text)

		# return the list of all questions from the JSON Object
		return obj['questions']


	# this function is to be updated further
	# this can be the endpoint from which we call notification bots 
	# like discord or slack bots
	# for now, just print the alert message to terminal
	def alert(self, question):
		print('New question!')
		self.print_question(question)

	# print a single questions
	# only the necessary attributes are printed
	def print_question(self, question):
		print('======================================\nquestion:' + str(question['id'])  + '\n======================================' )
		print('status :', question['status'])
		print('category :', question['category'])
		print('subcategory :', question['subcategory'])
		print('\n')

	# print a list of given questions
	def print_questions(self, questions):
		print('Number of Questions :' + str(len(questions)))
		for question in questions:
			self.print(question)


api = API()
questions = api.crawl_new_questions()
