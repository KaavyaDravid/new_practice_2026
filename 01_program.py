# Function to remove duplicate strings from a list
def remove_duplicates(strings):
	"""
	Removes duplicate strings from the input list and returns a list of unique strings.
	Preserves the original order of first occurrences.
	"""
	unique = []
	seen = set()
	for s in strings:
		if s not in seen:
			unique.append(s)
			seen.add(s)
	return unique

# Example usage
if __name__ == "__main__":
	input_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
	result = remove_duplicates(input_list)
	print("Unique strings:", result)
