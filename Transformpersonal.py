text = """Yesterday 4/4/2023 was a very good day. I started my Python journey and interacted with a great learning course. 'Python for beginners' is a learning path that I found through microsoft course. On day one I got half way through with the course, with 2 total hours of work. Completing 4 modules, I learned a number of things.
After settting up my visiual code it was time to gain some knowledge in a exciting field. New information I gathered included; ways to format mutlilines, converting units, using boolean logic, string methods, and how to transform text. These skills will be the foundation to my future and the things I can do with code. It is my goal
to learn and apply new skills everyday up until taking summer courses at NCC. It is my goal to excel in computer science. It is my goal to become a data analysis. I have always been a critical thinker and problem solver, I have always been good with numbers and math. It is my goal to reach my maximum potential. It is my goal to stay determined and reach new heights"""

sentences = text.split('. ')

for sentence in sentences:
    if 'goal' in sentence:
        print(sentence)
        print('------------------------------------------------------------')

