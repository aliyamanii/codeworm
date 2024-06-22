import argparse
from interpreter import run_code

def main():
    parser = argparse.ArgumentParser(description="Run the NSC interpreter.")
    parser.add_argument("input_file", type=str, help="The input file to be interpreted.")
    
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r') as f:
            code = f.read()
        run_code(code)
    except FileNotFoundError:
        print(f"Error: The file {args.input_file} was not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
