from .Question import Question
question_prompt = [
    "what color are apples?\n(a) red/green\n(b) purple\n(c) Orange\n\n",
    "what color are bananas?\n(a) teal\n(b) magenta\n(c) Yellow\n\n",
    "what color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"

]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "C"),
    Question(question_prompt[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("you got" + str(score) + "/" + str(len(questions)))

run_test(questions)
