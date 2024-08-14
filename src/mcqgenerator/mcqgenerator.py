import os

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
import os 
import json
import pandas as pd 
import traceback
from dotenv import load_dotenv
import PyPDF2


load_dotenv()

key=os.getenv("OPENAI_API_KEY")
print(key)

llm=ChatOpenAI(openai_api_key=key,model_name="gpt-3.5-turbo",temperature=0.5)

with open("/Users/ravina/Desktop/MCQGenerator/response.json","r") as f:
    response_json=json.load(f)

template1="""
Text: {text}
You are an expert mcq maker. Given the above text, it is your job to create a quiz of {number} multiple choice questions for {subject} students in {tone} which make sure the questions are not repeated and are free from any kind of mistakes also 
all the questions have great quality.make sure to format your response like RESPONSE_JSON below and use it as a guide.

Ensure to make {number} MCQs
### response_json
{response_json}
"""

quiz_prompt_template=PromptTemplate(
    input_variables=['text','number','subject','tone','response_json'],
    template=template1
)

my_quiz_chain=LLMChain(llm=llm,prompt=quiz_prompt_template,output_key="quiz",verbose=True)


template2="""
            You are an expert english grammarian and writer. Given a multiple choice quiz for {subject} you need to evaluate the complexity of the question
            and give a complete analysis of the  generated quiz. If the quiz is not at per with the cognitive and the analytical abilities of students 
            then update the quiz questions which are 
            required to be changed and change the tone such that it matches the required quiz_mcqs:
            {quiz}
            check the above quiz as an expert english writer"""


quiz_evaluation_prompt_template=PromptTemplate(
    input_variables=['subject','quiz'],
    template=template2
)


review_chain=LLMChain(llm=llm,prompt=quiz_evaluation_prompt_template,output_key="review",verbose=True)

generate_evaluate_chain=SequentialChain(chains=[my_quiz_chain, review_chain],input_variables=['text',"number",'subject',"tone","response_json"], output_variables=["quiz","review"], verbose=True)

