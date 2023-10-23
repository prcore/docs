import requests
from requests import Response

BASE_URL = "http****" # Please change this to your local instance address
API_TOKEN = "UaJW0QvkMA1cVnOXB89E0NbLf3JRRoHwv2wWmaY5v=QYpaxr1UD9/FupeZ85sa2r"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}
REQUEST_HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}
PROJECT_ID = 26


def get_project(project_id) -> Response:
    # Get the project definition
    url = f"{BASE_URL}/project/{project_id}"
    response = requests.get(url, headers=HEADERS)
    return response


def main():
    print("\nStaring the client...\n")

    try:
        # Get the project status
        print("Getting the project status...")
        i = 0
        while True:
            response = get_project(PROJECT_ID)
            if response.status_code != 200:
                print(f"[{i:08d}] = Error: {response.text}")
            else:
                project_status = response.json()["project"]["status"]
                print(f"[{i:08d}] = Project status: {project_status}")
            i += 1
    except KeyboardInterrupt:
        print("Interrupted by user\n")

    print("Done!\n")


if __name__ == "__main__":
    main()
