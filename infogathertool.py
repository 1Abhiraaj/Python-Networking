import requests
import socket
import json

# Prompt the user for a URL
url = input("Enter a URL: ")

# Check if the input is empty
if not url:
    print("URL cannot be empty.")
    exit(1)

try:
    # Send an HTTPS GET request to the URL
    req = requests.get("https://" + url)
    req.raise_for_status()  # Raise an exception if the request is not successful

    # Print the headers of the HTTP response
    print("\n" + str(req.headers))

    # Resolve the IP address of the URL
    gethostby_ = socket.gethostbyname(url)
    print("\nThe IP address of " + url + " is " + gethostby_ + "\n")

    # Send an HTTPS GET request to ipinfo.io to get location information based on the IP address
    req_tow = requests.get("https://ipinfo.io/" + gethostby_ + "/json")
    resp_ = req_tow.json()  # Parse the JSON response

    # Print location information
    print("Location: " + resp_["loc"])
    print("Region: " + resp_["region"])
    print("City: " + resp_["city"])
    print("Country: " + resp_["country"])

except requests.exceptions.RequestException as e:
    print("An error occurred while making the request:", e)
except socket.gaierror:
    print("Unable to resolve the IP address for the provided URL.")
except json.JSONDecodeError:
    print("Error parsing JSON response from ipinfo.io.")
except KeyError:
    print("Key not found in JSON response from ipinfo.io.")
except Exception as e:
    print("An error occurred:", e)




'''import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

req = requests.get("https://" + sys.argv[1])
print("\n" + str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1])
print("\n The ip address of " + sys.argv[1] + " is " + gethostby_ + "\n")

#ipinfo.in

req_tow = requests.get("https://ipinfo.io/" + gethostby_ + "/json")
resp_ = json.loads(req_tow.text)

print("Location: " + resp_["loc"])
print("Region: " + resp_["region"])
print("City: " + resp_["city"])
print("Country: " + resp_["country"])'''

