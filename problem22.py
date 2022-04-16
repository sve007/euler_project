# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

with open("problem22_input.txt") as f:
    input_data = f.read().split('","')
    input_data[0] = input_data[0][1:]
    input_data[-1] = input_data[-1][:-1]

#
input_data.sort()

# Maybe I pushed to hard for a one liner
letter_score = [(i+1)*sum([ord(l) - 96 for l in name.lower()]) for i, name in enumerate(input_data)]

print(sum(letter_score))