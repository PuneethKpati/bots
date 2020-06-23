import requests
import json

file = open('auth_token.txt', 'r')
token = file.readlines()
token = token[0]

headers = {
	'Connection': 'close',
	'Accept': 'application/json, text/plain, */*',
	'Authorization': 'Bearer ' + token,
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
	'Origin': 'https://homework.zookal.com',
	'Sec-Fetch-Site': 'same-site',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Dest': 'empty',
	'Referer': 'https://homework.zookal.com/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

resp = requests.get('https://api.homework.zookal.com/api/v1/questions?per=100&page=1', headers=headers)

obj = json.loads(resp.text)

for question in obj['questions']:
	print('======================================\nquestion:' + str(question['id'])  + '\n======================================' )
	print('status :', question['status'])
	print('category :', question['category'])
	print('subcategory :', question['subcategory'])
	print('\n')