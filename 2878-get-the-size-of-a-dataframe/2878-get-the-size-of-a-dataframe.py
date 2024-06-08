import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
#     pd = players.shape


        num_rows, num_columns = players.shape


        result = [num_rows, num_columns]

        return result
    # return list(players.shape)
    