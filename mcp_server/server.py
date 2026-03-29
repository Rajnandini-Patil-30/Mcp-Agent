from fastapi import FastAPI

app = FastAPI()

@app.get("/places")
def get_places():
    return {
        "city": "Pune",
        "places": [
            "Shaniwar Wada",
            "Aga Khan Palace",
            "Sinhagad Fort"
        ]
    }