vowels = 'aeiou'
consonant = 'zrtypqsdfghjklmwxcvbn'
# create your list here
a = input()
x = [char for char in a if char in vowels]
y = [char for char in a if char in consonant]
print(x)
print(y)
