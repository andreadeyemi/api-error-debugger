import requests
import datetime

def log_error(error_type, endpoint, message, code, trace_id):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {error_type} at {endpoint}\nDetails: {{\"message\": \"{message}\", \"code\": \"{code}\", \"trace_id\": \"{trace_id}\"}}\n"
    with open("error_log.txt", "a") as f:
        f.write(log_entry)

def test_api_endpoint(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            trace_id = response.headers.get("X-Trace-Id", "trace_" + datetime.datetime.now().strftime("%H%M%S"))
            log_error(f"ERROR {response.status_code}", url, "Unexpected status code", response.status_code, trace_id)
            print(f"⚠️ Error: Received status code {response.status_code}")
        else:
            print(f"✅ Success: {url} returned 200")
    except requests.exceptions.RequestException as e:
        trace_id = "trace_" + datetime.datetime.now().strftime("%H%M%S")
        log_error("ERROR 500", url, str(e), "E500X", trace_id)
        print(f"❌ Exception: {e}")

if __name__ == "__main__":
    test_api_endpoint("https://api.example.com/data")
