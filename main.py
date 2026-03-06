from finder import find_duplicates
import os

folder = input("Enter folder path to scan: ")

duplicates = find_duplicates(folder)

if duplicates:
    print("\nDuplicate files found:")

    for dup, original in duplicates:
        print(f"{dup} is duplicate of {original}")

    choice = input("\nDo you want to delete duplicate files? (yes/no): ").lower()

    if choice == "yes":
        for dup, original in duplicates:
            file_path = os.path.join(folder, dup)
            os.remove(file_path)
            print(f"Deleted: {dup}")

        print("Duplicate files removed.")

    else:
        print("No files were deleted.")

else:
    print("No duplicate files found.")