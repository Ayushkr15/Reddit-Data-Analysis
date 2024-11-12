import pandas as pd
import json

# Paths for the input and output files
input_file = '/mnt/d/coding/tensorflowProjects/tf217/Projects/Reddit/combined_processed_data.ndjson'  # replace with your actual file path
output_file = '/mnt/d/coding/tensorflowProjects/tf217/Projects/Reddit/output_file.csv'

# Convert JSON to CSV in chunks to handle large files
with open(input_file, 'r') as json_file:
    # Load each line as a JSON object
    json_data = [json.loads(line) for line in json_file]

    # Convert list of JSON objects to DataFrame
    df = pd.DataFrame(json_data)

    # Write the DataFrame to a CSV file
    df.to_csv(output_file, index=False)
