import cohere
from config import COHERE_API_KEY
user_key = ''
user_key = input('If you have a Cohere API Key, please input now. Otherwise, please press [ENTER]\n>>')

if(user_key):
    co = cohere.Client(user_key)
else: 
    co = cohere.Client(COHERE_API_KEY)

words = ''
def call_api(words, temp):
    response = co.chat(
        message= words,
        model="command",
        temperature= temp,
        max_tokens = 300, # maximum response length to prevent crashing
    )
    
    return response    
words = input('Chat with Cohere API! If you would like to end the chat session, please type END. \nIf you would like to adjust the creativity of the chat, please type CREATIVITY. \n>>')
creativity = .3
while words != 'END':
    if words.strip() == 'CREATIVITY': 
        creativity = input('Please enter a number from 0 - 10 to set creativity: \n>>')
        creativity = float(creativity.strip())
        creativity = creativity/10
        words = input(f'Creativity set to {creativity}. Please continue chatting! >>')
    output = call_api(words,creativity)
    print(output.text + '\n')
    if hasattr(output, 'finish_reason') and output.finish_reason == "MAX_TOKENS":
        print("\n[Notice: The response was truncated because it reached the maximum token limit.]")
    words = input(f'[Creativity Level: {creativity}] [Type END to end chat]>>')
    words = words.strip()
print('Thank you for chatting with Cohere API.')

