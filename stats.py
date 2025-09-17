def get_num_words(book_contents):
    count = 0
    words = book_contents.split()
    for word in words:
        count += 1
    return count

def get_letter_count(book_contents):
    letters = dict()
    str(book_contents)
    lower_case = book_contents.lower()
    for letter in lower_case:
        if letter in letters:
            letters[letter] = letters[letter] + 1
        else:
            letters[letter] = 1
    return(letters)

def sorting(items):
    return items["num"]

def get_report(letter_dictionary):
    report = []
    for letter in letter_dictionary:
        report.append({"char": letter, "num": letter_dictionary[letter]})
    report.sort(reverse=True, key=sorting)
    
    return(report)