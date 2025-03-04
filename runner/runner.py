import subprocess

# List of all the scripts to run
scripts = [
    "BlueOne.py",
    "BlueTwo.py",
    "BlueThree.py",
    "BlueSub",
    "RedOne.py",
    "RedTwo.py",
    "RedThree.py",
    "RedSub.py"
]

# Function to run each script
def run_scripts():
    for script in scripts:
        try:
            print(f"Running {script}...")
            subprocess.run(["python", script], check=True)
            print(f"{script} ran successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error running {script}: {e}")

# Main function to execute the scripts
if __name__ == "__main__":
    run_scripts()
