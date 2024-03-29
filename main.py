import pandas as pd

path = 'data.tsv'


# Error handling for file operations
def handle_file_errors(error_type, filename):
    if isinstance(error_type, pd.errors.EmptyDataError):
        print("The file is empty or has no valid data.")
    elif isinstance(error_type, FileNotFoundError):
        print(f"Error: File '{filename}' not found.")
    else:
        print(f"An unexpected error occurred: {error_type}")


# 1. Show the first 5 lines of the TSV file
def exercise_1():
    try:
        df = pd.read_csv(path, delimiter='\t')
        print(df.head())
    except Exception as e:
        handle_file_errors(e, path)


# 2. Find the number of rows and columns using read_csv with a sample
def exercise_2():
    try:
        df = pd.read_csv(path, delimiter='\t')
        num_rows, num_cols = df.shape
        print(f"Number of rows: {num_rows}")
        print(f"Number of columns: {num_cols}")
    except Exception as e:
        handle_file_errors(e, path)


# 3. Print the name of the columns
def exercise_3():
    try:
        df = pd.read_csv(path, delimiter='\t')
        column_names = df.columns.tolist()
        print("Column names:", column_names)
    except Exception as e:
        handle_file_errors(e, path)


# 4. What is the type of the column names?
def exercise_4():
    try:
        df = pd.read_csv(path, delimiter='\t')
        column_names_type = type(df.columns)
        print(f"Type of column names: {column_names_type}")
    except Exception as e:
        handle_file_errors(e, path)


# 5. Get the country column and save it to a variable. Show the first 5 observations.
def exercise_5():
    try:
        df = pd.read_csv(path, delimiter='\t')
        country_column = df['country']
        print("First 5 observations of 'country':")
        print(country_column.head())
    except Exception as e:
        handle_file_errors(e, path)


# 6. Show the last 5 observations of the country column
def exercise_6():
    try:
        df = pd.read_csv(path, delimiter='\t')
        country_column = df['country']
        print("Last 5 observations of 'country':")
        print(country_column.tail())
    except KeyError:
        print("The 'country' column does not exist in the file.")
    except Exception as e:
        handle_file_errors(e, path)


# 7. Look at country, continent, and year. Show the first 5 and last 5 observations.
def exercise_7():
    try:
        df = pd.read_csv(path, delimiter='\t')
        selected_columns = ['country', 'continent', 'year']
        if all(col in df.columns for col in selected_columns):
            print("First 5 observations of 'country', 'continent', and 'year':")
            print(df[selected_columns].head())
            print("Last 5 observations of 'country', 'continent', and 'year':")
            print(df[selected_columns].tail())
        else:
            missing_cols = [col for col in selected_columns if col not in df.columns]
            print(f"Columns '{', '.join(missing_cols)}' not found in the file.")
    except Exception as e:
        handle_file_errors(e, path)


# 8. Get the first row of the TSV file using two methods:
def exercise_8():
    try:
        df = pd.read_csv(path, delimiter='\t')
        print("First row using .head(1):")
        print(df.head(1))
        print("First row using .iloc[0]:")
        print(df.iloc[0])
    except Exception as e:
        handle_file_errors(e, path)


# 9. Get the first column and first/last column by integer index:
def exercise_9():
    try:
        df = pd.read_csv(path, delimiter='\t')
        print("First column:")
        print(df.iloc[:, 0])
        print("First and last columns:")
        first_col = df.iloc[:, 0]
        last_col = df.iloc[:, -1]
        print(pd.concat([first_col, last_col], axis=1))
    except Exception as e:
        handle_file_errors(e, path)


# 10. Get the last row using .loc and negative indexing:
def exercise_10():
    try:
        df = pd.read_csv(path, delimiter='\t')
        print("Last row using .loc[-1]:")
        print(df.loc[-1])
    except Exception as e:
        handle_file_errors(e, path)


# 11. Select the first, 100th, and 1000th rows using .iloc and .loc:
def exercise_11():
    try:
        df = pd.read_csv(path, delimiter='\t')
        print("First, 100th, 1000th rows using .iloc:")
        print(df.iloc[[0, 99, 999]])
        print("First, 100th, 1000th rows using .loc (assuming index starts from 0):")
        print(df.loc[[0, 99, 999]])
    except IndexError:
        print("The file may not have 1000 rows.")
    except KeyError:
        print("The file may not have an index starting from 0 or may not have 1000 rows.")
    except Exception as e:
        handle_file_errors(e, path)


# 12. Get the 43rd country using .loc and .iloc (assuming 'country' is a column):
def exercise_12():
    try:
        df = pd.read_csv(path, delimiter='\t')
        if 'country' in df.columns:
            print("43rd country using .loc (assuming index starts from 0):")
            print(df.loc[42, 'country'])
            print("43rd country using .iloc:")
            print(df.iloc[42, df.columns.get_loc('country')])
        else:
            print("The 'country' column does not exist in the file.")
    except Exception as e:
        handle_file_errors(e, path)


# 13. Get the first, 100th, 1000th rows from the first, 4th and 6th columns:
def exercise_13():
    try:
        df = pd.read_csv(path, delimiter='\t')
        cols = [0, 3, 5]

        # Define desired rows (manage potential IndexError)
        desired_rows = [0, 99]
        try:
            desired_rows.append(999)
        except IndexError:
            print("The file may not have 1000 rows.")

        # Select the subset using .iloc
        subset = df.iloc[desired_rows, cols]

        print("Subset of specified rows and columns:")
        print(subset)

    except Exception as e:
        handle_file_errors(e, path)


# 14. Get the first 10 rows of your data
def exercise_14():
    try:
        df = pd.read_csv(path, delimiter='\t')
        print("First 10 rows:")
        print(df.head(10))
    except pd.errors.EmptyDataError:
        print("The file is empty or has no valid data.")
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")


# 15. Average life expectancy for each year
def exercise_15():
    try:
        df = pd.read_csv(path, delimiter='\t')
        if 'year' in df.columns:
            print("Average life expectancy for each year:")
            print(df.groupby('year')['lifeExp'].mean())
        else:
            print("The 'year' column does not exist in the file.")
    except pd.errors.EmptyDataError:
        print("The file is empty or has no valid data.")
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")


# 16. Subsetting method for average life expectancy (alternative to 15)
def exercise_16():
    try:
        df = pd.read_csv(path, delimiter='\t')
        if 'year' in df.columns:
            year_groups = df.groupby('year')
            avg_life_expectancy = year_groups['lifeExp'].mean()
            print("Average life expectancy for each year (subsetting):")
            print(avg_life_expectancy)
        else:
            print("The 'year' column does not exist in the file.")
    except pd.errors.EmptyDataError:
        print("The file is empty or has no valid data.")
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")


# 17. Create a Series with index for 'banana' and '42'
def exercise_17():
    series = pd.Series(['banana', 42], index=['Person', 'Who'])
    print("Series with index 'Person' and 'Who':")
    print(series)


# 18. Series with index for 'Wes McKinney' and 'Creator of Pandas'
def exercise_18():
    series = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Title'])
    print("Series with index 'Person' and 'Title':")
    print(series)


# 19. Create a dictionary for pandas and convert to DataFrame
def exercise_19():
    data = {'Occupation': ['Chemist', 'Statistician'],
            'Born': ['1920-07-25', '1876-06-13'],
            'Died': ['1958-04-16', '1937-10-16'],
            'Age': [37, 61]}
    df = pd.DataFrame(data, index=['Franklin', 'Gosset'])
    print("DataFrame created from dictionary:")
    print(df)


if __name__ == "__main__":
    print("Exercise 1".center(100, "="))
    exercise_1()
    print("Exercise 2".center(100, "="))
    exercise_2()
    print("Exercise 3".center(100, "="))
    exercise_3()
    print("Exercise 4".center(100, "="))
    exercise_4()
    print("Exercise 5".center(100, "="))
    exercise_5()
    print("Exercise 6".center(100, "="))
    exercise_6()
    print("Exercise 7".center(100, "="))
    exercise_7()
    print("Exercise 8".center(100, "="))
    exercise_8()
    print("Exercise 9".center(100, "="))
    exercise_9()
    print("Exercise 10".center(100, "="))
    exercise_10()
    print("Exercise 11".center(100, "="))
    exercise_11()
    print("Exercise 12".center(100, "="))
    exercise_12()
    print("Exercise 13".center(100, "="))
    exercise_13()
    print("Exercise 14".center(100, "="))
    exercise_14()
    print("Exercise 15".center(100, "="))
    exercise_15()
    print("Exercise 16".center(100, "="))
    exercise_16()
    print("Exercise 17".center(100, "="))
    exercise_17()
    print("Exercise 18".center(100, "="))
    exercise_18()
    print("Exercise 19".center(100, "="))
    exercise_19()