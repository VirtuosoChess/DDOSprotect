import config
from utils.logger import setup_logger
from ddos_protection import enable_ddos_protection
from waf_config import setup_waf
from cdn_config import configure_cdn

logger = setup_logger()

def main():
    api_key = input("Enter your site API key: ")
    site_url = input("Enter your site URL: ")

    try:
        enable_ddos_protection(api_key, site_url)
        setup_waf(api_key, site_url)
        configure_cdn(api_key, site_url)
        logger.info("DDoS protection setup completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
