def main():
    # Define the path to the book file
    book_path = "books/frankenstein.txt"
    
    # Read the entire text of the book
    text = get_book_text(book_path)
    
    # Count the total number of words in the book
    num_words = get_num_words(text)
    
    # Create a dictionary with character frequencies
    chars_dict = get_chars_dict(text)
    
    # Convert the dictionary into a sorted list of character counts
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    # Print the report header
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    # Print character frequency, only for alphabetic characters (a-z)
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue  # Skip non-alphabetic characters
        print(f"The '{item['char']}' character was found {item['num']} times")

    # Print the report footer
    print("--- End report ---")


def get_num_words(text):
    """Counts the total number of words in the given text."""
    words = text.split()  # Split text into words based on spaces
    return len(words)  # Return the count of words


def sort_on(d):
    """Helper function for sorting by character count."""
    return d["num"]  # Returns the numeric count of characters


def chars_dict_to_sorted_list(num_chars_dict):
    """Converts a dictionary of character counts into a sorted list."""
    sorted_list = []
    
    # Convert dictionary entries to a list of dictionaries
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    
    # Sort the list in descending order based on character frequency
    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list


def get_chars_dict(text):
    """Creates a dictionary with the count of each character in the text."""
    chars = {}

    # Loop through each character in the text
    for c in text:
        lowered = c.lower()  # Convert character to lowercase
        if lowered in chars:
            chars[lowered] += 1  # Increment count if already exists
        else:
            chars[lowered] = 1  # Initialize count if first occurrence

    return chars  # Return the dictionary of character counts


def get_book_text(path):
    """Reads and returns the text from the given file path."""
    with open(path) as f:
        return f.read()  # Read the entire file content and return it


# Call the main function to execute the program
main()

