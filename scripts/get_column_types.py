import pandas as pd
import duckdb
import os

def get_column_types(file_path: str, table_name: str = "default_table") -> dict:
    """
    Reads a file (CSV, Excel, or DuckDB) and returns a dictionary 
    mapping column names to their data types.
    
    :param file_path: Path to the target file.
    :param table_name: Required if the file is a DuckDB database; 
                        specifies which table to inspect.
    :return: Dictionary of {column_name: dtype}
    """
    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == '.csv':
        # Load CSV into a DataFrame
        df = pd.read_csv(file_path)
        
    elif file_ext in ['.xlsx', '.xls']:
        # Load Excel into a DataFrame
        df = pd.read_excel(file_path)
        
    elif file_ext in ['.db', '.duckdb']:
        # Connect to DuckDB and query the table
        # Using .df() converts the result set directly into a pandas DataFrame
        conn = duckdb.connect(database=file_path)
        query = f"SELECT * FROM {table_name}"
        df = conn.execute(query).df()
        conn.close()
        
    else:
        raise ValueError(f"Unsupported file extension: {file_ext}. "
                         "Please provide a .csv, .xlsx, or .duckdb file.")

    # df.dtypes returns a Series where index=column name and value=data type.
    # We convert it to a standard dictionary with string values for clean output.
    return {col: str(dtype) for col, dtype in df.dtypes.items()}

# --- Example Usage ---
# if __name__ == "__main__":
#     # Replace the paths below with your actual file paths
#     file_path = "<placeholder_for_your_file_path>" 
    
#     # If you are using a DuckDB file, replace 'default_table' with the 
#     # actual name of the table inside the .duckdb file.
#     try:
#         schema_dict = get_column_types(file_path)
#         print(f"Column types for {file_path}:")
#         print(schema_dict)
#     except Exception as e:
#         print(f"Error processing file: {e}")

for key,val in get_column_types('data/raw/listings.csv').items():
    print(f"{key}: {val}")
