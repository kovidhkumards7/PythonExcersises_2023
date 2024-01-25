discs = int(input("Enter a number of discs in tower to be moved: "))

def hanoiTower(disc, a = "Tower1", b = "Tower2", c = "Tower3"):
    if disc == 1:
        print("Move 1st disc from ", a, " to ", c)
        return
    hanoiTower(disc - 1, a, c, b)
    print("Move ", disc, "th disc from ", a, " to ", c)
    hanoiTower(disc - 1, b, a , c)

hanoiTower(discs)