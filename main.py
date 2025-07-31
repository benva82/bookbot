def main():
    get_book_text("books/frankenstein.txt")
    get_word_count()

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_word_count():
    file_contents = get_book_text("books/frankenstein.txt")
    words_string = file_contents.split()
    num_words = len(words_string)
    print(f"{num_words} words found in the document")

main()
