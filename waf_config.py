import requests
from config import API_BASE_URL, WAF_ENDPOINT
from utils.api_request import make_request

def setup_waf(api_key, site_url):
    endpoint = f"{API_BASE_URL}{WAF_ENDPOINT}"
    data = {
        "api_key": api_key,
        "site_url": site_url
    }
    response = make_request("POST", endpoint, data)
    if response.status_code == 200:
        print("WAF setup completed successfully.")
    else:
        raise Exception("Failed to setup WAF.")
