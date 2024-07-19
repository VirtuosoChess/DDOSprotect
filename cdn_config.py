import requests
from config import API_BASE_URL, CDN_ENDPOINT
from utils.api_request import make_request

def configure_cdn(api_key, site_url):
    endpoint = f"{API_BASE_URL}{CDN_ENDPOINT}"
    data = {
        "api_key": api_key,
        "site_url": site_url
    }
    response = make_request("POST", endpoint, data)
    if response.status_code == 200:
        print("CDN configuration completed successfully.")
    else:
        raise Exception("Failed to configure CDN.")
