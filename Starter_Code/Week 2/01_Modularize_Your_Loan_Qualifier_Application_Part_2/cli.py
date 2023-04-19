import fire
import random

def clothes_picker(pants = True):
    shirts_list = ["red_cherry_crest", "black_unicorn", "blue_cherry_crest", "panaman_shirt", "girls_galaxy"]

    pants_list = ["grey sweats", "blue sweats", "black sweats"]

    if pants:
        return random.choice(shirts_list), random.choice(pants_list)
    
    return random.choice(shirts_list)


if __name__ == '__main__':
    fire.Fire(clothes_picker)
