import fire
import random

def clothes_picker ():
    shirts_list = ["red_cherry_crest", "black_unicorn", "blue_cherry_crest", "panaman_shirt", "girls_galaxy"]

    return random.choice(shirts_list)

if __name__ == '__main__':
    fire.Fire(clothes_picker)