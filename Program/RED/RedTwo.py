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

# Function to extract only the SECOND red alliance team (Red 2)
def extract_second_red_team(matches):
    red_matches = {}
    sorted_matches = sorted(matches, key=lambda m: m.get('match_number', 0))

    for match in sorted_matches:
        match_number = match.get('match_number')
        if match_number is None:
            continue

        red_teams = match.get('alliances', {}).get('red', {}).get('team_keys', [])

        # Ensure there are at least two red teams
        if len(red_teams) > 1:
            second_red_team = red_teams[1][3:] if red_teams[1].startswith("frc") else red_teams[1]
            red_matches[str(match_number)] = {
                "match_number": str(match_number),
                "team": {"number": second_red_team, "color": "red"}
            }

    return {"Red 2": red_matches}  # Wrap in "Red 2" key

# Function to save red alliance data to a JSON file
def save_matches_to_file(matches_data, filename="RedTwo.json"):
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
        red_alliance_data = extract_second_red_team(matches)
        save_matches_to_file(red_alliance_data)  # Saves to "RedTwo.json"

if __name__ == "__main__":
    main()
