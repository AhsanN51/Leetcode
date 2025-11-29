import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus']=0
    cond= (employees["employee_id"]%2==1) & (employees["name"].str[0]!='M')
    
    employees.loc[cond,'bonus']=employees["salary"]
    return employees[['employee_id','bonus']].sort_values(by='employee_id')
