import os
from dotenv import load_dotenv


COHERE_API_KEY = '' # INPUT COHERE API KEY HERE

if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY environment variable not set!")