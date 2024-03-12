# Define a function to count pairs in a list with a given sum
def count_pairs_with_sum(lst, t_sum):
    count = 0  # Initialize the count of pairs
    
    # Iterate through each element in the list
    for i in range(len(lst)):
        # Iterate through subsequent elements from the current element
        for j in range(i+1, len(lst)):
            # If the sum of the current pair equals the target sum
            if lst[i] + lst[j] == t_sum:
                count += 1  # Increment the count of pairs
                
    return count  # Return the total count of pairs

# Define the list and target sum
lst = [2, 7, 4, 1, 3, 6]
t_sum = 10

# Call the function to count pairs with the target sum
result = count_pairs_with_sum(lst, t_sum)

# Print the result
print(f"Number of pairs with sum {t_sum}: {result}")
