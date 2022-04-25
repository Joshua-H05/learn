rivers = {"Egypt": "The Nile",
          "Brazil": "The Amazon river",
          "China": "The yellow river"
          }
for country, river in sorted(rivers.items()):
    print(f"{river} runs through {country}\n")

print("Here is a list of the included countries:")
for country in sorted(rivers.keys()):
    print(f"{country}\n")

for river in sorted(rivers.values()):
    print(f"{river}\n")
