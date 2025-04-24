# GOOGLE PLACES API (NEW) CREDS
GOOGLE_API_KEY = "<API_KEY>"
GOOGLE_PLACES_URL = "https://places.googleapis.com/v1/places:searchText"
MAPS_HEADERS = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": GOOGLE_API_KEY,
    "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress,places.internationalPhoneNumber,places.websiteUri"
}

# WHATSAPP VALIDATION API CREDS
WHATSAPP_VAL_ENDPOINT = "whatsapp132.p.rapidapi.com"
WHATSAPP_VAL_HEADER = {
        'x-rapidapi-key': "<API_KEY>",
        'x-rapidapi-host': "whatsapp132.p.rapidapi.com",
        'Content-Type': "application/json"
    }