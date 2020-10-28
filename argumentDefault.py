def about(name, age, likes="java"):
    sentence = "Meet {}! He is {} years old and he like {}".format(name, age, likes)
    return sentence

answer = about("Abdifetah", 26, "java")
print(answer)
print(type(answer))


def about(name = "dhoore", age = 25, likes = "football"):
    sentence = "meet {} He is {} years old and he likes {} ".format(name,age, likes)
    return sentence

ans = about()
print(ans)
