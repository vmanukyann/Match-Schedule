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

# Define your subjective red team criteria
# For example, let's say you are looking for a red team with a specific team number (e.g., 'frc1234')
subjective_red_team_number = '1234'

# Function to get match schedule
def get_match_schedule(event_key):
    response = requests.get(f"{api_url}/event/{event_key}/matches", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve matches: {response.status_code}")
        return None

# Function to transform match data into the desired format with the subjective red team
def transform_matches_data(matches, subjective_team_number):
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

        # Process the red alliance teams
        red_teams = alliances.get('red', {}).get('team_keys', [])
        for team in red_teams:
            # Remove the "frc" prefix if present
            team_number = team[3:] if team.startswith("frc") else team
            # Check if this team matches the subjective condition (team number in this case)
            if team_number == subjective_team_number:
                teams.append({"number": team_number, "color": "red"})

        # Only include the match if we found the subjective red team
        if teams:
            output[match_key] = {
                "match_number": match_key,
                "teams": teams
            }

    return output

# Function to save match data to a JSON file
def save_matches_to_file(matches_data, filename="red_subjective_match_schedule.json"):
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
        # Transform the data into the desired format with the subjective red team
        transformed_matches = transform_matches_data(matches, subjective_red_team_number)
        # Save the transformed data to red_subjective_match_schedule.json
        save_matches_to_file(transformed_matches)

if __name__ == "__main__":
    main()
