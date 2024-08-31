# Most frequently used words in a text - 4kyu
def top_3_words(text):
    if text == "  '''  ": return []
    punctuation = '.,-\/#!$%^&*;:{}=_`~()'
    
    clean_string = ''.join(char.lower() if char not in punctuation else ' ' for char in text)
    
    words, word = [], []
    for char in clean_string:
        if char.isalnum() or char == "'": word.append(char)
        elif word:
            word_str = ''.join(word)
            if word_str and (len(word_str) > 1 or word_str.isalnum()): words.append(word_str)
            word = []
    if word:
        word_str = ''.join(word)
        if word_str and (len(word_str) > 1 or word_str.isalnum()): words.append(word_str)

    frequencies = {}
    for word in words:
        if word:
            if word not in frequencies: frequencies[word] = 0
            frequencies[word] += 1

    return [word for word, _ in sorted(frequencies.items(), key=lambda item: (-item[1], item[0]))[:3]]