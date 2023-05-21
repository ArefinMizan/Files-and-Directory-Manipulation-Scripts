import os
import shutil

base_dir = 'D:/sd-con'  # set this to your base directory

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file == 'learned_embeds.bin':
            new_name = os.path.basename(root) + '.bin'  # get folder name and append .bin
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(root, new_name)

            # rename the file
            shutil.move(old_file_path, new_file_path)
            print(f"Renamed file {old_file_path} to {new_file_path}")