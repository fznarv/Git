def rev(word):
    rev = word[::-1]
    count = len(word)
    print(f'"{rev}" with {count} Characters')

word = input('ENTER A WORD: ')

rev(word)

#lambda ex.
var = lambda x,y: x + y

print(var(2, 5))