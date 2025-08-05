from stats import get_num_words, character_count, sort_character_dict
import sys

def get_book_text(bookpath):
	with open(bookpath) as f:
		book_text = f.read()
	return book_text

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path=sys.argv[1]
	book_text=get_book_text(book_path)
	num_words=get_num_words(book_text)
	char_dict=character_count(book_text)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
#	print(char_dict)
	for dict_item in sort_character_dict(char_dict):
		print(f"{dict_item['char']}: {dict_item['num']}")
#	print(sort_character_dict(char_dict))
main()
