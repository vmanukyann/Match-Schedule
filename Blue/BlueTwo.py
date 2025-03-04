
import requests
import json

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

# Function to transform match data into the desired format with only Blue 2 team
def transform_matches_data(matches):
    output = {}
    # Sort matches by match_number (ascending)
    sorted_matches = sorted(matches, key=lambda m: m.get('match_number', 0))

    for match in sorted_matches:
        match_number = match.get('match_number')
        if match_number is None:
            continue
        match_key = str(match_number)
        teams = []
        alliances = match.get('alliances', {})

        # Process the blue alliance teams
        blue_teams = alliances.get('blue', {}).get('team_keys', [])
        if len(blue_teams) >= 2:
            # Get the second team in the blue alliance (Blue 2)
            blue2_team = blue_teams[1]
            blue2_team_number = blue2_team[3:] if blue2_team.startswith("frc") else blue2_team
            teams.append({"number": blue2_team_number, "color": "blue"})

        output[match_key] = {
            "match_number": match_key,
            "teams": teams
        }
    return output

# Function to save match data to a JSON file
def save_matches_to_file(matches_data, filename="blue2_match_schedule.json"):
    try:
        with open(filename, "w") as file:
            json.dump(matches_data, file, indent=4)
        print(f"Data saved to {filename}")
    except Exception as e:
        print("Error saving data:", e)

# Main function
def main():
    matches = get_match_schedule(event_key)
    if matches:
        # Transform the data into the desired format
        transformed_matches = transform_matches_data(matches)
        # Optionally, print the transformed data
        #print(json.dumps(transformed_matches, indent=4))
        # Save the transformed data to blue2_match_schedule.json
        save_matches_to_file(transformed_matches)

if __name__ == "__main__":
    main()
