import requests
import json
import os

# Define the API endpoint and your event key
api_url = "https://www.thebluealliance.com/api/v3"
event_key = "2025inmis"
auth_key = "LPBFcLNYuYkJhRemUEfXyXNCz8qLHLyIGO7LtKQHY25vzayHqelEodBQdZeJCFrq"

# Define the headers with your authentication key
headers = {
    "X-TBA-Auth-Key": auth_key
}

# Function to get match schedule
def get_match_schedule(event_key):
    response = requests.get(f"{api_url}/event/{event_key}/matches", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve matches: {response.status_code}")
        return None

# Function to extract only blue alliance teams
def extract_blue_alliance(matches):
    blue_matches = {}
    sorted_matches = sorted(matches, key=lambda m: m.get('match_number', 0))

    for match in sorted_matches:
        match_number = match.get('match_number')
        if match_number is None:
            continue

        blue_teams = match.get('alliances', {}).get('blue', {}).get('team_keys', [])
        teams = [{"number": team[3:], "color": "blue"} for team in blue_teams if team.startswith("frc")]

        blue_matches[str(match_number)] = {
            "match_number": str(match_number),
            "teams": teams
        }

    return {"Blue 1": blue_matches}  # Wrap in "Blue 1" key

# Function to save blue alliance data to a JSON file
def save_matches_to_file(matches_data, filename="BlueOne.json"):
    try:
        file_path = os.path.join(os.getcwd(), filename)  # Save in current directory
        with open(file_path, "w") as file:
            json.dump(matches_data, file, indent=4)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print("Error saving data:", e)

# Main function
def main():
    matches = get_match_schedule(event_key)
    if matches:
        blue_alliance_data = extract_blue_alliance(matches)
        save_matches_to_file(blue_alliance_data)  # Saves to "BlueOne.json"

if __name__ == "__main__":
    main()
