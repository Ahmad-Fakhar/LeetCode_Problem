import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
        # Create DataFrame
    df = pd.DataFrame(report)

    # Melt the DataFrame
    melted_df = pd.melt(df, id_vars=['product'], var_name='quarter', value_name='sales')

    return melted_df