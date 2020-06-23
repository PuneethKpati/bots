import requests
import json
import time


class API:
	def __init__(self):
		file = open('auth_token.txt', 'r')
		token = file.readlines()
		self.token = token[0]

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

		self.questions = {}
		self.seen = []

	def crawl_new_questions(self):
		new_seen = []
		count = 0 
		while True:
			print('Request number: ', count)

			new_questions = self.get_questions()
			for question in new_questions:
				new_seen.append(question['id'])
				if question['id'] in self.seen:
					continue
				else:
					self.alert(question)

			self.questions = new_questions
			self.seen = new_seen
			count += 1

			time.sleep(20)




	def get_questions(self):

		resp = requests.get('https://api.homework.zookal.com/api/v1/questions?per=100&page=1', headers=self.headers)

		obj = json.loads(resp.text)

		return obj['questions']


	def alert(self, question):
		print('New question!')
		self.print_question(question)


	def print_question(self, question):
		print('======================================\nquestion:' + str(question['id'])  + '\n======================================' )
		print('status :', question['status'])
		print('category :', question['category'])
		print('subcategory :', question['subcategory'])
		print('\n')

	def print_questions(self, questions):
		print('Number of Questions :' + str(len(questions)))
		for question in questions:
			print('======================================\nquestion:' + str(question['id'])  + '\n======================================' )
			print('status :', question['status'])
			print('category :', question['category'])
			print('subcategory :', question['subcategory'])
			print('\n')


api = API()
questions = api.crawl_new_questions()
