import json
import pprint
import requests
import sseclient
from requests import Response
from time import sleep

# Change this to your own event log file
EVENT_LOG_FILE = "./bpic2017-XES.zip"

BASE_URL = "https://prcore.chaos.run" 
API_TOKEN = "UaJW0QvkMA1cVnOXB89E0NbLf3JRRoHwv2wWmaY5v=QYpaxr1UD9/FupeZ85sa2r"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}
REQUEST_HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}
PROJECT_ID = None


def upload_file(file_path) -> Response:
    # Upload a file to the server.
    url = f"{BASE_URL}/event_log"
    files = [
        ("file", ("bpic2017-XES.zip", open(file_path, "rb"), "application/zip"))
    ]
    response = requests.post(url, files=files, headers=HEADERS)
    return response


def set_columns_definition(event_log_id) -> Response:
    # Set the columns definition for the uploaded file.
    url = f"{BASE_URL}/event_log/{event_log_id}"
    data = {
        "columns_definition": {
            "concept:name": "ACTIVITY",
            "lifecycle:transition": "TRANSITION",
            "time:timestamp": "TIMESTAMP",
            "case:concept:name": "CASE_ID"
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
                    "column": "concept:name",
                    "operator": "EQUAL",
                    "value": "O_Accepted"
                }
            ]
        ],
        "treatment": [
            [
                {
                    "column": "concept:name",
                    "operator": "EQUAL",
                    "value": "O_Returned"
                }
            ]
        ],
        "additional_info": {
            "plugin-causallift-resource-allocation": {
                "available_resources": ["Resource_A", "Resource_B", "Resource_C", "Resource_D", "Resource_E", "Resource_F", "Resource_G", "Resource_H", "Resource_I", "Resource_J", "Resource_K", "Resource_L", "Resource_M", "Resource_N", "Resource_O", "Resource_P", "Resource_Q", "Resource_R", "Resource_S", "Resource_T", "Resource_U", "Resource_V", "Resource_W", "Resource_X", "Resource_Y", "Resource_Z"],
                "treatment_duration": "1h"
            }
        }
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
        PROJECT_ID = project_id
        print(f"Project {project_id} has been created!\n")

        # Get the project status
        print("Getting the project status...")
        i = 1
        while True:
            response = get_project(project_id)
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

        # Start the simulation
        print("Starting the simulation...")
        response = start_simulation(project_id)
        response.raise_for_status()
        print("The simulation has been started!\n")

        # Get the streaming response
        print("Now we are going to get the streaming response...")
        printing_streaming_response(project_id)
    except KeyboardInterrupt:
        print("Interrupted by user\n")
    except Exception as e:
        print(f"Error: {e}\n")
    finally:
        PROJECT_ID and stop_simulation(PROJECT_ID)

    print("Done!\n")


if __name__ == "__main__":
    main()
