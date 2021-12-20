
label start:
    call initialize
    image julia angry = "characters/julia_outfit1_angry.png"
    
    scene afternoon01
    with fade

    "The ranking of the University of Lath has sunk moderately over the years,
        and with Christmas holidays starting, the time the university has to
        improve their ranking for the year is steadily decreasing."
    "University staff is tasked with aiding in the improvement of the rank by
        attempting to drive up average test scores and student satisfaction."
    show julia angry
    with dissolve
    "Julia Gadget is a Computer Science professor at the University of Bath and has
        just finished her last lecture for the term."
    "As she exits her lecture hall to make her way to her car across campus to
        return to her family for the holidays, concerned students approach her to
        ask her questions regarding different matters."
    "Julia is faced with the decision of whether she wants to help the students
        and therefore increase the university ranking through average scores and
        satisfaction increasing, or turning down the students and
        returning home to her family faster."
    
    menu:
        
        "Start Game?":
            window hide
            $renpy.call_screen("MapScreen",_layer="screens")

        "Inventory (Beta Phase)":
            
            jump test_menu 
       
