import os
import sys
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage,
    AIMessage
)

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory, ConversationEntityMemory, ConversationSummaryMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE

def main():
    load_dotenv()

if __name__ == "__main__":
    main()


#do we have an openai api key?
if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
    print("Please set OPENAI_API_KEY ")
    exit(1)
else:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    print("OPENAI_API_KEY set")

langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
langchain_tracing = os.getenv("LANGCHAIN_TRACING_V2")
langchain_endpoint = os.getenv("LANGCHAIN_ENDPOINT")
langchain_project = os.getenv("LANGCHAIN_PROJECT")

chat = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")

system_input = "You are a helpful assistant."

messages = [SystemMessage(content=system_input),]


print("You chatting with ChatGPT clone...")

def chat_own_memory():
    print("Assistant has own built-in buffer memory")
    user_input = ""
    while user_input.lower() != "quit":
        user_input = input("> ")
        messages.append(HumanMessage(content=user_input))
        ai_response = chat(messages)
        messages.append(AIMessage(content=ai_response.content))
        print("\nAssistant:\n",ai_response.content)


def chat_no_memory():
       print("Assistant has no memory")
       while True:
        user_input = input("> ")
        messages = [SystemMessage(content=system_input),HumanMessage(content=user_input)]
        ai_response = chat(messages)
        print("\nAssistant:\n",ai_response.content)

def chat_buffer_memmory():
    print("Assistant has buffer memory")
    conversation = ConversationChain(llm=chat, memory=ConversationBufferMemory(), verbose=True)
    while True:
        user_input = input("> ")
        ai_response = conversation.predict(input=user_input)
        print("\nAssistant:\n",ai_response)

def chat_entity_memmory():
    print("Assistant has entity memory")
    conversation = ConversationChain(llm=chat, memory=ConversationEntityMemory(llm=chat), verbose=True, 
                                     prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE)
    while True:
        user_input = input("> ")
        ai_response = conversation.predict(input=user_input)
        print("\nAssistant:\n",ai_response)

def chat_summary_memmory():
    print("Assistant has summary memory")
    conversation = ConversationChain(llm=chat, memory=ConversationSummaryMemory(llm=chat), verbose=True)
    while True:
        user_input = input("> ")
        ai_response = conversation.predict(input=user_input)
        print("\nAssistant:\n",ai_response)

def chat_openai():
    print("Assistant is Openai vanilla with no memory")
    import openai
    openai.api_key = openai_api_key
    user_input=""
    while user_input.lower() != "exit":
        user_input = input("> ")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}])
        print(response.choices[0].message.content)





if len(sys.argv)>=2:
    mem_argument = sys.argv[1].lower()
    if mem_argument ==  "no_mem":
        chat_no_memory()
    
    elif mem_argument == "own_mem":
        chat_own_memory()
    
    elif mem_argument == "ent_mem":
        chat_entity_memmory()

    elif mem_argument == "sum_mem":
        chat_summary_memmory()

    elif mem_argument == "buf_mem":
        chat_buffer_memmory()
        
    else:
        chat_no_memory()

else:
    chat_openai()