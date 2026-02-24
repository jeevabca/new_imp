from google import genai

# create client
client = genai.Client(api_key="AIzaSyDS7zAG_G3cYKcZxPAKxboVXeIsL0nJjEg")

# list available models
for model in client.models.list():
    print(model.name)