import requests
import sys
import json
from datetime import datetime

def log_error(endpoint, error):
    with open("error_log.txt", "a") as f:
        f.write(f"{datetime.now()} | {endpoint} | {error}\n")

def debug_api(endpoint):
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        print("✅ API request successful")
        print(f"ℹ️ Status Code: {response.status_code}")
        try:
            print("📄 Response:", json.dumps(response.json(), indent=2))
        except json.JSONDecodeError:
            print("📄 Response:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        log_error(endpoint, e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python debugger.py <API_ENDPOINT>")
    else:
        debug_api(sys.argv[1])
