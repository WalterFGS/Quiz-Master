import pgzrun

TITLE = "Quiz Master"
WIDTH = 870
HEIGHT = 650

marquee_box = Rect(0, 0, 880, 80)
question_box = Rect(0, 0, 650, 150)
timer_box = Rect(0, 0, 150, 150)
answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)
skip_box = Rect(0, 0, 150, 330)

score = 0
time_left = 10
question_file_name = "questions.txt"
marquee_message = ""
is_game_over = False
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []
questions_count = 0
question_index = 0

def update():
    move_marquee()

def move_marquee():
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def read_question_file(): 
    global question_count, questions

    try:
        q_file = open( question_file_name, "r")
        for questions_line in q_file: 
            question_line = question_line.strip()
            if question_line: 
                questions.append(question_line)
                question_count = question_count + 1
                q_file.close()
            print("Questions loaded", question_count)
    except FileNotFoundError:
        print("ERROR: questions.txt not found!")
        print("Looking for:")
        print(question_file_name)

def read_next_question():
    global question_index
    if questions:
        question_index = question_index + 1
        next_question = questions.pop(0)
        return next_question.split(",")
    else:
        return["No more questions!",
               "-",
               "-",
               "-",
               "-",
               "0"
               ]

def on_mouse_down(*pos):
    global question
    if is_game_over:
        return
    index = 1
    for box in answer_boxes:
        if box.collidepoint(*pos):
            if len(question) >=6:
                correct_answer_number = int(question[5])
                if index == correct_answer_number:
                    correct_answer()
                else:
                    game_over()
            return
    index = index + 1 

marquee_box.move_ip(0, 0)
question_box.move_ip(20, 100)
timer_box.move_ip(700, 100)
answer_box1.move_ip(20, 270)
answer_box2.move_ip(370, 270)
answer_box3.move_ip(20, 450)
answer_box4.move_ip(370, 450)
skip_box.move_ip(700, 270)

def draw(): 
    global marquee_message
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "navy blue")
    screen.draw.filled_rect(timer_box, "navy blue")
    screen.draw.filled_rect(skip_box, "dark green")
    for i in answer_boxes:
        screen.draw.filled_rect(i, "orange")
    marquee_message = "Welcome to Quiz Master!"
    marquee_message = marquee_message + f"Q:{question_index} of {questions_count}"
    screen.draw.textbox(marquee_message, marquee_box, color = "white")


read_question_file()
pgzrun.go()