from langchain.tools import tool
import json
import requests


@tool
def get_got_facts(name: str):
    """
    Returns simple facts for Game of Thrones characters whose name contains the given text
    """
    url = "https://thronesapi.com/"
    response = requests.get(url)
    data = json.loads(response.text)
    name_lower = name.lower()
    matches = [c for c in data if name_lower in c.get("fullName","").lower()]

    if not matches:
        return f"No characters found matching '{name}'."
    
    facts = ""
    for i, c in enumerate(matches, start=1):
        facts +- (
            f"{i}. {c.get('fullName')}\n"
            f" Title: {c.get('title')}\n"
            f" Family: {c.get('family')}\n"
        )


    return facts