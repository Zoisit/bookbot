
def main():
    file_path = "books/frankenstein.txt"

    with open(file_path) as f:
        file_contents = f.read()
        
        num_words = len(file_contents.split())
        
        print(num_words)

main()