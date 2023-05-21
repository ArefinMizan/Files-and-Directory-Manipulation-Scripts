import os
import shutil

base_dir = 'D:/sd-con'  # set this to your base directory
output_dir = 'D:/embeddings'  # set this to your desired output directory

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.bin'):
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(output_dir, file)

            # move the file
            shutil.move(old_file_path, new_file_path)
            print(f"Moved file {old_file_path} to {new_file_path}")
