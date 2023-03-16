import requests
from requests import Response
from time import sleep

# Change this to your own event log file
EVENT_LOG_FILE = "/home/zhaosi/Sites/PrCore/static/download/bpic2012-XES.zip"

BASE_URL = "https://prcore.chaos.run"
API_TOKEN = "UaJW0QvkMA1cVnOXB89E0NbLf3JRRoHwv2wWmaY5v=QYpaxr1UD9/FupeZ85sa2r"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}
REQUEST_HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}
PROJECT_ID = 28


def upload_file(file_path) -> Response:
    # Upload a file to the server.
    url = f"{BASE_URL}/event_log"
    files = [
        ("file", ("bpic2012-XES.zip", open(file_path, "rb"), "application/zip"))
    ]
    response = requests.post(url, files=files, headers=HEADERS)
    return response


def set_columns_definition(event_log_id) -> Response:
    # Set the columns definition for the uploaded file.
    url = f"{BASE_URL}/event_log/{event_log_id}"
    data = {
        "columns_definition": {
            "org:resource": "RESOURCE",
            "lifecycle:transition": "TRANSITION",
            "concept:name": "ACTIVITY",
            "time:timestamp": "TIMESTAMP",
            "case:REG_DATE": "DATETIME",
            "case:concept:name": "CASE_ID",
            "case:AMOUNT_REQ": "NUMBER"
        },
        "case_attributes": ["case:REG_DATE", "case:AMOUNT_REQ"],
        "fast_mode": False
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
                    "column": "concept:name",
                    "operator": "EQUAL",
                    "value": "A_APPROVED"
                }
            ]
        ],
        "treatment": [
            [
                {
                    "column": "concept:name",
                    "operator": "EQUAL",
                    "value": "O_SENT_BACK"
                }
            ]
        ]
    }
    response = requests.post(url, json=data, headers=REQUEST_HEADERS)
    return response


def get_project(project_id) -> Response:
    # Get the project definition
    url = f"{BASE_URL}/project/{project_id}"
    response = requests.get(url, headers=HEADERS)
    return response


def main():
    print("\nStaring the client...\n")

    try:
        # Upload the event log file
        print("Uploading the event log file...")
        response = upload_file(EVENT_LOG_FILE)
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
        PROJECT_ID = project_id
        print(f"Project {project_id} has been created!\n")

        # Get the project status
        print("Getting the project status...")
        i = 1
        while True:
            response = get_project(PROJECT_ID)
            project_status = response.json()["project"]["status"]
            if project_status == "TRAINED":
                break
            plugins = response.json()["project"]["plugins"]
            if plugins:
                plugin_statuses = ", ".join([plugin["status"] for plugin in plugins])
                print(f"[{i:03d}] Now the project status is {project_status}, and its plugins have statuses {plugin_statuses}")
            else:
                print(f"[{i:03d}] Now the project status is {project_status}")
            sleep(1)
            i += 1
        print("The project has been trained!\n")
    except KeyboardInterrupt:
        print("Interrupted by user\n")

    print("Done!\n")


if __name__ == "__main__":
    main()
