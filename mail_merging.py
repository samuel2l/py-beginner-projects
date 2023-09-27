#your idea initially but will not preserve the format of the letter
#one with correct format using the replace and readline func is in mail_mreging.py
with open("Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    k=file.read()

names_list=k.split()
print(names_list)

with open("Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    l = file.read()
print(l)
letter_list=l.split()
print(letter_list)
for i in names_list:
    letter_list[1]=i
    new_letter=' '.join(letter_list)
    with open(f"Mail Merge Project Start/Output/ReadyToSend/letter_for_{i}.txt", 'w') as file:
        file.write(new_letter)
#
# for i in names_list:
#
#
#
# for i in names:
#     with open(f"letter_for_{i}",) as file:
#         print(file.read())
