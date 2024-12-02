import pandas as pd

# List of players
roster = ['Tyson', 'Davis', 'Cadeau', 'Withers', 'Trimble', 'Powell', 'Jackson', 'Washington', 'Lubin', 'Claude']

# Print the roster list
print("Roster List:", roster)

# Loop 
print("\nRoster Loop:")
for player in roster:
    print(player)

# DataFrame with default header
df_default = pd.DataFrame(roster)
print("\nDataFrame with Default Header:")
print(df_default)

# DataFrame with "Last Name" as the header
df_with_header = pd.DataFrame(roster, columns=["Last Name"])
print("\nDataFrame with 'Last Name' Header:")
print(df_with_header)
