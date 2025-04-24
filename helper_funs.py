import http.client
import json

def validate_whatsapp_number(num: str, conn: http.client.HTTPSConnection, header: dict) -> bool:

    """
    Validate a WhatsApp number using the WhatsApp API.
    Args:   
        num (str): The phone number to validate.
    Returns:
        bool: True if the number is valid, False otherwise.
    """
    
    val_num = "".join([i for i in num if i.isdigit()])
    payload = "{\"phone\":\"+" + val_num + "\",\"service_plan\":1}"

    conn.request("POST", "/open/phone/service-plan", payload, header)

    res = conn.getresponse()
    data = res.read()
    val = json.loads(data.decode("utf-8")).get("data").get("exists")

    return val