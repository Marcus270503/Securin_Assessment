''' Calculate the probability of each sum by counting the occurrences 
and dividing by the total number of combinations. '''

probability_sums = [0] * 12
total_combinations = 6 * 6
for i in range(6):
    for j in range(6):
        probability_sums[(i + 1) + (j + 1) - 2] += 1

for i, count in enumerate(probability_sums):
    probability = count / total_combinations
    print(f"P(Sum = {i + 2}) = {probability}")
