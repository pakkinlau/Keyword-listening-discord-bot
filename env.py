import os

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

print(type(TOKEN), GUILD)