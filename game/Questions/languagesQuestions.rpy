label initLanguagesQuestions:
    $ langQuestions = ["lang_question1", "lang_question2", "lang_question3", "lang_question4", "lang_question5"]
    $ renpy.random.shuffle(langQuestions)
    return

label lang_question1:
    s "I listened to this song and they said “voulez vous coucher avec moi, ce soir?” What does that mean?"
    menu:
        "I have no idea, is that spanish?":
            $ ranking_meter -= lower_increase
            s "Well that wasn't helpful at all!"
        "I am not sure that is an appropriate thing to ask.":
            s "Oh I am sorry if I said anything bad, I am going to go now.."
        "I believe it means “would you like to sleep with me tonight?”":
            $ ranking_meter += lower_increase
            s "That is so embarassing, I am so sorry!"
        "Brexit means Brexit, keep those languages away from me!":
            $ ranking_meter -= higher_increase
            s "You are the opposite of helpful..."
    return

label lang_question2:
    s "I was reading something for my Italian homework, and
        noticed it looked similar to the writing I see on coins sometimes, why’s that?"
    menu:
        "I’m neither Italian nor a historian, so why do you ask me this? Leave me alone.":
            $ ranking_meter -= lower_increase
            s "True, I should of asked someone who speak Italian, but you could of been nicer about it."
        "Not entirely sure what they write on coins. Sorry but I’m afraid I can’t help.":
            s "That's fine I will go find someone else who might know!"
        "I believe you mean that Italian looks similar to Latin, and that would be because Italian stems from Latin.":
            $ ranking_meter += higher_increase
            s "So thats why! Thank you!"
    return

label lang_question3:
    s "I was listening to this cool song from ERA the other day called Ameno,
        but I didn’t recognize the language. Could you help me?"
    menu:
        "Sorry but I have absolutely no clue what you are talking about.":
            $ ranking_meter -= lower_increase
            s "That's too bad, I will find someone else who does!"
        "I personally only listen to death metal, so I do not recognize the song,
            but I’m sure the Music department could help you.":
            s "Why would the Music Department know what language it is..."
        "You are in luck, I am actually a big fan of that song. If I remember
            correctly, it is actually written in pseudo-latin, so it appears to be Latin,
            but actually does not mean anything.":
            $ ranking_meter += higher_increase
            s "That's a shame but thank you any way!"
    return

label lang_question4:
    s "My friends and I were discussing our German lecture today, and we were
        confused regarding the genders of nouns. Is the cat a feminine or masculin noun in german?"
    menu:
        "God, you Language students are by far the most annoying, walking through here is always painful.":
            $ ranking_meter -= higher_increase
            s "Why are you so mean?"
        "I never learnt German, but all the members of the Pussycat Dolls were female,
            so if I had to guess, I’d say it’s feminine.":
            $ ranking_meter -= lower_increase
            s "That makes sense!"
        "I believe it would be the same as in French, and in French the cat is masculin.":
            $ ranking_meter += lower_increase
            s "I didn't know that, thats so cool!"
        "Oh I remember my great-grandmother’s youngest sister’s boyfriend when she was
            in kindergarten had a German aunt, and according to them the cat was a feminine noun in german.":
            $ ranking_meter += lower_increase
            s "Weirdly specific but solves my question!"
    return
    
label lang_question5:
    s "Latin America is a name given to a big number of countries in the Americas,
        but they speak Spanish for the most part, does this mean Spanish came from Latin?"
    menu:
        "*music blasting from Airpods* SORRY I CAN’T HEAR YOU, AND I JUST CANNOT BRING MYSELF
            TO TURN BRITTNEY SPEARS DOWN!":
            $ ranking_meter -= lower_increase
            s "Who even listens to Brittney Spears in 2021?"
        "I’m not sure I should be the one you ask, but I believe that is the reason, yes.":
            s "Oh cool, Thank you!"
        "When I was but a small young girl, I was fascinated by the fireworks we would get to
            see on the 5th of November. Nowadays I blankly stare into them and feel myself fade
            away, little by little. Oh wait, that’s not what we were talking about. Yes, my wife’s
            friend is from Panama and she actually knows a lot of Latin because of this.":
            $ ranking_meter += higher_increase
            s "... Thanks .. I think.."
    return