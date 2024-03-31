# import requests
# import sys


# res = requests.get(url="https://dummyjson.com/products")
# if res.status_code == 200:
#     print(f"response is ok {res.json()}")


import requests

# Define the base URL of the API you want to test
BASE_URL = "https://dummyjson.com/products"

# Define a list of payloads to fuzz the API with
PAYLOADS = [
    "",  # Empty payload
    "'; DROP TABLE users;",  # SQL injection payload (example)
    "invalid_input",  # Invalid input payload
    # Add more payloads as needed
]


def fuzz_api(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    print(f"Fuzzing {url}")
    for payload in PAYLOADS:
        try:
            response = requests.get(url, params={"input": payload})
            # Process the response here (e.g., check status code, response content, etc.)
            print(
                f"Payload: {payload}, Status Code: {response.status_code}, Response: {response.text}"
            )
        except requests.RequestException as e:
            print(f"Error making request: {e}")


def main():
    # Define endpoints to fuzz
    endpoints = [1, 2, 3]

    # Fuzz each endpoint
    for endpoint in endpoints:
        fuzz_api(endpoint)


if __name__ == "__main__":
    main()
