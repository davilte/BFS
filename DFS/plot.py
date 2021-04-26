import matplotlib.pyplot as plt

adj_list = {
    "8": ["3"],
    "3": ["1", "2", "4"],
    "1": ["4"],
    "2": ["4"],
    "4": ["7", "6"],
    "6": ["7", "5"],
    "7": ["5"],
    "5": []
}

plt.hist(adj_list, 5, rwidth=0.9)
plt.show()