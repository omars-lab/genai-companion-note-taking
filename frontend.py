import streamlit as st
from idea_gen_chain import idea_generation_chain
from langchain_openai import ChatOpenAI

# Default UX
st.title("Marketing Helper")
use_case = st.sidebar.selectbox("Pick a use case", ("Note Taking Companion", "Financial Helper", "Marketing Assistant"))

# The following UX is appended to the page based on the value picked in the previous step.
if use_case:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.9)
    response = idea_generation_chain(llm, use_case)
    for k, v in response.items():
        st.header(f"Suggestions for {k}")
        for x in v:
            st.markdown(f"* {x}")
