
def main():
    file_path = "books/frankenstein.txt"

    with open(file_path) as f:
        file_contents = f.read()

        generate_report(file_path, file_contents)
        
        
        
def generate_report(file_path, file_contents):
    print(f"--- Begin report of {file_path} ---")
    print(f"{len(file_contents.split())} words found in the document\n")

    num_words = count_characters(file_contents)
    sorted_num_words = sorted(num_words.items(), key=lambda item:item[1], reverse=True)
    
    for num_word in sorted_num_words:
        print(f"The '{num_word[0]}' character was found {num_word[1]} times")

    print("--- End report ---")

def count_characters(text):
    ##initialize dictionary, so that only letters are included (no numbers or interpunctuation)
    char_dict = {}
    for num in range(97, 123):
        char_dict[chr(num)] = 0
    
    ## preprocessing
    text = text.lower()
    text = text.replace(" ", "")
    num_chars = len(text)

    ##count chars
    for i in range(num_chars):
        if text[i] in char_dict.keys(): 
            char_dict[text[i]] += 1
        # else:
        #     char_dict[text[i]] = 1

    return char_dict


main()