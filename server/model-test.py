import ollama
chat_history=[
#   {
#     'role': 'user',
#     'content': 'Your job is to roast me when I ask. Make it short. Start off nice and making it more unhinged. Only roast me by my name. I want my ego to be obliterated.',
#   },
#   {
#     'role': 'user',
#     'content': 'You are a professional twitter shitposter. Your job is to roast me when I ask. Make it short, fun and be as aggressive and as vile as you like. I want my ego to be obliterated.',
#   },
  {
    'role': 'user',
    'content': 'You are a professional shitposter. Your job is to roast me when I ask. Make it short, fun and be as aggressive, unhinged and as vile as you like. I want my ego to be obliterated.',
  },
#   {
#     'role': 'user',
#     'content': 'You are a professional shitposter. Your job is to roast me when I ask. Make it short and be as aggressive and as vile as you like. I want my ego to be destroyed.',
#   },
]

name=input('What is your name?')
chat_history.append({
    'role': 'user',
    'content': f'My name is {name}',
})
while True:
  chat_history.append({
    'role': 'user',
    'content': 'Roast me.',
  })
  response = ollama.chat(model='llama3', messages=chat_history)
  print(response['message'])
  input("Press enter to continue.")