def compare_arrays(original, updated):
    new_elements = list(set(updated) - set(original))
    removed_elements = list(set(original) - set(updated))
    return new_elements, removed_elements

original = [1, 2, 3, 4, 5]
updated = [2, 3, 5, 6, 7]
new_elements, removed_elements = compare_arrays(original, updated)

print('New Elements:',new_elements)
print('Removed elements:',removed_elements)