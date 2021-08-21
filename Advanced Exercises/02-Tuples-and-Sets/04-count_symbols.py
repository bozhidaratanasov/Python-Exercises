from collections import defaultdict
text = input()
character_occurrences = defaultdict(int)
for el in text:
    character_occurrences[el] += 1
character_occurrences = dict(sorted(character_occurrences.items(), key=lambda el: el[0]))
for key, value in character_occurrences.items():
    print(f"{key}: {value} time/s")
