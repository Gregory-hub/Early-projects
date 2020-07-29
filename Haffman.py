text = input()
letters = []
no_repeat_dict = []
dict_letters = {}

for l in text:
    letters.append(l)

for k in letters:
    if k in no_repeat_dict:
        continue
    no_repeat_dict.append(k)

for i in no_repeat_dict:
    count = 0
    for j in letters:
        if i == j:
            count += 1
    dict = {i : str(count)}
    dict_letters.update(dict)


#print(letters)
#print(no_repeat)
print(dict_letters)