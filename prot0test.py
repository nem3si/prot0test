import asyncio
import requests
from py_mini_racer import py_mini_racer


Please enter the URL of the web page you want to test:
"""

# Define a test payload for prototype pollution
test_payload = {
    "__proto__": {
        "admin": True
    }
}

# Function to test for prototype pollution
def test_prototype_pollution(url):
    # Perform the test
    test_object = {}
    merge_objects(test_object, test_payload)

    # Check if the pollution was successful
    if test_object.get("admin"):
        print(f"Prototype pollution detected in {url}!")
        describe_findings(test_object)
    else:
        print(f"No prototype pollution detected in {url}.")

# Function to merge dictionaries (similar to dict.update())
def merge_objects(target, source):
    for key, value in source.items():
        target[key] = value

# Function to describe the findings
def describe_findings(test_object):
    print("Prototype pollution findings:")
    for key, value in test_object.items():
        print(f" - {key}: {value}")

# Display ASCII art and prompt for the web page URL
print(ascii_art)
url = input("Enter the URL of the web page to test: ")

# Asynchronous function to send a request and perform prototype pollution testing
async def send_request(url):
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
    javascript_code = response.text

    with py_mini_racer.MiniRacer() as ctx:
        ctx.eval(javascript_code)
        test_prototype_pollution(url)

# Run the script asynchronously
asyncio.run(send_request(url))
