def filter_words_by_length(words, min_length=3):
    """
    Фільтрує слова за довжиною.
    
    :param words: список слів (list[str])
    :param min_length: мінімальна довжина слова (int)
    :return: список слів довших за min_length
    """
    return [word for word in words if len(word) > min_length]

# --- Приклад використання ---
if __name__ == "__main__":
    result = filter_words_by_length(["hi","python","cat"], 4)
    print(result)  # Виведе: ['python']
