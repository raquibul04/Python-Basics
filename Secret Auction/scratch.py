scores = {
    "Alice": 78,
    "Bob": 92,
    "Charlie": 85,
    "Diana": 90,
    "Ethan": 88
}
highest_score = 0
for keys in scores:
    if scores[keys] > highest_score:
        highest_score = scores[keys]

print(highest_score)        