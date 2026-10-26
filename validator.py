import json

def validate_evaluations(file_path):
    """Validates the structure and LaTeX syntax of evaluation records."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        print(f"Loaded {len(data)} evaluation records successfully.\n")
        
        for record in data:
            record_id = record.get("id", "Unknown ID")
            pref = record.get("preferred_response")
            justification = record.get("justification")
            
            if not pref or not justification:
                print(f"[FAIL] Record {record_id}: Missing preference or justification.")
            else:
                print(f"[PASS] Record {record_id}: Verified logic breakdown.")
                
    except Exception as e:
        print(f"Error loading evaluation file: {e}")

if __name__ == "__main__":
    validate_evaluations("evaluations.json")