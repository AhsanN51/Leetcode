import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee=employee.drop_duplicates(subset=['salary'])
    st="getNthHighestSalary("+str(N)+")"
    employee[st]=None
    if len(employee.index)<(N) or  N<=0 :
        return employee.iloc[[0]][[st]]
    else:
        employee=employee.sort_values(by="salary",ascending=False)
        employee[st][N-1]=employee["salary"].iloc[N-1]
        return employee[employee[st].index==(N-1)][[st]]

