import os
import glob

folder_path = "frames_1"
jpgs = glob.glob(os.path.join(folder_path,"*.jpg"))

for i, old_name in enumerate(jpgs):
    new_name = os.path.join(folder_path, f"frame_{i}.jpg")

    os.rename(old_name, new_name)
    print(f"{old_name} to {new_name}")