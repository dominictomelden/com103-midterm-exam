sports = ["Basketball", "Volleyball", "Badminton", "Chess", "Table Tennis"]
categories = ["Team", "Team", "Individual", "Individual", "Individual"]

section = input("Class section: ")
coordinator = input("Coordinator name: ")

print("\n" + "="*40)
print("  INTRAMURALS -- SPORTS EVENTS")
print("="*40)
for i in range(5):
    print(" {}. {:12} [{}]".format(i+1, sports[i], categories[i]))
print("="*40, "\n")

games = []

for game_no in range(1, 5):
    print("--- GAME {} ---".format(game_no))
    snum_input = input("Sport number (0 to skip): ")
    # BASIC: Just try to convert. If error, skip
    if snum_input == "0":
        print()
        continue
    if snum_input == "1" or snum_input == "2" or snum_input == "3" or snum_input == "4" or snum_input == "5":
        snum = int(snum_input)
        opp = input("Opposing section: ")
        res = input("Result (W/L): ").strip().upper()
        if res == "W":
            pts = 3
        else:
            pts = 0
            res = "L"
        games.append([snum, sports[snum-1], categories[snum-1], opp, res, pts])
        print()
    else:
        print("Invalid sport number. Skipping.\n")

total_points = 0
for g in games:
    total_points = total_points + g[5]

if total_points >= 9:
    standing = "GOLD CONTENDER"
elif total_points >= 6:
    standing = "SILVER PUSH"
else:
    standing = "KEEP FIGHTING!"

print("="*47)
print("     {} -- GAME RESULTS BOARD".format(section))
print("="*47)
print("Coordinator : {}".format(coordinator))
print("---------------------------------------------")

for idx in range(len(games)):
    g = games[idx]
    if g[4] == "W":
        res_word = "WIN"
    else:
        res_word = "LOSS"
    print("[{}] {:11} [{}]".format(idx+1, g[1], g[2]))
    print("    vs {}  |  Result: {:4} |  Points: {}".format(g[3], res_word, g[5]))
    print()
if len(games) == 0:
    print("(No games recorded)\n")
print("---------------------------------------------")
print("Total Points   : {}".format(total_points))
print("Standing       : {}".format(standing))
print("="*47)

"""
=============================================
     BSIT-1B -- GAME RESULTS BOARD
=============================================
Coordinator : Sir Raffy
---------------------------------------------
[1] Basketball [Team]
    vs BSIT-1C  |  Result: WIN  |  Points: 3

[2] Badminton  [Individual]
    vs BSIT-1D  |  Result: WIN  |  Points: 3

[3] Volleyball [Team]
    vs BSIT-1A  |  Result: LOSS |  Points: 0

---------------------------------------------
Total Points   : 6
Standing       : SILVER PUSH
=============================================
"""
