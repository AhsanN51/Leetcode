import pandas as pd
      
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    users=users[users["mail"].str.match('^[A-Za-z][a-zA-Z0-9_.-]*@leetcode[.]com$')]
    return users
