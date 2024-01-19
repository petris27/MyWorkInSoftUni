lOlOl = set()
for something in range(int(input())):
    data_one, data_two = [eleM.split(",") for eleM in input().split("-")] #"0,3-1,2 -> ["0,3", "1,2"]" -> [[0, 3], [1, 2]]

    setche = set(range(int(data_one[0]), int(data_one[1]) + 1)) #{0, 1, 2, 3}
    setche_dwe = set(range(int(data_two[0]), int(data_two[1]) + 1)) #{1, 2}

    intersection = setche.intersection(setche_dwe)

    if len(intersection) > len(lOlOl):
        lOlOl = intersection

print(f"Longest intersection is "
      f"[{', '.join(str(x) for x in lOlOl)}] "
      f"with length {len(lOlOl)}")