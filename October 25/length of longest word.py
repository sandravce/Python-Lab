#Accept a list of words and return length of a longest word

def longest_word_length(words):
    if not words:
        return 0  # Handle empty list
    return max(len(word) for word in words)

