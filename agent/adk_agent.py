from google.adk import Agent
from agent.prompts import system_prompt
from store.tools import search_products, view_product, execute_purchase

def build_agent(mandate):
    """
    Google ADK agent.
    NOTE: ADK Agent is a strict Pydantic model.
    """

    agent = Agent(
        name="ap2_intent_agent",
        instructions=system_prompt(mandate),
        tools=[
            search_products,
            view_product,
            execute_purchase,
            ],
    )

    return agent
