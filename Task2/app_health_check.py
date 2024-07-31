import requests
import logging


URL = "https://active-users-react-app.vercel.app/"
# URL ="https://web-rtc-testing.vercel.app/" 
LOG_FILE = "app_health.log"

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_application_health():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            logging.info(f"Application is UP. Status code: {response.status_code}")
        else:
            logging.warning(f"Application is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Application is DOWN. Error: {e}")

if __name__ == "__main__":
    check_application_health()

