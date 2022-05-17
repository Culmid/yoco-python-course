import sys


def delete(start_dir: str) -> None:
    """Remove duplicate files recursively from the start_dir"""
    print(f"Delete {start_dir};)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Incorrect Usage,\n\tUsage: duplicate.py <start_dir>")

    delete(sys.argv[1])
