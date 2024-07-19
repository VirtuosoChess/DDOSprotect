import requests
from config import API_BASE_URL, DDOS_PROTECTION_ENDPOINT
from utils.api_request import make_request

def enable_ddos_protection(api_key, site_url):
    endpoint = f"{API_BASE_URL}{DDOS_PROTECTION_ENDPOINT}"
    data = {
        "api_key": api_key,
        "site_url": site_url
    }
    response = make_request("POST", endpoint, data)
    if response.status_code == 200:
        print("DDoS protection enabled successfully.")
    else:
        raise Exception("Failed to enable DDoS protection.")
