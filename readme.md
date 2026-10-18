
# Talk to Your Data: AI Powered DataFrame Agent

An AI agent that answers questions about Twitter analytics data in plain English using LangChain and Google Gemini.

## What it does

- You type a question like "Which weekday has the highest engagement rate?"
- The agent thinks, writes Pandas code automatically, runs it and returns the answer
- No need to write any code or know Pandas

## How it works

1. User types a question in the Gradio web interface
2. LangChain agent receives the question
3. Agent writes Pandas code to answer it
4. Code runs on the Twitter dataset
5. Answer is returned to the user

## Tools and Technologies

- Python
- LangChain
- Google Gemini API
- Pandas
- Gradio
- python-dotenv

## Dataset

Twitter Analytics dataset with 1000 tweets and 24 columns including likes, retweets, impressions, engagement rate, hashtag clicks and more.

## How to run

1. Clone this repository
2. Install dependencies: pip install -r requirements.txt
3. Create a .env file and add your Gemini API key: GOOGLE_API_KEY=your_key_here
4. Run: python app.py
5. Open http://127.0.0.1:7860 in your browser

## Sample questions you can ask

- What is the average number of likes?
- Which weekday has the highest engagement rate?
- Which hour of the day has the highest impressions?
- What is the total number of retweets?
- What is the top performing tweet by engagement rate?
