import pandas as pd


def validate_table_format(file_path):
    try:
        # Read the file into a DataFrame
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        else:
            return False

        # Check if the DataFrame has at least 2 columns, rows, and valid format
        if (
            len(df.columns) >= 2
            and len(df) >= 2
            and all(isinstance(col, str) for col in df.columns)
            and all(
                isinstance(value, str) or pd.isna(value)
                for value in df.values.flatten()
            )
            and len(df.columns) == len(set(df.columns))
        ):
            return True
        else:
            return False

    except Exception as e:
        print("Error:", e)
        return False
