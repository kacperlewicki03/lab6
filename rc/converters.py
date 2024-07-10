# src/converters.py (continuation)
def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Similar functions for XML and YAML

def convert_file(input_path, output_path):
    input_format = input_path.split('.')[-1]
    output_format = output_path.split('.')[-1]

    if input_format == 'json':
        data = load_json(input_path)
    # Similar checks for XML and YAML

    if output_format == 'json':
        save_json(data, output_path)
    # Similar checks for XML and YAML
