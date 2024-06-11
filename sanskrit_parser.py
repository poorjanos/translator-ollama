sanskrit_response_70b = ollama.chat(model='llama3:70b', messages=[
    {'role': 'system', 'content': 'You are a sanskrit scholar and linguist. Parse and explain the text. Express doubt when not sure of parsing'},
    {
      'role': 'user',
      'content': """
content
"""
  },
])

print(sanskrit_response_70b['message']['content'])