import os
import shutil
import argparse
from concurrent.futures import ThreadPoolExecutor

def copy_file(source_file, target_dir):
    file_name = os.path.basename(source_file)
    file_ext = os.path.splitext(file_name)[1]
    ext_dir = os.path.join(target_dir, file_ext[1:])
    os.makedirs(ext_dir, exist_ok=True)
    target_file = os.path.join(ext_dir, file_name)
    shutil.copy2(source_file, target_file)

def process_directory(directory, target_dir):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                copy_file(entry.path, target_dir)
            elif entry.is_dir():
                process_directory(entry.path, target_dir)

def main(source_dir, target_dir='dist'):
    with ThreadPoolExecutor() as executor:
        executor.submit(process_directory, source_dir, target_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process files in a directory and sort them by extension.')
    parser.add_argument('source_dir', type=str, help='Path to the source directory.')
    parser.add_argument('--target_dir', type=str, default='dist', help='Path to the target directory. Default is "dist".')
    args = parser.parse_args()
    main(args.source_dir, args.target_dir)
