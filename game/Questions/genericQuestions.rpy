label genericQ1:
    s "GENERIC Q 1"
    menu:
        "A1":
            $ ranking_meter -= five_points
            s "R1"
        "A2":
            $ ranking_meter -= five_points
            s "R1"
        "A3":
            $ ranking_meter += five_points
            s "R1"
        "A4":
            if logic < 2:
                "You dont have enough logic"
                jump genericQ1
            $ ranking_meter -= five_points
            s "R1"
    return

label genericQ2:
    s "GENERIC Q 2"
    menu:
        "A1":
            $ ranking_meter -= five_points
            s "R1"
        "A2":
            $ ranking_meter -= five_points
            s "R1"
        "A3":
            $ ranking_meter += five_points
            s "R1"
        "A4":
            if logic < 2:
                "You dont have enough logic"
                jump genericQ2
            $ ranking_meter -= five_points
            s "R1"
    return

label genericQ3:
    s "GENERIC Q 3"
    menu:
        "A1":
            $ ranking_meter -= five_points
            s "R1"
        "A2":
            $ ranking_meter -= five_points
            s "R1"
        "A3":
            $ ranking_meter += five_points
            s "R1"
        "A4":
            if logic < 2:
                "You dont have enough logic"
                jump genericQ3
            $ ranking_meter -= five_points
            s "R1"
    return

label genericQ4:
    s "GENERIC Q 4"
    menu:
        "A1":
            $ ranking_meter -= five_points
            s "R1"
        "A2":
            $ ranking_meter -= five_points
            s "R1"
        "A3":
            $ ranking_meter += five_points
            s "R1"
        "A4":
            if logic < 2:
                "You dont have enough logic"
                jump genericQ4
            $ ranking_meter -= five_points
            s "R1"
    return

label genericQ5:
    s "GENERIC Q 5"
    menu:
        "A1":
            $ ranking_meter -= five_points
            s "R1"
        "A2":
            $ ranking_meter -= five_points
            s "R1"
        "A3":
            $ ranking_meter += five_points
            s "R1"
        "A4":
            if logic < 2:
                "You dont have enough logic"
                jump genericQ5
            $ ranking_meter -= five_points
            s "R1"
    return