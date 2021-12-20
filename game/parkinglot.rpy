label parking_lot:

    if ranking_meter >= 60:
        jump good_end
    elif ranking_meter >= 30:
        jump medium_end
    else:
        jump bad_end


label bad_end:
    scene car_gone
    
    "Julia arrives in the parking lot at long last, but does not see her car anywhere."
    "She checks all over the parking lot to see if maybe she forgot where she parked,
        but after 10 minutes of looking she comes to the conclusion that her car was stolen."
    "She takes out her phone to call the police and her insurance, and while dialing up the number,
        gets a notification that the University of Bath’s temporary ranking has fallen to the bottom 25\% of UK universities."

    jump finished


label medium_end:
    scene vandalized


    "Julia arrives in the parking lot, ready to go home, but finds that her car has been vandalized with graffiti."
    "She looks over the car and takes pictures from each side to make sure she has documentation of the crime."
    "Clearly upset, she gets into her car and drives away at a speed that is very clearly above the recommended speed for a university parking lot."

    jump finished


label good_end:
    scene sixhundered

    "After feeling like she did a good job helping students, Julia reaches her car in the parking lot."
    "She reaches into her pocket to get the car keys and unlocks it."
    "As she sits there, relieved that the term has come to an end and she can now enjoy the holidays, she notices that the car is awfully cold."
    "She swiftly starts up the engine and turns up the heat, before peacefully pulling out of the parking lot and driving off."

    jump finished

label finished:

    window hide

    show screen scoreboard
    show screen clear_scoreboard_button
    show screen add_to_leaderboard_button
    show screen exit_game_button
    pause
    jump finished
