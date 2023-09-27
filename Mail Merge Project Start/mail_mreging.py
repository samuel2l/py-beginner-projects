PLACEHOLDER='[name]'
with open("Input/Names/invited_names.txt") as file:
    k=file.read()

names_list=k.split()
# print(names_list)

with open("Input/Letters/starting_letter.txt") as file:
    l = file.read()

# print(l)
for i in names_list:

    # new_letter=' '.join(letter_list)
    new_letter=l.replace(PLACEHOLDER,i)
    with open(f"Output/ReadyToSend/letter_for_{i}.txt", 'w') as file:
        file.write(new_letter)

