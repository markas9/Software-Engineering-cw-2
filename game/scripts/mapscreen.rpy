# style hbox:
#     background "#000000"
#     color "#000000"


screen MapScreen():
    

    frame:
        # xalign 0.0
        # yalign 0.0
        # xsize 192
        # ysize 108
        background Frame("map.png")
        xmaximum 0.999
        ymaximum 0.999
        xalign 0
        yalign 0


        for i in Places:
            if i.isActive:
                hbox:
                    xpos i.xloc
                    ypos i.yloc

                    imagebutton :
                        hover i.iconsHover
                        idle i.icons
                        background "#f7f7f7"
                        action Jump (i.name)


                    if i.name=="cs_department" and not cs_dep_visited:
                        button:
                            text i.name size 20 color "#000000"
                            background "#f7f7f7"
                            action Jump ("cs_department")
                            yalign 0.5

                    elif i.name=="math_department" and not math_dep_visited:
                        button:
                            text i.name size 20 color "#000000"
                            background "#f7f7f7"
                            action Jump ("math_department")
                            yalign 0.5

                    elif i.name=="languages_department" and not languages_dep_visited:
                        button:
                            text i.name size 20 color "#000000"
                            background "#f7f7f7"
                            action Jump ("languages_department")
                            yalign 0.5

                    else:
                        button:
                            text i.name size 35 color "#db1616"
                            background "#000000"
                            action Jump ("cs_department")
                            yalign 0.5


    $all_visited()
