map = []

for x in range(0,5):
    map.append(["."] * 10)

map[0][0] = "S"
map[0][2], map[0][3] = "#", "#"
map[0][9], map[1][1] = "T", "T"
map[1][0], map[1][2], map[1][3], map[1][6], map[1][7], map[1][8] = "#", "#", "#", "#", "#", "#"



def print_map(map):
    for row in map:
        print " ".join(row)

print_map(map) 