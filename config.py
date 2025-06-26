import os
from dotenv import load_dotenv


COHERE_API_KEY = 'your-default-api-key-here'

if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY environment variable not set!")
