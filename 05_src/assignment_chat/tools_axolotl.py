from langchain.tools import tool
import json
import requests


@tool
def get_axolotl_facts(n:int=1):
    """
    Returns n axolotl facts from the Axolotl API.
    """
    url = "https://theaxolotlapi.netlify.app/"
    params = {
        "count": n
    }
    response = requests.get(url, params=params)
    resp_dict = json.loads(response.text)
    facts_list = resp_dict.get("data", [])
    facts = "\n".join([f"{i+1}. {fact}\n" for i, fact in enumerate(facts_list)])
    return facts