import os
import requests

api_endpoint=" https://api.openai.com/v1/completions"
api_key = os.environ['OPENAI_API_KEY']
prompt = "say this is a test"
model ="text-davinci-003"
request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_data = {
    "model": model,
    "prompt": prompt,
    "max_tokens": 100,
    "temperature": 0.5
}


response = requests.post(api_endpoint, headers=request_headers, json=request_data)
if response.status_code == 200:
    print(response.json())
else:
    print("something went wrong")




