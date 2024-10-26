import streamlit as st
import subprocess

st.title("Welcome to offer.ai")

def page1():
    st.title("Company 1")
    st.write("This company prioritizes stuff like this, this, this. Select what type of question you'd like.")

    def page1_a():
        st.title("blah blah")
        st.write("lsdjfsl")
        code_input = st.text_area("Enter your code below:", height=200)

        if st.button("Run Code in Python"):
            try:
                exec_locals = {}
                codeExecution = exec(code_input, {}, exec_locals)
            except Exception as e:
                st.error(f"Error executing code: {e}")
        elif st.button("Run Code in Javascript"):
            try:
            # Use subprocess to run the code through Node.js
                process = subprocess.run(
                ["node", "-e", code_input],
                capture_output=True,
                text=True,
                check=True
        )
                codeExecution = process.stdout

            except subprocess.CalledProcessError as e:
                st.error(f"Error executing code: {e.stderr}")

    if st.button("Question Type 1_a"):
        st.session_state["page"] = "page1_a"
        st.stop()

    if st.button("Wrong Company!"):
        homepage()
        st.stop()

if st.button("Page 1"):
        page1()
        st.stop()

