# 🗳 Indian State Level Election Project



```python
# 📦 Import the pandas library
import pandas as pd
```



```python
# 📥 Load the dataset into a DataFrame
df = pd.read_csv("indian-state-level-election.csv")
```



```python
# 👀 Display the DataFrame
df
```



```python
# 🔢 Show total number of elements in the DataFrame
df.size
```



```python
# 🧠 Inspect structure, column types, and null values
df.info()
```



```python
# ❌ Drop unnecessary columns
df.drop(columns=['ac_no', 'ac_name', 'ac_type', 'cand_name'], axis=1, inplace=True)
```



```python
# 🔁 Recheck the structure after column removal
df.info()
```



```python
# ✏️ Rename columns for clarity
df.rename(columns={
    'totvotpoll': 'Votes_Recieved',
    'cand_sex': 'Gender',
    'st_name': 'State_Name',
    'partyname': 'Party_Name',
    'electors': 'Total_Votes'
}, inplace=True)
```



```python
# 🔍 Check the updated column info
df.info()
```



```python
# 📉 Count missing values
df.isna().sum()
```



```python
# 🧬 View unique gender values
df.Gender.unique()
```



```python
# ⚙️ Fill missing Gender values with 'O'
df.Gender.fillna('O', inplace=True)
```



```python
# ✅ Confirm unique values after replacement
df.Gender.unique()
```



```python
# 🧪 Check null values again
df.isna().sum()
```



```python
# 🔤 Fill missing party abbreviations
df.partyabbre.fillna('Unknown', inplace=True)
```



```python
# 🧪 Recheck for missing values
df.isna().sum()
```



```python
# 🧹 Drop remaining rows with missing data
df.dropna(inplace=True)
```



```python
# ✅ Final check for nulls
df.isna().sum()
```



```python
# 📋 View final structure
df.info()
```



```python
# 🧩 Identify duplicate entries
df.duplicated()
```



```python
# 🧼 Remove duplicates
df.drop_duplicates(inplace=True)
```



```python
# 📊 Confirm after removing duplicates
df.info()
```



```python
# 🏷️ Unique states
df.State_Name.unique()
```



```python
# 🧬 Unique gender values
df.Gender.unique()
```



```python
# 🏛️ Unique party names
df.Party_Name.unique()
```



```python
# 📜 Store unique parties in a list
x = list(df.Party_Name.unique())
```



```python
# 🖨️ Print the list
print(x)
```



```python
# 🔠 Convert party names to uppercase
df.Party_Name = df.Party_Name.str.upper()
```



```python
# 👀 View changes
df.Party_Name
```



```python
# 🛠️ Function to correct common abbreviations
def correct_party_name(value):
    if value == 'BJP':
        return 'BHARTIYA JANTA PARTY'
    elif value == 'BSP':
        return 'BAHUJAN SAMAAJ PARTY'
    elif value == 'INC':
        return 'INDIAN NATIONAL CONGRESS'
    else:
        return value
```



```python
# 🎯 Apply correction function
df.Party_Name = df.Party_Name.apply(correct_party_name)
```



```python
# 💾 Save cleaned DataFrame
df.to_csv("Indian_state_level_election_cleaned.csv", index=False)
```
