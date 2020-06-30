
import discord
import random
from discord.ext import commands

dialogues = [
"Remember, with great power comes great responsibility.",
"YES! We know each other. He's a friend from work.",
"I am Groot!",
"Genius, billionaire, playboy, philanthropist... me",
"I like this one.",
"Get this man a shield!",
"I'll do you one better. Why is Gamora?",
"Yeah. I knocked out Adolf Hitler over 200 times.",
"Nature made me a freak. Man made me a weapon. And God made it last too long.",
"Intelligence is a privilege, and it needs to be used for the greater good of people.",
"*Nothing* goes over my head...! My reflexes are too fast, I would catch it.",
"I love you 3000.",
"And I am Iron Man.",
"Avengers! ASSEMBLE!",
"Hulk...smash!",
"I have a plan. Attack!",
"Puny God!"
]


	

token = open('token.txt', 'r').read().strip()
client = commands.Bot(command_prefix=':')

# Quick little notification on the terminal to show that the bot is active
@client.event
async def on_ready():
	print('Jarvis lives...')

# A cute little feature that I thought would lighten things up
# everytime someone mesages 'hey jarvis' Jarvis spits out a line 
# from the Avengers Saga
@client.event
async def on_message(message):
	# We don't want to keep triggering this function from our own messages
	if message.author == client.user:
		return 

	# if the message starts with 'hey jarvis'
	# send a random dialogue back to the channel
	if message.content.lower().startswith('hey jarvis') :
		dialogueNo = int(random.random()*len(dialogues))
		await message.channel.send(dialogues[dialogueNo])

client.run(token)
