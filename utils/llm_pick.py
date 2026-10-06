from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env filecd..


def pick_llm(level: str):
    """
    Picks the appropriate LLM based on the specified level.

    Args:
        level (str): The level of the LLM to pick. Can be "basic", "intermediate", or "advanced".

    Returns:
        ChatGroq: The LLM instance to be used.
    """
    if level.lower() == "low":
        llm =  ChatGroq(model_name="openai/gpt-oss-20b", temperature=0)
    elif level.lower() == "medium":
        llm = ChatGroq(model_name="qwen/qwen3.8-27b", temperature=0)
    elif level.lower() == "high":
        llm = ChatGroq(model_name="openai/gpt-oss-120b", temperature=0)
    else:
        raise ValueError(f"Unsupported level: {level}")
    return llm


llm_obj = pick_llm("medium")  # Example usage, you can change the level as needed
print(llm_obj.invoke("What is the capital of France?")) # Example invocation, replace with your query