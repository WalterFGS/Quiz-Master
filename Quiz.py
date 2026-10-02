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
is_game_overr = False
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