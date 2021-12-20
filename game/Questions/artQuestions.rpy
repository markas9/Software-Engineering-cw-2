define artQuestions = ["art_question1", "art_question2", "art_question3"]
$ renpy.random.shuffle(artQuestions)

label art_question1:
    s "I just found out Adolf Hitler was also a painter, and while I find that really interesting and would like to see his work, I’m afraid I’ll end up on a government watchlist if I search for his work on google..."
    menu:
        "Hello and good morning to you too. Whatever you do, do not use a university computer.":
            s "Okay, I have another question"
        "I heard nothing, have a nice day.":
            $ ranking_meter -= lower_increase
            s "Okay, I have another question"
        "Perhaps you could look in the library, maybe they have a book that talks about it.":
            s "Okay, I have another question"
            $ ranking_meter += higher_increase
        "Maybe you can call them up on the phone before you google it to give them a heads up.":
            s "Okay, I have another question"
            $ ranking_meter += lower_increase
    return

label art_question2:
    s "Picasso had such an interesting development in his art style, it’s very captivating."
    menu:
        "That is nice but you are slowing my development towards my car.":
            s "Okay, I have another question"
            $ ranking_meter -= lower_increase
        "I thought Picasso was the guy with the apple and gravity.":
            $ ranking_meter -= lower_increase
            s "Okay, I have another question"
        "If you’re interested in him, I can recommend the Picasso Museum in Malaga, Spain. It has work from all throughout his life, and encompasses his art very well.":
            s "Okay, I have another question"
            $ ranking_meter += higher_increase
    return

label art_question3:
    s "Man, Leonardo DaVinci was fascinating. A scientist, engineer, painter, sculptor, theorist and architect, was there anything he couldn’t do? He was basically the Johnny Sins of his time."
    menu:
        "The who of his time? He drew the Mona Lisa and a few guys having dinner, if my daughter practiced painting for years she could do that too.":
            $ ranking_meter -= lower_increase
            s "Okay, I have another question"
        "Hey, don’t say that so loudly. That name can’t be thrown around like that.":
            s "Okay, I have another question"
        "Yeah, DaVinci was pretty talented, and he really knew how to leave his mark in history.":
            s "Okay, I have another question"
            $ ranking_meter += lower_increase
        "While DaVinci was undoubtedly gifted, do not drag the name of the mighty Johnny Sins through the mud like that. The man accomplished what DaVinci did, but also became a doctor, general, president, professor, astronaut, musician, went to jail, and then redeemed himself by becoming a car mechanic, a chef, a race car driver, and a professional sports player.":
            if creativity < 2:
                "You dont have enough creativity"
                jump art_question3
            s "Okay, I have another question"
            $ ranking_meter += higher_increase
    return