
even_num = [x for x in range(1, 101) if x % 2 == 0]
print(even_num)
print()
odd_num = [x for x in range(1,101) if x % 2!= 0]
print(odd_num)
print()

words = ["the", "quick", "fox", "brown", "jumps", "lazy", "dog"]
answer = [[w.upper(), w.lower(), len(w) ] for w in words]
print(answer)
