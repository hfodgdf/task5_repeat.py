from typing import List

def filter_words_by_length(words: List[str], min_length: int = 3) -> List[str]:
    return [word for word in words if len(word) > min_length]

if __name__ == "__main__":
    result = filter_words_by_length(["hi", "python", "cat"], 4)
    print(result)  # ['python']
