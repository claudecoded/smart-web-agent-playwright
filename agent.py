import os
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig

# Load environment variables from .env file
load_dotenv()

async def main():
    # Configure the browser to run in stealth/persistent mode to bypass basic anti-bot systems
    browser_config = BrowserConfig(
        headless=False,  # Running with UI helps bypass anti-bot fingerprinting
        disable_security=True,
        extra_chromium_args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-infobars"
        ]
    )
    
    browser = Browser(config=browser_config)

    # Initialize the AI model (GPT-4o is recommended for complex UI layouts)
    llm = ChatOpenAI(model="gpt-4o", temperature=0.0)

    # Define the mission for the AI Agent
    task_description = (
        "Go to amazon.com, search for 'wireless mouse', "
        "and extract the title and price of the first 3 results."
    )

    # Instantiate the AI Agent with the browser and the task
    agent = Agent(
        task=task_description,
        llm=llm,
        browser=browser
    )

    print(f"Starting AI Agent task: '{task_description}'...")
    
    # Run the agent and capture the final execution history
    history = await agent.run()
    
    print("\nTask Completed successfully!")
    print("Final Result Summary:")
    print(history.final_result())

    # Ensure the browser instance is properly closed
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
