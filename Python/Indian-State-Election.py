import pandas as pd

# Load data
df = pd.read_csv("indian-state-level-election.csv")

# Initial inspection
print(df.size)
df.info()

# Drop unnecessary columns
df.drop(columns=['ac_no', 'ac_name', 'ac_type', 'cand_name'], axis=1, inplace=True)
df.info()

# Rename columns for clarity
df.rename(columns={
    'totvotpoll': 'Votes_Recieved',
    'cand_sex': 'Gender',
    'st_name': 'State_Name',
    'partyname': 'Party_Name',
    'electors': 'Total_Votes'
}, inplace=True)
df.info()

# Handle missing values
print(df.isna().sum())
print(df.Gender.unique())
df.Gender.fillna('O', inplace=True)
print(df.Gender.unique())
print(df.isna().sum())
df.partyabbre.fillna('Unknown', inplace=True)
print(df.isna().sum())
df.dropna(inplace=True)
print(df.isna().sum())
df.info()

# Remove duplicates
print(df.duplicated())
df.drop_duplicates(inplace=True)
df.info()

# Explore unique values
print(df.State_Name.unique())
print(df.Gender.unique())
print(df.Party_Name.unique())

# Party name processing
party_names = list(df.Party_Name.unique())
print(party_names)
df.Party_Name = df.Party_Name.str.upper()

def correct_party_name(value):
    if value == 'BJP':
        return 'BHARTIYA JANTA PARTY'
    elif value == 'BSP':
        return 'BAHUJAN SAMAAJ PARTY'
    elif value == 'INC':
        return 'INDIAN NATIONAL CONGRESS'
    else:
        return value

df.Party_Name = df.Party_Name.apply(correct_party_name)

# Save cleaned data
df.to_csv("Indian_state_level_election_cleaned.csv", index=False)
