# Sample grocery lists from parents
list1 = ["milk", "eggs", "bread", "butter"]
list2 = ["cheese", "milk", "apples", "bread", "bananas"]

# Step 1: Combine both lists
combined_list = list1 + list2

# Step 2: Remove duplicates using set
unique_items = set(combined_list)

# Step 3: Sort the final list alphabetically
final_list = sorted(unique_items)

# Step 4: Print the final sorted list
print("Final Grocery List:")
for item in final_list:
    print("-", item)
