from fastapi import FastAPI, Request, Response
import requests
import http.client
import json
from statis_vars import *
from helper_funs import validate_whatsapp_number

# Initialize the api connections
whatsapp_val_conn = http.client.HTTPSConnection(WHATSAPP_VAL_ENDPOINT)
app = FastAPI()

@app.post("/search")
async def search_places(request: Request):
    """
    Search for places using Google Places API and validate their phone numbers with WhatsApp API.
    Args:
        request (Request): The incoming request containing the search query.
    Returns:
        Response: The response containing the search results and WhatsApp validation status.
    """
    # Extract the text query from the request body
    text_query = (await request.body()).decode("utf-8").strip()

    if not text_query:
        return {"error": "Empty query"}

    response = requests.post(
        GOOGLE_PLACES_URL,
        headers=MAPS_HEADERS,
        json={"textQuery": text_query}
    )

    data = response.json()

    # Validate each phone number in the response to check if it's in WhatsApp
    for place in data.get("places", []):
        phone = place.get("internationalPhoneNumber")

        if phone:
            analysis = validate_whatsapp_number(num= phone, 
                                                conn= whatsapp_val_conn, 
                                                header= WHATSAPP_VAL_HEADER)
            place["isInWhatsapp"] = analysis


    return Response(
        content=json.dumps(data, indent=2),
        media_type="application/json",
        status_code=response.status_code
    )