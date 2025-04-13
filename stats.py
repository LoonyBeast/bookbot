def words_total(string):
    dictionary= string.split()
    return len(dictionary)

def count_characters(text: str) -> dict:
    """
    Returns a dictionary with the count of each character (lowercased)
    from the given text.
    """
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(item):
    return item["count"]

def sort_characters_by_count(char_dict: dict) -> list:
    sorted_chars = [
        {'char': char, 'count': count}
        for char, count in char_dict.items()
        if char.isalpha()
    ]
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars