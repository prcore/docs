import json
import pprint
import requests
from requests import Response
from time import sleep

# Change this to your own event log file
EVENT_LOG_FILE = "/home/zhaosi/Sites/PrCore/static/download/bpic2012-CSV.zip"
TEST_FILE = "/home/zhaosi/Sites/PrCore/static/download/bpic2012-ongoing-CSV.zip"

BASE_URL = "http://localhost:8001"
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
    files = [
        ("file", ("bpic2012-CSV.zip", open(EVENT_LOG_FILE, "rb"), "application/zip")),
        ("test", ("bpic2012-ongoing-CSV.zip", open(TEST_FILE, "rb"), "application/zip"))
    ]
    response = requests.post(url, files=files, headers=HEADERS, data={"separator": ","})
    return response


def set_columns_definition(event_log_id) -> Response:
    # Set the columns definition for the uploaded file.
    url = f"{BASE_URL}/event_log/{event_log_id}"
    data = {
        "columns_definition": {
            "Case ID": "CASE_ID",
            "start_time": "START_TIMESTAMP",
            "end_time": "END_TIMESTAMP",
            "AMOUNT_REQ": "NUMBER",
            "REG_DATE": "DATETIME",
            "Activity": "ACTIVITY",
            "Resource": "RESOURCE"
        }
    }
    response = requests.put(url, json=data, headers=REQUEST_HEADERS)
    return response


def create_project(event_log_id) -> Response:
    # Create a project with the definition
    url = f"{BASE_URL}/project"
    data = {
        "event_log_id": event_log_id,
        "positive_outcome": [
            [
                {
                    "column": "Activity",
                    "operator": "EQUAL",
                    "value": "A_APPROVED"
                }
            ]
        ],
        "treatment": [
            [
                {
                    "column": "Activity",
                    "operator": "EQUAL",
                    "value": "O_SENT_BACK"
                }
            ]
        ]
    }
    response = requests.post(url, json=data, headers=REQUEST_HEADERS)
    return response


def get_result(project_id, result_key) -> Response:
    # Get the result of the project
    url = f"{BASE_URL}/project/{project_id}/result/{result_key}"
    response = requests.get(url, headers=HEADERS)
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

        # Set the columns definition
        print("Setting the columns definition...")
        response = set_columns_definition(event_log_id)
        response.raise_for_status()
        print("The columns definition has been set!\n")

        # Create the project
        print("Creating the project...")
        response = create_project(event_log_id)
        response.raise_for_status()
        project_id = response.json()["project"]["id"]
        result_key = response.json()["result_key"]
        print(f"Project {project_id} has been created!\n")

        # Get the result
        print("Getting the project status...\n")
        i = 1
        while True:
            response = get_result(project_id, result_key)
            response.raise_for_status()
            cases = response.json()["cases"]

            if cases:
                break

            project_status = response.json()["project_status"]
            expected_plugins = response.json()["expected_plugins"]
            finished_plugins = response.json()["finished_plugins"]

            if not finished_plugins:
                print(f"[{i:03d}] - Now the project status is {project_status}")
            else:
                print(f"[{i:03d}] - We have got results from {', '.join(finished_plugins)}, "
                      f"and we are still waiting for {', '.join(list(set(expected_plugins) - set(finished_plugins)))}.")

            sleep(1)
            i += 1
        
        print("\nWe have got all results!\n")
        cases = response.json()["cases"]

        print("Here is the first case:\n")
        pprint.pprint(cases[list(cases.keys())[0]])
    except KeyboardInterrupt:
        print("Interrupted by user\n")
    except Exception as e:
        print(f"Error: {e}\n")

    print("\nDone!\n")


if __name__ == "__main__":
    main()
