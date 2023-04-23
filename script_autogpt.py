import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']   # set your API key
#use autogpt to generate a poem
response = openai.Completion.create(
    engine="davinci",
    prompt="write a 4 line poem about a dog. the poem should be happy and suitable for children.",
    temperature=0.5,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
)
print(response.choices[0].text)
