import json
import pprint
import requests
import sseclient
from requests import Response
from time import sleep

# Change this to your own event log file
EVENT_LOG_FILE = "/home/zhaosi/Sites/PrCore/static/download/bpic2012-CSV.zip"

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
        ("file", ("bpic2012-CSV.zip", open(file_path, "rb"), "application/zip"))
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
            ],
            [
                {
                    "column": "DURATION",
                    "operator": "LESS_THAN",
                    "value": "10 d"
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


def get_project(project_id) -> Response:
    # Get the project definition
    url = f"{BASE_URL}/project/{project_id}"
    response = requests.get(url, headers=HEADERS)
    return response


def start_simulation(project_id) -> Response:
    # Start the simulation
    url = f"{BASE_URL}/project/{project_id}/stream/start/simulating"
    response = requests.put(url, headers=HEADERS)
    return response


def stop_simulation(project_id) -> Response:
    # Stop the simulation
    url = f"{BASE_URL}/project/{project_id}/stream/stop"
    response = requests.put(url, headers=HEADERS)
    response.raise_for_status()
    print("The simulation has been stopped!")
    return response


def printing_streaming_response(project_id):
    # Get a streaming response for the given event feed using sseclient.
    response = requests.get(f"{BASE_URL}/project/{project_id}/stream/result", stream=True, headers=HEADERS)
    client = sseclient.SSEClient(response)

    print("Waiting for events...")

    for event in client.events():
        if event.event != "message":
            continue

        event_data = json.loads(event.data)
        first_event = event_data[0]
        prescriptions = first_event["prescriptions"]
        prescriptions_with_output = [prescriptions[p] for p in prescriptions if prescriptions[p]["output"]]

        if not prescriptions_with_output:
            continue

        print(f"Received message: {event.event}")
        print(f"ID: {event.id}")

        pprint.pprint(prescriptions_with_output, width=120)

        print("-" * 24)



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
        while True:
            response = get_project(PROJECT_ID)
            project_status = response.json()["project"]["status"]
            if project_status == "TRAINED":
                break
            plugins = response.json()["project"]["plugins"]
            if plugins:
                plugin_statuses = ", ".join([plugin["status"] for plugin in plugins])
                print(f"Now the project status is {project_status}. It's plugins have status {plugin_statuses}. Waiting for 5 seconds...")
            else:
                print(f"Now the project status is {project_status}. Waiting for 5 seconds...")
            sleep(0.1)
        print("The project has been trained!\n")

        # Start the simulation
        print("Starting the simulation...")
        response = start_simulation(PROJECT_ID)
        response.raise_for_status()
        print("The simulation has been started!\n")

        # Get the streaming response
        print("Now we are going to get the streaming response...")
        printing_streaming_response(PROJECT_ID)
    except KeyboardInterrupt:
        print("Interrupted by user\n")
    finally:
        print("Stopping the simulation...")
        PROJECT_ID and stop_simulation(PROJECT_ID)

    print("Done!\n")


if __name__ == "__main__":
    main()
