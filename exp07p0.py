def find_vowels(sentence):
    return set(sentence) & {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

# Example usage
sentence = input("Enter a sentence: ")
print("Vowels in the sentence:", find_vowels(sentence))
