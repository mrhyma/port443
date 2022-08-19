
import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
	"X-RapidAPI-Key": os.getenv("X_RAPIDAPI_KEY"),
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}


class Joke:
	def __init__(self, setup, punchline):
		
		self.setup = setup
		self.punchline = punchline

def getJoke():
	the_response = requests.request("GET", url, headers=headers)
	data = the_response.json()
	joke = Joke(data['body'][0]['setup'], data['body'][0]['punchline'])
	return joke

