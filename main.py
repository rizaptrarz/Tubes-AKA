import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd
import sys

sys.setrecursionlimit(10000)
file_path = '/content/Filtered_Matches.csv'
data = pd.read_csv(file_path)

data_info = data.info()
data_head = data.head()
data_info, data_head
# Filter dataset
filtered_data = data[["Team", "Opponent", "Team_Score", "Opponent_Score"]].dropna()

filtered_data = filtered_data.head(10000)

matches_list = filtered_data.rename(columns={
    "Team": "team1",
    "Opponent": "team2",
    "Team_Score": "score1",
    "Opponent_Score": "score2"
}).to_dict(orient="records")

# subset dan jumlah n
n_values = [1, 2, 3, 4, 5, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000]
subsets = {n: matches_list[:n] for n in n_values}

# Bubble Sort
def bubble_sort_simulation(matches):
    matches = matches.copy()
    start_time = time.time()
    n = len(matches)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (matches[j]["score1"] + matches[j]["score2"]) > (matches[j + 1]["score1"] + matches[j + 1]["score2"]):
                matches[j], matches[j + 1] = matches[j + 1], matches[j]
    end_time = time.time()
    return (end_time - start_time) * 1000  

# Quick Sort
def quick_sort_simulation(matches):
    matches = matches.copy()

    def partition(arr, low, high):
        pivot = arr[high]["score1"] + arr[high]["score2"]
        i = low - 1
        for j in range(low, high):
            if (arr[j]["score1"] + arr[j]["score2"]) <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort(arr, low, pi - 1)
            quick_sort(arr, pi + 1, high)

    start_time = time.time()
    quick_sort(matches, 0, len(matches) - 1)
    end_time = time.time()
    return (end_time - start_time) * 1000  

bubble_sort_times = [bubble_sort_simulation(subsets[n]) for n in n_values]
quick_sort_times = [quick_sort_simulation(subsets[n]) for n in n_values]

plt.figure(figsize=(10, 6))
plt.plot(n_values, bubble_sort_times, label="Bubble Sort", marker="o")
plt.plot(n_values, quick_sort_times, label="Quick Sort", marker="o")
plt.xlabel("Number of Matches (n)")
plt.ylabel("Time (ms)")
plt.title("Sorting Time Comparison: Bubble Sort vs Quick Sort")
plt.legend()
plt.grid()
plt.show()
