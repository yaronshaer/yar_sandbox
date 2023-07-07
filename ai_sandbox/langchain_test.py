import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator


api_key = os.getenv("OPENAI_API_KEY")
serpapi_key = os.getenv("SERPAPI_API_KEY")
pinecone_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENV")


llm = OpenAI(temperature=0.9)

#simple prompt fed to LLM through langchain
prompt = "suggest the top 3 things to do in Stockholm with 2 young children aged 6 and 4."
#print(llm(prompt))

#now try prompt template and feed it to LLM
prompt = PromptTemplate(
    input_variables=["adjective","object", "place"],
    template="What is the most {adjective} {object} in {place}?",
)
#prompt= prompt.format(place="house", adjective="famous", city="London")
#print(llm(prompt))

#now try chain LLM and prompt together
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run(object="restaurant", adjective="expensive", place="world"))

tools=load_tools(["serpapi","llm-math"], llm=llm)
agent=initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
agent.run("who is the current CEO of Klarna? and what is his age divided by 2?")
