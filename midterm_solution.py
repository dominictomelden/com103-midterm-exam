sports = ["Basketball", "Volleyball", "Badminton", "Chess", "Table Tennis"]
categories = ["Team", "Team", "Individual", "Individual", "Individual"]
section = ""
section_ok = False
while section_ok == False:
    section = input("Class section: ")
    if section == "":
        print("Invalid input. Please enter a class section.")
    else:
        section_ok = True

coordinator = ""
coordinator_ok = False
while coordinator_ok == False:
    coordinator = input("Coordinator name: ")
    if coordinator == "":
        print("Invalid input. Please enter a coordinator name.")
    else:
        coordinator_ok = True

print("\n" + "="*40)
print("  INTRAMURALS -- SPORTS EVENTS")
print("="*40)
for i in range(5):
    print(" " + str(i+1) + ". " + sports[i] + "    [" + categories[i] + "]")
print("="*40 + "\n")

games = []

for game_no in range(1, 5):
    print("--- GAME " + str(game_no) + " ---")
    snum_input = input("Sport number (0 to skip): ")
    if snum_input == "0":
        print()
        continue
    if snum_input == "1" or snum_input == "2" or snum_input == "3" or snum_input == "4" or snum_input == "5":
        snum = int(snum_input)
        opp = input("Opposing section: ")
        res = input("Result (W/L): ").upper()
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
print("     " + section + " -- GAME RESULTS BOARD")
print("="*47)
print("Coordinator : " + coordinator)
print("---------------------------------------------")

for idx in range(len(games)):
    g = games[idx]
    if g[4] == "W":
        res_word = "WIN"
    else:
        res_word = "LOSS"
    print("[" + str(idx+1) + "] " + g[1] + " [" + g[2] + "]")
    print("    vs " + g[3] + "  |  Result: " + res_word + "  |  Points: " + str(g[5]))
    print()
if len(games) == 0:
    print("(No games recorded)\n")
print("---------------------------------------------")
print("Total Points   : " + str(total_points))
print("Standing       : " + standing)
print("="*47)
