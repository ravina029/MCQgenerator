import os 
import json
import pandas as pd 
import traceback
from dotenv import load_dotenv

from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from langchain_community.callbacks.manager import get_openai_callback
from langchain_openai import ChatOpenAI
from src.mcqgenerator.Mcqgenerator import generate_evaluate_chain

load_dotenv()  # Load environment variables

st.title("MCQ generator application with LangChain")

with st.form("user input"):
    uploaded_file = st.file_uploader("Upload PDF or text file")
    number = st.number_input("No of MCQs", min_value=3, max_value=50)
    subject = st.text_input("Insert subject", max_chars=20)  # Corrected max_chars
    tone = st.text_input("Complexity level of questions", max_chars=20, placeholder='simple')  # Corrected max_chars
    button = st.form_submit_button("Create MCQs")

    if button and uploaded_file is not None and number and subject and tone:
        with st.spinner("Loading...."):
            try:
                text = read_file(uploaded_file)  # Ensure read_file accepts an argument
                with open("/Users/ravina/Desktop/MCQGenerator/response.json", "r") as f:
                    response_json = json.load(f)

                # Count token and the cost of API call 
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain(
                        {
                            "text": text,
                            "number": number,
                            "subject": subject,
                            "tone": tone,
                            "response_json": json.dumps(response_json)
                        }
                    )
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
            else:
                print(f"Total tokens: {cb.total_tokens}")
                print(f"Prompt tokens: {cb.prompt_tokens}")
                print(f"Completion tokens: {cb.completion_tokens}")
                print(f"Total cost: {cb.total_cost}")
                
                if isinstance(response, dict):
                    Quiz = response.get("quiz", None)
                    if Quiz is not None and Quiz.startswith("### response_json"):
                        Quiz = Quiz.replace("### response_json", "").strip()

                        """
                        try:
                            quiz = json.loads(Quiz)
                            print("Successfully parsed JSON!")
                        except json.JSONDecodeError as e:
                            print("JSON decoding failed:", e)
                        """

                        table_data = get_table_data(Quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index + 1 
                            st.table(df)

                            # Display the review as well in the text box.
                            st.text_area(label='Review', value=response['review'])
                        else: 
                            st.error("Error in the table data") 
                    else:
                        st.write(response)
