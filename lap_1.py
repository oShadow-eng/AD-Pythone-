cat_a = ([1, 2, 3, 4, 5])
cat_b = ([10, 20, 30])

def calculate_stats(data):
    sum(cat_a)
    max(cat_b)
    return(sum(cat_a) / len(cat_a), max(cat_b))

stats_a = calculate_stats(cat_a)
stats_b = calculate_stats(cat_b)

print("A:", stats_a)
print("B:", stats_b)
