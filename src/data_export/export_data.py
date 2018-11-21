
import pandas as pd


def export_table_as_csv(data, filename):
    pd.DataFrame(data).to_csv(filename, index=False)