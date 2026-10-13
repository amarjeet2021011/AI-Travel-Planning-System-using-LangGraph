from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()


# https://www.tavily.com/ 
# Signup and login, On dashboard- > under api keys you will see the default key.
# Use that or click on + to create new one. Then save it in .env file

_client = None


def get_client():
    global _client
    if _client is None:
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            raise RuntimeError("TAVILY_API_KEY is not set. Add it to .env or Streamlit secrets.")
        _client = TavilyClient(api_key=api_key)
    return _client

# test it
#################################
# response = client.search(
    # query="Best hotels in Dubai"
# )

# print(response)

####################################



def tavily_search(query):
    response = get_client().search(
        query=query,
        max_results=5
    )

    results = []

    for i, r in enumerate(response["results"], 1):
        title   = r.get("title", "Unknown")
        url     = r.get("url", "")
        snippet = r.get("content", "").strip()
        # Keep only the first 300 characters to avoid wall-of-text
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    return "\n\n".join(results)
    
    
    
