import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.llm_pick import pick_llm
from models.schema import AgentSchema



def curate_question(state: AgentSchema)-> AgentSchema:
    user_question = state.user_question
    llm = pick_llm("low")  # pick the appropriate LLM based on the level of the question
    response = llm.invoke(f"Curate the following question for SQL analysis: {user_question}")
    state.current_ques = response
    return state