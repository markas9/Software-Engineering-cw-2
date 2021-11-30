label campus_map:
    scene utica map 720p
    with dissolve

    if all_visited():
        jump parking_lot

menu:
    "Math Department" if not math_dep_visited:
        jump math_department
    "CS Department" if not cs_dep_visited:
        jump cs_department
    "Languages Department" if not languages_dep_visited:
        jump languages_department
    
    
