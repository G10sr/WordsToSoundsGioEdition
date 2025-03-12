import random
fnaf =  [
    "five night's at freddy's", "five nights at freddys", "freddy", "animatronic", "foxy", "bonnie", "chica",
    "baby", "ennard", "springtrap", "afton", "purple guy", "fazbear", "mangle", "puppet", "jj", "rwqfsfasxc",
    "shadow bb", "xor", "springlock", "fredbear", "phantom bb", "nightmare", "plushtrap", "balloon boy", 
    "nightmarionne", "freddles", "dreadbear", "ballora", "bidybab", "minireena", "bon-bon", "lolbit", "electrobab", 
    "bonnet", "music man", "lefty", "rockstar foxy's parrot", "carnie", "happy frog", "mr. hippo", "pigpatch", 
    "nedd bear", "orville elephant", "mystic hippo", "monty", "montgomery gator", "roxxy", "roxanne wolf", "endo",
    "the mimic", "tangle", "helpy"
]
message = "baby,tangle y lefty"

if message in fnaf:
    rand = random.randint(1, 9)
    print(rand)
