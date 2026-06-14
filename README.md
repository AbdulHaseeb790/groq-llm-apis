# Groq LLM API Learning Project

A hands-on project for learning how to work with Large Language Model (LLM) APIs using the Groq API and LLaMA 3.3 70B.

## Overview

This repository covers the fundamentals of interacting with modern AI models, handling errors, managing conversations, tracking token usage, and building simple AI-powered applications.

## Topics Covered

### Basic API Calls
Learn how to send prompts to an LLM and receive responses.

### Multi-Turn Conversations
Maintain chat history to create conversational AI experiences.

### Error Handling
Handle common API-related issues such as:
- Invalid API keys
- Rate limits
- Network failures
- Bad requests

### Retry Logic
Implement automatic retries with exponential backoff when rate limits occur.

### Token Usage Tracking
Monitor prompt and completion token usage to understand API costs.

### CLI Chatbot
Build a simple command-line chatbot using Groq's API.

## Project Structure

```text
.
├── first_api_call.py
├── chat_history.py
├── error-handling
│   ├── basic_errors.py
│   ├── retry.py
│   ├── cost_tracking.py
│   └── chatbot.py
└── README.md
Tech Stack
Python
Groq API
LLaMA 3.3 70B Versatile
python-dotenv
Installation
pip install groq python-dotenv
Environment Variables


This project was built to understand:

How LLM APIs work
Prompt-response workflows
Chat history management
Production-style error handling
Retry strategies
Token tracking
Building AI-powered applications
Future Improvements
Streaming responses
System prompts
Function calling
Tool use
RAG (Retrieval-Augmented Generation)
AI Agents
LangChain integration
Web-based chatbot interface
