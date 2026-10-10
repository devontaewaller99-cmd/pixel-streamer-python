# PIXEL STREAMER - text edition (v1)
# Run it with: python3 game.py
# Goal: reach 1,000 subscribers before your rig overheats.

import random  # brings in Python's dice roller for random events

subs = 0        # your subscriber count
heat = 20       # rig heat - hits 100 and the stream dies
hype_left = 3   # hype blasts left
goal = 1000     # subs needed to win


def glitch_event():
    # a random glitch hits the stream - hands back how many subs you lost
    print("")
    print("GLITCH! chat is spamming. type 'fix' fast!")
    answer = input("> ")
    if answer == "fix":
        print("glitch squashed. chat loves you.")
        return 0
    print("too slow - the glitch ate some subs.")
    return 30


print("PIXEL STREAMER - you're live!")
print("reach", goal, "subs before heat hits 100.")

playing = True
while playing:
    print("")
    print("subs:", subs, "| heat:", heat, "| hype left:", hype_left)
    choice = input("what now? (stream / cool / hype): ")

    if choice == "stream":
        gained = random.randint(20, 60)
        subs = subs + gained
        heat = heat + random.randint(8, 15)
        print("nice stream! +", gained, "subs")
    elif choice == "cool":
        heat = heat - 25
        if heat < 0:
            heat = 0
        print("cooling down... heat:", heat)
    elif choice == "hype":
        if hype_left > 0:
            hype_left = hype_left - 1
            gained = random.randint(80, 150)
            subs = subs + gained
            heat = heat + 20
            print("HYPE BLAST! +", gained, "subs")
        else:
            print("no hype left!")
    else:
        print("huh? type stream, cool, or hype")

    # 1-in-4 chance of a glitch each turn
    if random.randint(1, 4) == 1:
        lost = glitch_event()
        subs = subs - lost
        if subs < 0:
            subs = 0

    if heat >= 100:
        print("")
        print("RIG OVERHEATED. stream over - final subs:", subs)
        playing = False
    elif subs >= goal:
        print("")
        print("1,000 SUBS! you're a diamond creator!")
        playing = False
