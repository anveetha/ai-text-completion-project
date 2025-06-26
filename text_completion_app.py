import cohere
from config import COHERE_API_KEY

user_key = input('If you have a Cohere API Key, please input now. Otherwise, please press [ENTER]\n>>')

if user_key:
    co = cohere.Client(user_key)
else: 
    co = cohere.Client(COHERE_API_KEY)

def call_api(words, temp):
    response = co.chat(
        message=words,
        model="command",
        temperature=temp,
        max_tokens=300,  # maximum response length to prevent crashing
    )
    return response

creativity = 0.3
words = input('Chat with Cohere API! If you would like to end the chat session, please type END. \nIf you would like to adjust the creativity of the chat, please type CREATIVITY. \n>>').strip()

while words != 'END':
    if words == '':
        # Handle empty input
        words = input('Input cannot be empty. Please enter your message:\n>>').strip()
        continue
    if words == 'CREATIVITY':
        new_creativity = input('Please enter a number from 0 - 10 to set creativity: \n>>').strip()
        if new_creativity == '':
            print('Creativity value cannot be empty.')
            words = input(f'[Creativity Level: {creativity}] [Type END to end chat]>>').strip()
            continue
        try:
            creativity = float(new_creativity) / 10
            print(f'Creativity set to {creativity}.')
        except ValueError:
            print('Invalid input. Please enter a number from 0 to 10.')
        words = input('Please continue chatting! >>').strip()
        continue
    output = call_api(words, creativity)
    print(output.text + '\n')
    if hasattr(output, 'finish_reason') and output.finish_reason == "MAX_TOKENS":
        print("\n[Notice: The response was truncated because it reached the maximum token limit.]")
    words = input(f'[Creativity Level: {creativity}] [Type END to end chat]>>').strip()

print('Thank you for chatting with Cohere API.')
