import subprocess
import os

# Create JSON directory if it doesn't exist
json_directory = "JSON"
if not os.path.exists(json_directory):
    os.makedirs(json_directory)

# List of all the scripts to run
scripts = [
    "BlueOne.py",
    "BlueTwo.py",
    "BlueThree.py",
    "RedOne.py",
    "RedTwo.py",
    "RedThree.py",
    "RedSubjective.py"
]

# Function to run each script
def run_scripts():
    for script in scripts:
        try:
            print(f"Running {script}...")
            # Pass the JSON directory as an environment variable to each script
            subprocess.run(["python", script, json_directory], check=True)
            print(f"{script} ran successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error running {script}: {e}")

# Main function to execute the scripts
if __name__ == "__main__":
    run_scripts()
