import pandas as pd

# Load the uploaded file to see what's inside
file_path = 'data/emp_df.pkl'
data = pd.read_pickle(file_path)

# Zeigt alle Staaten an, ohne die Zeile werden die Staaten mit ... zusammengefasst
pd.set_option('display.max_columns', None)
# Splittet die Tabelle nicht, fuer mich uebersichtlicher, wenn die Daten nebeneinander sind
pd.set_option('display.width', 200)


# Display the first few rows of the dataframe
print(data)