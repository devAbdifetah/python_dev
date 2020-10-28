#get sentence from user
original = input("please enter sentence")
#split sentence into words
words = original.split()

#loop through words and convert to pig latin

new_words = []
for word in words:
     if word[0] in "aeiou":
          new_word = word + "yay"
          new_words.append(new_word)
print(new_words)     
         

#if starts with vowel just add yay
#otherwise move the first consonant cluster to end and add "ay"
