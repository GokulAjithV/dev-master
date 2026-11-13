# Langgraph = steps (nodes) + shared state + rules for what runs next (edges and conditional edges)
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

class State(TypedDict):
    attempts: int 
    found: bool

def search(state: State) -> dict:
    attempts = state["attempts"] + 1
    found = attempts == 3 # pretending 3rd search finds the answer
    print(f"search attempt - {attempts}: found={found}")
    return {"attempts": attempts, "found": found}

def report(state: State) -> dict:
    print(f"report: done after {state['attempts']} attempts")
    return {}

def what_next(state: State) -> str:
    if state["found"] or state["attempts"] >= 5:
        return "report"
    return "search"

graph = StateGraph(State)
graph.add_node("search", search)
graph.add_node("report", report)
graph.add_edge(START, "search")
graph.add_conditional_edges("search", what_next, ["search", "report"])
graph.add_edge("report", END)

app = graph.compile()
final_state = app.invoke({"attempts": 0, "found": False})
print("final state: ", final_state)
