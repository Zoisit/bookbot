
def main():
    file_path = "books/frankenstein.txt"

    with open(file_path) as f:
        file_contents = f.read()
        
        num_words = count_characters(file_contents)
        
        print(num_words)

def count_characters(text):
    char_dict = {}
    
    ## preprocessing
    text = text.lower()
    text = text.replace(" ", "")
    num_chars = len(text)

    #count chars
    for i in range(num_chars):
        if text[i] in char_dict.keys(): 
            char_dict[text[i]] += 1
        else:
            char_dict[text[i]] = 1

    return char_dict

main()