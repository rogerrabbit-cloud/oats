import requests

BASE_URL = "http://your-api-url"  # Replace with the actual base URL

def scan_network():
    """Scans the network by calling the /scan endpoint."""
    response = requests.get(f"{BASE_URL}/scan")
    if response.status_code == 200:
        return response.json()  # Return the scan results
    else:
        raise Exception(f"Failed to scan network: {response.status_code} {response.text}")

def kick_user(user_id):
    """Kicks a user by calling the /kick endpoint."""
    response = requests.post(f"{BASE_URL}/kick", json={"user_id": user_id})
    if response.status_code == 200:
        return response.json()  # Return confirmation of the kick
    else:
        raise Exception(f"Failed to kick user: {response.status_code} {response.text}")

# Example usage:
if __name__ == "__main__":
    try:
        scan_results = scan_network()
        print("Scan Results:", scan_results)
        
        # Example of kicking a user
        user_id_to_kick = "example_user_id"  # Replace with actual user ID
        kick_response = kick_user(user_id_to_kick)
        print("Kick Response:", kick_response)
    except Exception as e:
        print("Error:", e)