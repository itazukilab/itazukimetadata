import csv
import json
import os

# Create directory for metadata files
os.makedirs("metadata", exist_ok=True)

csv_file_path = "itazukitraits.csv"
image_base_url = "https://raw.githubusercontent.com/itazukilab/itazukiimages/main/images/"

with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Get the token ID (0, 1, 2...)
        token_id = row.get("ID")
        if not token_id:
            continue
            
        # Structure the standard NFT metadata
        metadata = {
            "name": f"Itazuki #{token_id}",
            "description": "Itazuki NFT Collection",
            "image": f"{image_base_url}{token_id}.webp",
            "attributes": []
        }
        
        # Add traits from CSV to attributes list
        for key, value in row.items():
            if key != "ID" and value: # Skip ID and empty traits
                metadata["attributes"].append({
                    "trait_type": key,
                    "value": value
                })
        
        # Save as a standard extensionless metadata file or JSON
        output_path = os.path.join("metadata", str(token_id))
        with open(output_path, "w", encoding="utf-8") as out_file:
            json.dump(metadata, out_file, indent=4)

print("Metadata generation complete successfully.")
