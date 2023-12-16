from openai import OpenAI
from dotenv import load_dotenv
import os
import json


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

#write a function to get the current weather in a given location

# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API.
def get_current_weather(location, unit="celsius"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "22",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

# Step 1, send model the user query and what functions it should access
def run_conversation():
    response = client.chat.completions.create(model="gpt-3.5-turbo-0613",
    messages=[{"role": "user", "content": "What's the weather like in Tel Aviv?"}],
    functions=[
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
                "required": ["unit"],
            },
        }
    ],
    function_call="auto")
    message =  response.choices[0].message



    #message = response["choices"][0]["message"]


    # Step 2, check if the model wants to call a function
    if message.function_call.name is not None:
        function_name = message.function_call.name
        arguments = json.loads(message.function_call.arguments)



        # Step 3, call the function
        # Note: the JSON response from the model may not be valid JSON
    function_response = get_current_weather(
            location=arguments["location"],
            unit=arguments["unit"],
        )

        # Step 4, send model the info on the function call and function response
    second_response = client.chat.completions.create(model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "user", "content": "What is the weather like in Tel Aviv?"},
            message,
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            },
        ])
    return second_response.choices[0].message.content

print(run_conversation())
