###this program displays both square and exponent(optional)
##def exponent(num, power=2):
##     return num ** power
##
##print(exponent(4,2))

def multiple_letter_count(string):
    dic={"dhoore": count(string), "saadaalin": count(string)}
    answer={dic[i]:string[i] for i in dic}
    return answer
print(multiple_letter_count("dhoore"))
