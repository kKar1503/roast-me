import ollama
from flask import Flask, request
from typing import Dict, List, Literal, Union

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>bruh</p>"

class ChatMessage:
    role: Union[Literal['user'], Literal['assistant']]
    content: str

chats: Dict[str, List[ChatMessage]] = {}

@app.get('/roast/<id>')
def roast_me(id):
    # Obtain the name parameter from the request
    name = request.args.get('name', '')

    chat_history = chats.get(id)
    if chat_history is None:
        role_message = ChatMessage()
        role_message.role = "user"
        role_message.content = "You are a professional shitposter. Your job is to roast me when I ask. Make it short, fun and be as aggressive, unhinged and as vile as you like. I want my ego to be obliterated."

        me_message = ChatMessage()
        me_message.role = "user"
        me_message.content = f"About me: My name is {name}."

        chat_history = [role_message, me_message]
        chats[id] = chat_history

    message = ChatMessage()
    message.role = "user"
    message.content = "Roast me bitch"
    chat_history.append(message)
    
    obj_history = map(lambda chat_message: {
        'role': chat_message.role,
        'content': chat_message.content,
    }, chat_history)
    obj_history = list(obj_history)

    response = ollama.chat(model='llama3', messages=obj_history)
    response_message = response['message']

    message = ChatMessage()
    message.role = "assistant"
    message.content = response_message['content']
    chat_history.append(message)

    # Return the roast
    return {
        "roast": message.content,
    }