import json
import pprint
import requests
import sseclient

BASE_URL = "https://prcore.chaos.run" 
PROJECT_ID = 1
URL = f"{BASE_URL}/project/{PROJECT_ID}/streaming/result"
HEADERS = {
  "Authorization": "Bearer UaJW0QvkMA1cVnOXB89E0NbLf3JRRoHwv2wWmaY5v=QYpaxr1UD9/FupeZ85sa2r"
}


def with_requests(url, headers):
    # Get a streaming response for the given event feed using requests.
    return requests.get(url, stream=True, headers=headers)


response = with_requests(URL, HEADERS)
client = sseclient.SSEClient(response)

print("Waiting for events...")

"""
Please note that the word `event` here is the `E` from `SSE`, 
not the `event` in the business processing perspective.
The data of our `event` is in the `event.data` list.
"""

for event in client.events():
    if event.event == "ping":
      continue
    print(f"Received message: {event.event}")
    print(f"ID: {event.id}")
    print(f"Data type: {type(json.loads(event.data))}")
    print(f"Length: {len(json.loads(event.data))}")
    print("-" * 24)

print("Done!")