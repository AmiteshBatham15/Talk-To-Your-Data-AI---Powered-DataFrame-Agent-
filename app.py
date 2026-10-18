from dotenv import load_dotenv
import os
import pandas as pd 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import gradio as gr       

load_dotenv()

df = pd.read_csv("Twitter.csv")

llm = ChatGoogleGenerativeAI(model = "gemini-3.8-flash", temperature = 0)

agent  = create_pandas_dataframe_agent(
    llm,
    df,
    verbose = True,
    allow_dangerous_code = True,
    handle_parsing_errors = True
)

def ask(question):
    try:
        time.sleep(5)
        result = agent.invoke(question)
        return result["output"]
    except Exception as e:
        return "Gemini rate limit reached. Please wait 1 minute and try again."
    
app = gr.Interface(
    fn = ask,
    inputs = gr.Textbox(label = "Ask your data"),
    outputs = gr.Textbox(label = "Answer"),
    title = "🐦 Twitter Data Analyst Agent",
    description="Ask any question about the Twitter dataset in plain English.",
    examples=[
        ["How many rows and columns are there?"],
        ["What is the average number of likes?"],
        ["Which weekday has the highest engagement rate?"],
        ["What is the total number of retweets?"],
        ["Which hour has the highest impressions?"]
    ],
    theme = gr.themes.Soft()
)    

app.launch()

