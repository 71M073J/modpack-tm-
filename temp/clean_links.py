with open("./___1_18_2_newmods.txt", "r") as f:
    d = set()
    for line in f:
        l = line.replace("beta", "www")
        d.add(l)
with open("./modpack.txt", "w") as f:
    for l in sorted(list(d)):
        f.write(l)