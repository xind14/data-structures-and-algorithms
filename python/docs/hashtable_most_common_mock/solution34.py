def most_common_word(book):

    words = book.lower().split()
    
    word_freq = {}
    
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    most_common = ""
    max_count = 0
    
    for word, count in word_freq.items():
        if count > max_count:
            most_common = word
            max_count = count
    
    return most_common
