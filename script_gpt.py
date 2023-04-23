import os
import requests
import gpt_utils

api_endpoint=" https://api.openai.com/v1/completions"
api_key = os.environ['OPENAI_API_KEY']
prompt = "write a 4 line poem about a dog. the poem should be happy and suitable for children."
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
print(gpt_utils.check_response(response))






