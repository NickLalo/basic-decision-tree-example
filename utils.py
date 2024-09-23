"""
file to store functions used for in the basic decision tree example
"""


def print_data_types(df):
    """
    Print out the column names and their data types in a dataframe
    
    inputs:
        df: pandas dataframe
    outputs:
        None
    """
    # get the max length of any individual column name or string "Column Name"
    max_col_name_len = max([len(col) for col in df.columns] + [len("Column Name")])
    # get the max length of any individual data type or string "Data Type"
    max_dtype_len = max([len(str(dtype)) for dtype in df.dtypes] + [len("Data Type")])
    # get total length of the printed line for the spacer lines
    total_len = max_col_name_len + max_dtype_len + 5
    
    # print out the column names and their data types
    print("-" * total_len)
    print(f" {'Column Name':<{max_col_name_len}}   {'Data Type':>{max_dtype_len}}")
    print("-" * total_len)
    for col in df.columns:
        print(f" {col:<{max_col_name_len}}   {str(df[col].dtype):>{max_dtype_len}}")
    print("-" * total_len)
    return


def print_target_percentage_numerical(df, target_column):
    """
    function to print the percentage and count of each target value in the target column of a pandas dataframe for
    numerical data.  This is helpful to understand the distribution of targets in the dataset and a first step to 
    understand if a dataset is balanced or not.
    
    inputs:
        df: pandas dataframe
        target_column: str, name of the target column in the dataframe
    outputs:
        None
    """
    
    # get the count of each target value in the dataframe
    count_dict = {}
    for target in df[target_column].unique():
        count = df[df[target_column] == target].shape[0]
        count_dict[target] = count
    
    # sort the dictionary by the target count (dictionary value)
    count_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
    
    # print the results in a table format
    print("-" * 33)
    print(f" Target  |  Percentage  |  Count")
    print("-" * 33)
    total_target_count = df.shape[0]
    for target, count in count_dict.items():
        percentage = (count / total_target_count) * 100
        print(f"{target:>7.3f}  |  {percentage:>9.2f}%  |{count:>7}")
    
    # print extra information
    print(f"\nTotal count: {total_target_count:>7}")
    print(f"Unique targets: {len(df[target_column].unique()):>4}")
    print("-" * 33)
    return


def print_target_percentage_categorical(df, target_column, target_names):
    """
    function to print the percentage and count of each target value in the target column of a pandas dataframe for
    categorical data.  This function assumes that the target values in the dataframe are integers that are used as
    indexes in the target_names list. This is helpful to understand the distribution of targets in the dataset and a 
    first step to understand if a dataset is balanced or not.
    
    inputs:
        df: pandas dataframe
        target_column: str, name of the target column in the dataframe
        target_names: list of str, names of the target values
    outputs:
        None
    """
    
    # get the count of each category in the dataframe
    count_dict = {}
    for target in df[target_column].unique():
        count = df[df[target_column] == target].shape[0]
        count_dict[target] = count
    
    # sort the dictionary by the target count (dictionary value)
    count_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
    
    # print the results in a table format
    print("-" * 40)
    print(f" Category Name  |  Percentage  |  Count")
    print("-" * 40)
    total_target_count = df.shape[0]
    for target, count in count_dict.items():
        percentage = (count / total_target_count) * 100
        category_name = target_names[target]
        print(f" {category_name:<15}|  {percentage:>9.2f}%  |{count:>7}")
    
    print(f"\nTotal count: {total_target_count:>7}")
    print(f"Unique targets: {len(df[target_column].unique()):>4}")
    print("-" * 40)
    return