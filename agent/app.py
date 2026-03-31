import os
import requests
from fastapi import FastAPI, Query

app = FastAPI()

MCP_URL = os.environ.get("MCP_URL", "").rstrip("/")

def get_top_places(city: str):
    r = requests.get(f"{MCP_URL}/get_top_places", params={"city": city}, timeout=30)
    r.raise_for_status()
    return r.json()

def get_place_details(place_name: str):
    r = requests.get(f"{MCP_URL}/get_place_details", params={"place_name": place_name}, timeout=30)
    r.raise_for_status()
    return r.json()

@app.get("/")
def root():
    return {"message": "Multi-tool MCP agent is running"}

@app.get("/ask")
def ask(city: str = Query(..., description="City name")):
    top_places_data = get_top_places(city)
    places = top_places_data.get("places", [])

    if not places:
        return {
            "city": city,
            "answer": f"Sorry, I could not find any attractions for {city}."
        }

    detailed_results = []
    for place in places:
        details_data = get_place_details(place)
        details = details_data.get("details", {})
        detailed_results.append({
            "place": place,
            "category": details.get("category", "N/A"),
            "timings": details.get("timings", "N/A"),
            "ticket_price": details.get("ticket_price", "N/A"),
            "best_for": details.get("best_for", "N/A")
        })

    lines = [f"Top places to visit in {city.title()}:"]
    for item in detailed_results:
        lines.append(
            f"- {item['place']} ({item['category']}), timings: {item['timings']}, "
            f"ticket: {item['ticket_price']}, best for: {item['best_for']}"
        )

    return {
        "city": city,
        "places": detailed_results,
        "answer": "\n".join(lines)
    }