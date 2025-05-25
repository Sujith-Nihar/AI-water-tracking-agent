import asyncio
import threading

# Ensure an event loop exists for the current thread (Streamlit doesn't set one)
if threading.current_thread() is not threading.main_thread() or not asyncio.get_event_loop_policy().get_event_loop():
    asyncio.set_event_loop(asyncio.new_event_loop())


import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY= os.getenv("GOOGLE_API_KEY")
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

# llm=ChatOpenAI(api_key=OPEN_AI_KEY, model="gpt-4", temperature=0.5)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

class WaterIntakeAgent:

    def __init__(self):
        self.history=[]

    
    def analyze_intake(self, intake_ml):

        prompt = f"""
        You are a hyderation specialized assistant, Only provide what is asked in 2 to 4 lines, no unncessary details. The user has consumed {intake_ml} ml of water today, 
        Provide the user's hydration status and suggest if they need to drink more.
            """

        response = llm.invoke([HumanMessage(content=prompt)])

        return response.content



if __name__ == '__main__':

    agent = WaterIntakeAgent()
    intake = 1500
    feedback = agent.analyze_intake(intake)
    print(f"Hydration status : {feedback}")
