import curses
from curses import wrapper
import time
import random

def start_screen(stdscr): 
    stdscr.clear()
    stdscr.addstr("Speed typing whatever shit, I guess.")
    stdscr.addstr("\nPress any key to begin?")
    stdscr.refresh()

def load_quote() -> str:
    with open("quotes.txt", "r", encoding = "UTF-8") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def display_text(stdscr, target_text: str, current_text: list[str], time_elapsed: float, wpm: int = 0):

    stdscr.addstr(target_text)
    stdscr.addstr(10, 0, f"WPM: {wpm}")
    stdscr.addstr(10, 12, f"Time: {time_elapsed:.3f}s")

    for index, char in enumerate(current_text):

        # Handles whether the character is correct
        correct_character = target_text[index]
        color = curses.color_pair(1)
        if char != correct_character:
            color = curses.color_pair(2)

        stdscr.addstr(0, index, char, color)

def wpm_test(stdscr):
    # target_text: str = "lorem ipsum dolor sit amet, consectetur adipiscing elit"
    target_text:str = load_quote()
    current_text: list[str] = list()

    wpm: float = 0
    start_time: float = time.time()
    stdscr.nodelay(True)
    AVERAGE_WORD_LENGTH: int = 5

    while True:
        time_elapsed: float = max(time.time() - start_time, 1)
        wpm = round(60 * (len(current_text) / time_elapsed) / AVERAGE_WORD_LENGTH, 2)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, time_elapsed, wpm)
        stdscr.refresh()

        # Check if word is right
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        # Necessary to avoid "no input" crashes
        try:
            key = stdscr.getkey()
        except:
            continue
        
        # Breaks loop with the ESC key
        try:
            if ord(key) == 27:
                break
        except:
            continue

        # Handles proper backspace?
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):

    # Adds color... it seems
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # Initializes
    start_screen(stdscr)
    
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "Done? Press whatever to continue... I guess")
        try:
            key = stdscr.getkey()
        except:
            break

        try:
            if ord(key) == 27:
                break
        except:
            continue

wrapper(main)