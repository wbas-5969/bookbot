def get_num_words(input_text):
	split_words=input_text.split()
	count_words=len(split_words)
	return count_words

def character_count(input_text):
	word_count_dict = {}
	for char in input_text:
		if char.lower() in word_count_dict:
			word_count_dict[char.lower()] += 1
		else:
			word_count_dict[char.lower()] = 1
	return word_count_dict

def sort_on_char(items):
	return items["num"]

def sort_character_dict(char_dict):
	sorted_list = []
	for char_key in char_dict:
		if char_key.isalpha():
			sorted_list.append({"char": char_key, "num": char_dict[char_key]})
	sorted_list.sort(reverse=True, key=sort_on_char)
	return sorted_list