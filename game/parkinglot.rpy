label parking_lot:
    $check_ending_scene()
    
    scene school_gate
    with dissolve

    if ranking_meter >= 80:
        jump good_end
    elif ranking_meter >= 40:
        jump medium_end
    else:
        jump bad_end


label bad_end:

    "Car not found!"

    jump finished


label medium_end:

    "Car found with grafiti!"

    jump finished


label good_end:

    "Car found!"

    jump finished



label finished:

    "CONGRATULATIONS FINISHED"
    pause
    return