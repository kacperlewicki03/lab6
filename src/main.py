# src/main.py
import sys
from converters import convert_file

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_file(input_file, output_file)

if __name__ == "__main__":
    main()
