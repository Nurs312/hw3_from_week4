text = input()
uppers = 0
lowers = 0
total = len(text)
for letter in text:
    if letter.isupper() == True:
        uppers += 1
    else:
        lowers += 1
up_per = (uppers/total)*100
low_per = (lowers/total)*100
print(f'Upper case letters percent is {up_per}%')
print(f'Lower case letters percent is {low_per}%')
