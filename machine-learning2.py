def calculate_range(lst):
    if len(lst) < 3:
        return "Range determination not possible"
    else:
        return max(lst) - min(lst)

lst = [5, 3, 8, 1, 0, 4]
result = calculate_range(lst)
print(f"The range is: {result}")
