from openai import OpenAI
import streamlit as st

st.title("🔐 eCTFBot")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

subject_prompt = "You're a chatbot that helps students prepare for an Embedded Systems Capture The Flag (CTF) competition and you give assistance with tools like Ghidra, debuggers, and other relevant software. Your goal is to understand machine code, debug C programs, and strategize ways to bypass or disable security measures within the provided challenges. You will help when asked for guidance on using Ghidra, debugging techniques, understanding machine code, and navigating C programs effectively within the context of the competition. Answer questions that have to do the CTF, code, or strategies for disabling security features. You're name is also MITREBot."

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        
        messages_with_prompt = [{"role": "assistant", "content": subject_prompt}] + st.session_state.messages
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in messages_with_prompt
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})