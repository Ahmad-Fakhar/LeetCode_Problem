import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = pd.DataFrame(students)

# Rename the columns
    students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    }, inplace=True)
    return students