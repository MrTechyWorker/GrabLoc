# Places Search API with WhatsApp Validation

This FastAPI application provides an API endpoint to search for places using Google Places API and validates if their phone numbers are registered on WhatsApp.

## Features

- Search places using Google Places API
- Validate phone numbers against WhatsApp
- Returns place details including name, address, phone number, website, and WhatsApp status

## Setup

1. Install the required dependencies:
```bash
uv sync
```

2. Run the application:
```bash
uvicorn main:app --reload
```
3. Run the application in cloud background:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
4. Run the application in cloud background:
```bash
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
```
The server will start at `http://localhost:8000`

## API Usage

### Search Places

**Endpoint:** `/search`
**Method:** POST
**Content-Type:** text/plain

Example request using curl:
```bash
curl -X POST \
  http://localhost:8000/search \
  -H 'Content-Type: text/plain' \
  -d 'restaurants in new york'
```

Example Response:
```json
{
  "places": [
    {
      "id": "example_id",
      "displayName": "Sample Restaurant",
      "formattedAddress": "123 Example St, New York, NY 10001",
      "internationalPhoneNumber": "+12125551234",
      "websiteUri": "https://example.com",
      "isInWhatsapp": true
    }
  ]
}
```

## Environment Variables

The application uses the following API keys (configured in `statis_vars.py`):
- Google Places API Key
- RapidAPI Key for WhatsApp validation
