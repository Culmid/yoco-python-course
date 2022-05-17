import filecmp
import sys
import os
from os.path import join


def delete(start_dir: str, interactive: bool = True) -> None:
    """Remove duplicate files recursively from the start_dir. Notes:
        - Duplicate = filename, size and contents are all equal.
        - Interactive like mode enabled by default (Removes are dangerous).
        - NB: Be careful with start_dir as you could remove important files,
              if you are not careful. dummy_desktop is the recommended argument."""
    print(f"Removing duplicates, start directory: {start_dir}", end="\n\n")

    file_dict = {}
    for root, _, files in os.walk(start_dir):
        for file in files:
            if file in file_dict:
                if filecmp.cmp(file_dict[file], join(root, file), shallow=False):
                    old_file = file_dict[file]
                    new_file = join(root, file)

                    if interactive:
                        print(
                            f"Existing<0>: {old_file}, New<1>: {new_file}")
                        delete_info = input(
                            "DELETE: [0] - Existing, [1] - New, [other] - Ignore: ")
                        if delete_info == "0":
                            os.remove(old_file)
                            file_dict[file] = new_file
                            print(f"DELETED: {old_file}")
                        elif delete_info == "1":
                            os.remove(new_file)
                            print(f"DELETED: {new_file}")
                        else:
                            print(f"SKIPPED: {file}")
                    else:
                        os.remove(new_file)
                        print(f"DELETED: {new_file}")

                    print("-" * 100)

            else:
                file_dict[file] = join(root, file)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Incorrect Usage,\n\tUsage: duplicate.py <start_dir>")

    delete(sys.argv[1], False)
