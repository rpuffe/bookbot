def main():
    path = "./books/frankenstein.txt"
    frankenstein = get_text(path)
    count_words(frankenstein)
    count_characters(frankenstein)
    listOfDictionaries = create_list_of_dictionaries(count_characters(frankenstein))
    friendly_output(listOfDictionaries)

def get_text(path):
    with open(path) as f:
        text = f.read()
    return text 

def count_words(text):
    # print(len(text.split()))
    return len(text.split())

def count_characters(text):
    characters_dict = {}
    characters = list(text)
    for char in characters:
        lowercase = char.lower()
        if lowercase in characters_dict:
            characters_dict[lowercase] += 1
        else:
            characters_dict[lowercase] = 1
    
    # print(characters_dict)

    return characters_dict
    
def create_list_of_dictionaries(characters_dict):
    characters_list = []
    for key, value in characters_dict.items():
        characters_list.append({"character": key, "count": value})
    # sort the list of dictionaries by the count key
    characters_list.sort(key=lambda x: x["count"], reverse=True)
    return characters_list

def friendly_output(characters_list):
    for item in characters_list:
        print(f"The {item['character']} character was found {item['count']} times")

main()