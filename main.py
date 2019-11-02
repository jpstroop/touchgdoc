from touchgdoc import timestamp
from touchgdoc.app_setup import load_config
from sys import stderr

def main():
    try:
        config = load_config()
        # Do stuff
        return True
    except Exception as e:
        print(f"{timestamp()} - {e}", file=stderr)
        return False

if __name__ == "__main__":
    main()
