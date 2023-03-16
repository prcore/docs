import json
import pprint
import requests
from requests import Response
from time import sleep
from zipfile import ZipFile

# Change this to your own event log file
EVENT_LOG_FILE = "/home/zhaosi/Sites/PrCore/static/download/bpic2012-CSV.zip"
TEST_FILE = "/home/zhaosi/Sites/PrCore/static/download/bpic2012-ongoing-CSV.zip"

BASE_URL = "http://localhost:8000"
API_TOKEN = "UaJW0QvkMA1cVnOXB89E0NbLf3JRRoHwv2wWmaY5v=QYpaxr1UD9/FupeZ85sa2r"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}
REQUEST_HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}


def upload_file() -> Response:
    # Upload a file to the server.
    url = f"{BASE_URL}/event_log"

    file = open(EVENT_LOG_FILE, "rb")
    _ = ZipFile(file)
    file.seek(0)

    files = [
        ("file", ("bpic2012-CSV.zip", file, "application/zip")),
        ("test", ("bpic2012-ongoing-CSV.zip", open(TEST_FILE, "rb"), "application/zip"))
    ]
    response = requests.post(url, files=files, headers=HEADERS, data={"separator": ","})
    return response


def main():
    print("\nStaring the client...\n")

    try:
        # Upload the event log file
        print("Uploading the event log file...")
        response = upload_file()
        response.raise_for_status()
        event_log_id = response.json()["event_log_id"]
        print(f"Event log {event_log_id} has been uploaded!\n")
    except KeyboardInterrupt:
        print("Interrupted by user\n")
    except Exception as e:
        print(f"Error: {e}\n")

    print("\nDone!\n")


if __name__ == "__main__":
    main()
