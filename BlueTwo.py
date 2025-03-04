import requests
import json
import sys
import os

# Define the API endpoint and your event key
api_url = "https://www.thebluealliance.com/api/v3"
event_key = "2025inmis"
auth_key = "API_KEY"

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

# Function to transform match data (modify this based on the purpose of the script)
def transform_matches_data(matches):
    output = {}
    sorted_matches = sorted(matches, key=lambda m: m.get('match_number', 0))

    for match in sorted_matches:
        match_number = match.get('match_number')
        if match_number is None:
            continue
        match_key = str(match_number)
        teams = []
        alliances = match.get('alliances', {})

        # Process blue alliance, focusing on Blue 2
        blue_teams = alliances.get('blue', {}).get('team_keys', [])
        if len(blue_teams) >= 2:
            team_number = blue_teams[1][3:] if blue_teams[1].startswith("frc") else blue_teams[1]
            teams.append({"number": team_number, "color": "blue"})

        output[match_key] = {
            "match_number": match_key,
            "teams": teams
        }
    return output

# Function to save match data to a JSON file
def save_matches_to_file(matches_data, directory, filename="BlueTwo.json"):
    try:
        file_path = os.path.join(directory, filename)
        with open(file_path, "w") as file:
            json.dump(matches_data, file, indent=4)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print("Error saving data:", e)

# Main function
def main():
    json_directory = sys.argv[1]  # Get the JSON directory passed from run_all_scripts.py

    matches = get_match_schedule(event_key)
    if matches:
        transformed_matches = transform_matches_data(matches)
        save_matches_to_file(transformed_matches, json_directory)

if __name__ == "__main__":
    main()
