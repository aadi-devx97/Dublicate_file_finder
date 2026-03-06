import os
import hashlib

def get_file_hash(filepath):
    hasher = hashlib.md5()

    with open(filepath, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            hasher.update(chunk)

    return hasher.hexdigest()

def find_duplicates(folder_path):
    hashes = {}
    duplicates = []

    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)

        if os.path.isfile(filepath):
            file_hash = get_file_hash(filepath)

            if file_hash in hashes:
                duplicates.append((filename, hashes[file_hash]))
            else:
                hashes[file_hash] = filename

    return duplicates