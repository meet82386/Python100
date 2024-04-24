import requests

x = requests.get("https://opentdb.com/api.php?amount=15&category=18&type=boolean")
print(x.json())

question_data = x.json()["results"]

# question_data = [
#     {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
#      "question": "The HTML5 standard was published in
#      2014.", "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
#      "question": "In most programming languages, the operator ++ is equivalent to the statement.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
#      "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
#      "question": "All program codes have to be compiled into an executable
#      file in order to be run. This file can then be executed on any machine.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
#      "question": "The first computer bug was formed by faulty wires.", "correct_answer": "False",
#      "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
#                                       "question": "MacOS is based on Linux.", "correct_answer": "False",
#                                       "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
#      "question": "The last Windows operating system to be based on the Windows 9x kernel was Windows 98.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
#      "question": "The very first recorded computer &quot;bug&quot; was a moth found inside a Harvard Mark II computer.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "hard", "category": "Science: Computers",
#      "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
#      "question": "Linus Sebastian is the creator of the Linux kernel, which went on to be used in Linux, Android, and Chrome OS.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
#      "question": "&quot;HTML&quot; stands for Hypertext Markup Language.", "correct_answer": "True",
#      "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
#                                        "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
#                                        "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
#      "question": "Ada Lovelace is often considered the first computer programmer.", "correct_answer": "True",
#      "incorrect_answers": ["False"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
#                                        "question": "The common software-programming acronym &quot;I18N&quot; comes from the term &quot;Interlocalization&quot;.",
#                                        "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
#      "question": "A Boolean value of &quot;0&quot; represents which of these words?", "correct_answer": "False",
#      "incorrect_answers": ["True"]}
# ]
