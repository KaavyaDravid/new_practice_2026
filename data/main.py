print("main.py started")

try:
    from extract import extract_orders
    print("extract import successfully")
except Exception as e:
    print(f"Error importing extract module: {str(e)}")
    raise

def main():
    file_path = "orders.csv"
    
    try:
        orders = extract_orders(file_path)
        print("Extraction successful")
    except Exception as e:
        print(f"extraction failed: {str(e)}")
        return   
    
    print(f"Total records extracted: {len(orders)}")
    print("Sample record:")
    for key, value in orders[0].items():
        print(f"  {key}: {value}")
    
if __name__ == "__main__":
    main()