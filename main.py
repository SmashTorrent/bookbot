#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

def main(book_path):

    def count_words(text):
        words_list = text.split()
        return len(words_list)
    
    def count_characters(text):
        characters = {}
        for i in text.lower():
            if i.isalpha():                 # only adds an alpha character to the dictionary
                if i in characters:
                    characters[i] += 1
                else:
                    characters[i] = 1
        return characters

    def print_report(character_count, word_count):
        print(f"--- Begin report of {book_path} ---")
        print(f"{number_of_words} words were found in the document\n")

        for i in character_count:
            print(f"The '{i[0]}' character was found {i[1]} times")

        print("--- End report ---")

    with open(book_path, "r") as my_book:
        book_text = my_book.read()
        number_of_words= count_words(book_text)
        unique_characters = count_characters(book_text)
        # sort dictionary by most to least found characters
        # convert dictionary to a list
        lst = list(unique_characters.items())
        sorted_by_usage = sorted(lst, reverse=True, key= lambda x: x[1])
        print_report(sorted_by_usage, number_of_words)


main("books/frankenstein.txt")