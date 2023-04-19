import fire
import random

def excercise_options ():
    exercise_list = ["deadlifts", "rope_climb", "situps", "snatch", "biceps"]

    return random.choice(excercise_options)

if __name__ == '__main__':
    fire.Fire(excercise_options)