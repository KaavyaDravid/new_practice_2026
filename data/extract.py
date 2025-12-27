import csv
from typing import List, Dict

def extract_orders(file_path: str) -> List[Dict[str, str]]:
    """
    Extracts raw order data from a CSV file.
    Each row is returned as a dictionary with column headers as keys.
    """
    
    records = []
    
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                records.append(row)
                
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    
    except Exception as e:
        raise Exception(f"An error occurred while reading the file/extraction: {str(e)}")   
    
    return records         