import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ['student_id','age'])

student_data = [[1, 15], [2, 11], [3, 11], [4, 20]]  # List of lists with student data
df = pd.DataFrame(student_data, columns=['student_id', 'age'])

print(df)

    