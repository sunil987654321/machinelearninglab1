def count_pairs_with_sum(lst, t_sum):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == t_sum:
                count += 1
    return count

lst = [2, 7, 4, 1, 3, 6]
t_sum = 10
result = count_pairs_with_sum(lst, t_sum)
print(f"Number of pairs with sum {t_sum}: {result}")
