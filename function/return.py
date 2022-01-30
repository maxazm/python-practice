def print_dict(input_dict): #Noneを返す
    for k, v in input_dict.items():
        print(f"key:{k}, value:{v}")
    # return None


a = {"one": 1, "two": 2}
print(a)
return_val = print_dict(a)
print_dict(a)
print(return_val)

def get_first_last_word(text):
    text = text.replace(",", " ")
    words = text.split()
    return words[0], words[-1]

text = "Hello my name is Mike"
first, last = get_first_last_word(text)
print(f"first: {first} last: {last}")