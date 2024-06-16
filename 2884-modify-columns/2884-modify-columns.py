import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
        # Modify the salary column by multiplying each salary by 2
    employees['salary'] = employees['salary'] * 2
    # Return the modified DataFrame
    return employees