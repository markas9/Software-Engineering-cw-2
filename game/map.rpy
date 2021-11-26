
screen map_button:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action Jump ("call_mapUI")

label call_mapUI:
    call screen MapUI

screen MapUI():
    add "map/map_bath.png"
