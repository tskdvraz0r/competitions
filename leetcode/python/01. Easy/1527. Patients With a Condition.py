import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    
    patients["is_diabet"] = False
    
    for idx, string_with_conditions in enumerate(iterable = patients["conditions"]):
        for condition in string_with_conditions.split(" "):
            if condition[:5].lower() == "diab1":
                patients.loc[idx, "is_diabet"] = True
            
            else:
                continue
    
    return patients[patients["is_diabet"] == True].drop(labels = "is_diabet", axis = 1)