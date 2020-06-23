import requests
import json

file = open('auth_token.txt', 'r')
token = file.readlines()
print(token[0])