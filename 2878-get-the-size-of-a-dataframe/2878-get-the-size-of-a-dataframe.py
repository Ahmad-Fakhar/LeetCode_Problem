import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    pd = players.shape

    # Get the number of rows and columns
    num_rows, num_columns = players.shape

# Return the result as an array
    result = [num_rows, num_columns]
 
    return result
    