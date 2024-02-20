import streamlit as st
from gemini import generate_query_result
import pyperclip
def main():
    st.title("SQL Query Generator")

    # Create a 2-column layout
    col1, col2 = st.columns(2, gap="large")    

    # Place inputs in the left column
    with col1:
        question = st.text_area("Enter your question:", height=5)
        st.empty()
        schema = st.text_area("Enter your schema:", height=20)

    # Generate query result (placeholder for now)
    result = generate_query_result(question, schema)

    # Place output in the right column
    with col2:
        if st.button("Generate Query Result"):
            st.write("Query Result:")
            st.write(result)
            st.button("Copy Result", on_click=copy_result, args=(result,))

def copy_result(result):
    pyperclip.copy(result)

if __name__ == "__main__":
    main()
