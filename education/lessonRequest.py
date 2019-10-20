arr1 = ['i','e','d','e','m','b','r']
word = input("Provide a word to find in vowels")
found =[]
for letter in word:
    if letter in arr1:
        if letter not in found:
            found.append(letter)
for arr2 in found:
    print(arr2)
