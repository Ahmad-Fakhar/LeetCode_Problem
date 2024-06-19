import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(weather)

    # Pivot the DataFrame
    pivot_df = df.pivot(index='month', columns='city', values='temperature')

    return pivot_df  