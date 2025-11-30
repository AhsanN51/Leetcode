import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee=employee.drop_duplicates(subset="salary")
    if len(employee["salary"])<2:
        return pd.DataFrame({"SecondHighestSalary": [None]}, columns=["SecondHighestSalary"])
    else:
        employee=employee.sort_values(by="salary",ascending=False)
    
    ss=employee["salary"].iloc[1]

    return pd.DataFrame({"SecondHighestSalary": [ss] },columns=["SecondHighestSalary"])
    



"""def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if len(employee) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]}, columns=["SecondHighestSalary"])
    
    sorted_df = employee.sort_values(by="salary", ascending=False).drop_duplicates(subset="salary")
    second_salary = sorted_df["salary"].iloc[1]
    
    return pd.DataFrame({"SecondHighestSalary": [second_salary]}, columns=["SecondHighestSalary"])
"""
