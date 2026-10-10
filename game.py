# PIXEL STREAMER - text edition (v2)
# Run it with: python3 game.py
# Goal: reach 1,000 subscribers before your rig overheats.
# New in v2: props shop (spend subs, earn more per stream) + raid events.

import random  # brings in Python's dice roller for random events

subs = 0        # your subscriber count
heat = 20       # rig heat - hits 100 and the stream dies
hype_left = 3   # hype blasts left
goal = 1000     # subs needed to win

# the props shop: each item is [name, price in subs, bonus subs per stream]
shop_items = [
    ["Artuban Sculpture", 300, 15],
    ["Cyber Odyssey 2027 poster", 150, 8],
    ["Neon Mecha Rising poster", 150, 8],
    ["8-Bit Space Hero poster", 150, 8],
    ["Pixel Samurai figure", 200, 10],
    ["Cyber Mecha figure", 200, 10],
    ["Mythic Chibi Dragon figure", 250, 12],
]
owned = []  # props you bought - starts empty


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


def show_shop():
    # prints everything on the shelf, numbered so you can pick one
    print("")
    print("PROPS SHOP - your subs:", subs)
    num = 1
    for item in shop_items:
        print(num, "-", item[0], "| price:", item[1], "| +", item[2], "subs per stream")
        num = num + 1


print("PIXEL STREAMER - you're live!")
print("reach", goal, "subs before heat hits 100.")
print("new: type 'shop' to buy props that boost every stream.")

playing = True
while playing:
    print("")
    print("subs:", subs, "| heat:", heat, "| hype left:", hype_left, "| props:", len(owned))
    choice = input("what now? (stream / cool / hype / shop): ")

    if choice == "stream":
        bonus = 0
        for prop in owned:
            bonus = bonus + prop[2]  # add up every prop's per-stream bonus
        gained = random.randint(20, 60) + bonus
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
    elif choice == "shop":
        show_shop()
        pick = input("buy which number? (or 'back'): ")
        if pick == "back":
            print("leaving the shop.")
        else:
            num = int(pick)  # turn the typed text into a real number
            if num >= 1 and num <= len(shop_items):
                item = shop_items[num - 1]  # shelf numbers start at 1, list starts at 0
                name = item[0]
                price = item[1]
                if subs >= price:
                    subs = subs - price
                    owned.append(item)
                    print("bought", name, "- nice.")
                else:
                    print("not enough subs for", name, "(costs", price, ")")
            else:
                print("that's not on the shelf.")
    else:
        print("huh? type stream, cool, hype, or shop")

    # 1-in-4 chance of a glitch each turn
    if random.randint(1, 4) == 1:
        lost = glitch_event()
        subs = subs - lost
        if subs < 0:
            subs = 0

    # 1-in-6 chance a bigger streamer raids you with free viewers
    if random.randint(1, 6) == 1:
        raiders = random.randint(30, 80)
        subs = subs + raiders
        print("")
        print("RAID! another streamer sent", raiders, "viewers your way!")

    if heat >= 100:
        print("")
        print("RIG OVERHEATED. stream over - final subs:", subs)
        playing = False
    elif subs >= goal:
        print("")
        print("1,000 SUBS! you're a diamond creator!")
        playing = False
