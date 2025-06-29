import streamlit as st
st.title("✅ Streamlit is working!")
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Load AI Model
try:
    llm = OllamaLLM(model="mistral", options={"num_gpu": 0})
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

# Initialize Memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory()

# Define Prompt Template
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="""
You are a helpful AI assistant. Here's the previous conversation:

{chat_history}

Now the user asks:
User: {question}
AI:"""
)

# AI Response Function
def run_chain(question):
    chat_history_text = "\n".join(
        [f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages]
    )
    try:
        with st.spinner("🤖 Thinking..."):
            response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))
    except Exception as e:
        st.error(f"❌ Error calling model: {e}")
        return "Model error. Please check Ollama status."

    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(response)
    return response

# Streamlit UI
st.title("🧠 AI Chatbot with Memory")

with st.form("chat_form"):
    user_input = st.text_input("Your Question:")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    ai_response = run_chain(user_input)
    st.markdown(f"**🧑 You:** {user_input}")
    st.markdown(f"**🤖 AI:** {ai_response}")

st.subheader("🗂️ Chat History")
for msg in st.session_state.chat_history.messages:
    role = "🧑 You" if msg.type == "human" else "🤖 AI"
    st.markdown(f"**{role}:** {msg.content}")









# from langchain_community.chat_message_histories import ChatMessageHistory
# from langchain_core.prompts import PromptTemplate
# from langchain_ollama import OllamaLLM

# # Load AI Model from Ollama (CPU fallback)
# llm = OllamaLLM(model="mistral", options={"num_gpu": 0})

# # Initialize Memory
# chat_history = ChatMessageHistory()

# # Improved AI Chat Prompt
# prompt = PromptTemplate(
#     input_variables=["chat_history", "question"],
#     template="""
# You are a helpful AI assistant. Here is the previous conversation between the user and the AI:
# {chat_history}

# Now the user asks:
# User: {question}
# AI:"""
# )

# # Function to run AI chat with memory
# def run_chain(question):
#     chat_history_text = "\n".join(
#         [f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages]
#     )

#     print("\n[DEBUG] Chat History:\n", chat_history_text)  # optional

#     response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))

#     chat_history.add_user_message(question)
#     chat_history.add_ai_message(response)

#     return response

# # Interactive CLI Chatbot
# print("\n AI Chatbot with Memory")
# print("Type 'exit' to stop.")

# while True:
#     user_input = input("\n You: ")
#     if user_input.lower() == 'exit':
#         print("\n  Goodbye!")
#         break
#     ai_response = run_chain(user_input)
#     print(f"\n AI: {ai_response}")




# from langchain_ollama import OllamaLLM

# # Load AI Model from Ollama
# llm = OllamaLLM(model="mistral")

# print("\nWelcome to your AI Agent! Ask me anything.")
# while True:
#     question = input("Your Question (or type 'exit' to stop): ")
#     if question.lower() == 'exit':
#         print("Exiting the AI Agent. Goodbye!")
#         break
#     response = llm.invoke(question)
#     print("\nAI Response:", response)
