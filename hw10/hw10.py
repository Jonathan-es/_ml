import ollama

response = ollama.chat(model='llama3:2.3b', messages=[{
    'role': 'user', 
    'content': "what is the reason World War 2 happened?"}])
print(response["message"]["content"])