input = input("Enter word to convert: ").upper()

import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

data = [phonetic_dict[n] for n in input]

print(data)


