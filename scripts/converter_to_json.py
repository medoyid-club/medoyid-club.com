import csv
import json
import os

# Get the script's directory to build relative paths
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# Use relative paths
csv_file_path = os.path.join(project_root, 'temp', 'members_list.csv')
json_file_path = os.path.join(project_root, 'data', 'members.json')

# Read the raw data
with open(csv_file_path, mode='r', encoding='utf-8') as infile:
    lines = infile.readlines()

# Use csv reader to handle quoted fields
reader = csv.reader(lines)
data = list(reader)

# Transpose the data
headers = [row[0] for row in data]
members_data = []
# There is an extra empty column at the end of the csv, so I subtract 1
num_members = len(data[0]) - 1

for i in range(1, num_members):
    member = {}
    for j, header in enumerate(headers):
        if i < len(data[j]):
            member[header] = data[j][i]
        else:
            member[header] = ""
    members_data.append(member)

# Create the JSON objects
output_members = []

for item in members_data:
    output_item = {
        "category": item.get("function", ""),
        "name": item.get("name", ""),
        "case": item.get("case", ""),
        "foto": f"{item.get('foto', '')}.webp" if item.get('foto') else "",
        "youtube": item.get("YouTube", ""),
        "telegram": item.get("Telegram", ""),
        "facebook": item.get("Facebook", ""),
        "patreon": item.get("Patreon", ""),
        "instagram": item.get("Instagram", ""),
        "tiktok": item.get("TikTok", ""),
        "threads": item.get("threads", ""),
        "web": item.get("Web", ""),
        "email": item.get("E-mail", ""),
        "linkedin": item.get("LinkedIn", "")
    }
    output_members.append(output_item)

final_output = output_members

# Ensure the data directory exists
os.makedirs(os.path.dirname(json_file_path), exist_ok=True)

with open(json_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(final_output, outfile, ensure_ascii=False, indent=2)

print(f"Successfully converted CSV to JSON at {json_file_path}")
