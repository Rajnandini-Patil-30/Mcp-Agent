from fastapi import FastAPI
from typing import Dict, List

app = FastAPI()

# Simulated maps data
CITY_PLACES: Dict[str, List[str]] = {
    "pune": ["Shaniwar Wada", "Aga Khan Palace", "Sinhagad Fort"],
    "mumbai": ["Gateway of India", "Marine Drive", "Elephanta Caves"],
    "delhi": ["India Gate", "Qutub Minar", "Red Fort"]
}

# Simulated database records
PLACE_DB = {
    "Shaniwar Wada": {
        "category": "Historical Fort",
        "timings": "8:00 AM - 6:30 PM",
        "ticket_price": "₹25",
        "best_for": "History lovers"
    },
    "Aga Khan Palace": {
        "category": "Museum / Heritage",
        "timings": "9:00 AM - 5:30 PM",
        "ticket_price": "₹20",
        "best_for": "Architecture and history"
    },
    "Sinhagad Fort": {
        "category": "Fort / Trek",
        "timings": "Open all day",
        "ticket_price": "Free",
        "best_for": "Trekking and scenic views"
    },
    "Gateway of India": {
        "category": "Monument",
        "timings": "Open all day",
        "ticket_price": "Free",
        "best_for": "Sightseeing"
    },
    "Marine Drive": {
        "category": "Promenade",
        "timings": "Open all day",
        "ticket_price": "Free",
        "best_for": "Evening visit"
    },
    "Elephanta Caves": {
        "category": "UNESCO Site",
        "timings": "9:00 AM - 5:00 PM",
        "ticket_price": "₹40",
        "best_for": "History and sculpture"
    }
}

@app.get("/get_top_places")
def get_top_places(city: str):
    places = CITY_PLACES.get(city.lower(), [])
    return {"city": city, "places": places}

@app.get("/get_place_details")
def get_place_details(place_name: str):
    details = PLACE_DB.get(place_name, {})
    return {"place_name": place_name, "details": details}