import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers, HuggingFaceHub
import os

os.environ['HUGGINGFACEHUB_API_TOKEN'] = #paste your actual hugging face token here 


## Function To get response from LLAma 2 model
def getresponse(input_text, no_words):

    # GPT-neox20b model (removed unnecessary parameter)
    llm = HuggingFaceHub(repo_id='EleutherAI/gpt-neox-20b')

    ## Prompt Template
    template = """
    Write a blog on the topic {input_text}
    within {no_words} words. Make sure to use proper punctuations and grammar.
    """

    prompt = PromptTemplate(input_variables=["input_text", 'no_words'],
                           template=template)

    # Generate the response from the GPT-neox20b model
    response = llm(prompt.format(input_text=input_text, no_words=no_words))
    print(response)
    return response


# Set the Hugging Face API token from the environment variable (outside the function)

st.set_page_config(page_title="Generate Blogs",
                   page_icon='',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs ")

input_text = st.text_input("Blog Topic")

## Creating two columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')

submit = st.button("Generate")

## Final response
if submit:
    st.write(getresponse(input_text, no_words))
