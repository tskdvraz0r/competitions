import re
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    
    users["is_valid"] = [
        "valid" if re.match(pattern = r"^[a-zA-Z][a-zA-Z0-9._-]*@leetcode[.]com", string = mail) else "invalid"
        
        for mail in users["mail"]
    ]
    
    return users[users['is_valid'] == 'valid'].drop(labels = 'is_valid', axis = 1)