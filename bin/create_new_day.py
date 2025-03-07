import os
import shutil

# Find base directory (assumes bin/ is inside i18n/)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_FILE = os.path.join(BASE_DIR, "utils", "template.py")
INPUTS_DIR = os.path.join(BASE_DIR, "inputs")

def create_new_day():
    # Find existing days (folders named "01", "02", etc.)
    existing_days = sorted(
        int(d) for d in os.listdir(INPUTS_DIR) if d.isdigit()
    )

    new_day = str(existing_days[-1] + 1).zfill(2)

    # Create input folder for the new day
    new_day_folder = os.path.join(INPUTS_DIR, new_day)
    os.makedirs(new_day_folder, exist_ok=True)

    # Create empty input files if they don't exist
    for filename in ["test-answer"]: # "test-input", "input", 
        open(os.path.join(new_day_folder, filename), "a").close()

    # Copy template.py to new_day.py
    new_day_file = os.path.join(BASE_DIR, f"{new_day}.py")
    shutil.copyfile(TEMPLATE_FILE, new_day_file)

    print(f"✅ Created day {new_day}: {new_day_file}")
    print(f"✅ Created input folder: {new_day_folder}")

if __name__ == "__main__":
    create_new_day()