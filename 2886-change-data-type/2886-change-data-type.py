import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students = pd.DataFrame(students)
    students['grade'] = students['grade'].astype(int)
    return students