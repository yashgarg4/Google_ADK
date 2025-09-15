"""
LinkedIn Post Generator Agent

This agent generates the initial LinkedIn post before refinement.
"""

from google.adk.agents.llm_agent import LlmAgent

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Initial Post Generator Agent
initial_post_generator = LlmAgent(
    name="InitialPostGenerator",
    model=GEMINI_MODEL,
    instruction="""You are a LinkedIn Post Generator.

    Your task is to create a LinkedIn post about whether the topic is given to you.
    
    ## STYLE REQUIREMENTS
    - Professional and conversational tone
    - Between 1000-1500 characters
    - NO emojis
    - NO hashtags
    - Show genuine enthusiasm
    
    ## OUTPUT INSTRUCTIONS
    - Return ONLY the post content
    - Do not add formatting markers or explanations
    """,
    description="Generates the initial LinkedIn post to start the refinement process",
    output_key="current_post",
)