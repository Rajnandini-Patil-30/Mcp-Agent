import requests

def call_mcp():
    url = "http://localhost:8000/places"
    response = requests.get(url)
    return response.json()

def agent_response(user_query):
    data = call_mcp()
    
    places = data["places"]

    return f"Top places in {data['city']} are: {', '.join(places)}"

if __name__ == "__main__":
    print(agent_response("Show places"))