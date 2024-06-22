import sys

from interpreter import nscInterpreter

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        with open(file_path, 'r') as f:
            code = f.read()
            nscInterpreter.run_code(code)
    else:
       print("No file path provided.")

