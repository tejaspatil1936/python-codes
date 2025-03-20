# Start

# Input Sentence 1
sentence1 = input("Enter first sentence: ")

# Split Sentence 1 and Create Set 1
set1 = set(sentence1.split())

# Input Sentence 2
sentence2 = input("Enter second sentence: ")

# Split Sentence 2 and Create Set 2
set2 = set(sentence2.split())

# Find Common Words
common_words = set1 & set2  # Intersection

# Find Unique Words
unique_words_sentence1 = set1 - set2  # Words unique to sentence 1
unique_words_sentence2 = set2 - set1  # Words unique to sentence 2

# Print Common Words
print("\nCommon Words:", common_words)

# Print Unique Words
print("Words unique to sentence 1:", unique_words_sentence1)
print("Words unique to sentence 2:", unique_words_sentence2)

# End

