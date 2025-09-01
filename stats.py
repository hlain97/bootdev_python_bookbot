def get_book_text(filepath):
        
    with open(filepath) as f:
        read_data = f.read()
        
    print(read_data)

def get_num_words(filepath):
    
    with open(filepath) as f:
        read_data = f.read()
    
    counter = 0
    words = read_data.split()
    
    for word in words:
        counter += 1
        
    print(f"Found {counter} total words")
    
def count_characters(filepath):
    
    with open(filepath) as f:
        read_data = f.read()
    
    words = read_data.split()
    word_count = {}
    
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in word_count:
                word_count[letter] += 1
            else:
                word_count[letter] = 1
    return word_count

def sort_on(items):
    return items[1]

def sort_dict(d):
    
    new_list = []
    
    for key, value in d.items():
        new_list.append((key, value))
    
    new_list.sort(reverse=True, key=sort_on)
    
    for key, value in new_list:
        print(f'{key}: {value}')

###