# 🧠 AI Chatbot with Memory

A conversational AI chatbot built with Streamlit and LangChain that maintains conversation history and provides intelligent responses using the Mistral model via Ollama.

## ✨ Features

- **Conversational Memory**: The chatbot remembers previous conversations and maintains context
- **Streamlit Web Interface**: Beautiful and intuitive web-based chat interface
- **LangChain Integration**: Built with LangChain for robust AI interactions
- **Ollama Support**: Uses Ollama to run the Mistral model locally
- **Real-time Chat**: Interactive chat experience with immediate responses
- **Error Handling**: Graceful error handling for model loading and API calls

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed on your system
2. **Ollama** installed and running locally
3. **Mistral model** downloaded in Ollama

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jaysuryawanshi65/basic_ai_agent.git
   cd basic_ai_agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install and setup Ollama**
   - Download Ollama from [https://ollama.ai](https://ollama.ai)
   - Install and start Ollama
   - Pull the Mistral model:
     ```bash
     ollama pull mistral
     ```

4. **Run the application**
   ```bash
   streamlit run basic_agent.py
   ```

5. **Open your browser**
   - Navigate to `http://localhost:8501`
   - Start chatting with your AI assistant!

## 🛠️ Usage

1. **Start a conversation**: Type your question in the text input field
2. **Send messages**: Click the "Send" button or press Enter
3. **View history**: All conversation history is displayed below the chat interface
4. **Context awareness**: The AI remembers previous messages and maintains conversation context

## 📁 Project Structure

```
basic_ai_agent/
├── basic_agent.py      # Main application file
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 Configuration

The application uses the following default settings:
- **Model**: Mistral (via Ollama)
- **GPU**: Disabled (CPU mode for compatibility)
- **Memory**: Session-based chat history

You can modify these settings in `basic_agent.py`:
- Change the model by modifying the `model="mistral"` parameter
- Enable GPU by setting `"num_gpu": 1` in the options
- Customize the prompt template for different AI personalities

## 🐛 Troubleshooting

### Common Issues

1. **"Failed to load model" error**
   - Ensure Ollama is running: `ollama serve`
   - Verify Mistral model is installed: `ollama list`
   - Pull the model if missing: `ollama pull mistral`

2. **Streamlit not starting**
   - Check if port 8501 is available
   - Try running: `streamlit run basic_agent.py --server.port 8502`

3. **Import errors**
   - Verify all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Jay Suryawanshi**
- GitHub: [@jaysuryawanshi65](https://github.com/jaysuryawanshi65)
- Email: suryavanshijay65@gmail.com

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the web framework
- [LangChain](https://langchain.com/) for AI/LLM orchestration
- [Ollama](https://ollama.ai/) for local model inference
- [Mistral AI](https://mistral.ai/) for the language model 