label initGenericQuestions:
    $ genericQuestions = ["genericQ1", "genericQ2", "genericQ3", "genericQ4", "genericQ5", "genericQ6", "genericQ7"]
    $ renpy.random.shuffle(genericQuestions)
    return

label genericQ1:
    s "If a tree falls in the forest, and nobody is around to hear it, does it make a sound?"
    menu:
        "If I blew your brains out and nobody found your body, who even cares?":
            $ ranking_meter -= higher_increase
            s "Okay, I have another question"
        "Or better yet: does it matter?":
            $ ranking_meter -= lower_increase
            s "Okay, I have another question"
        "From a literal perspective yes, but the point of the metaphysical question is that you think about it, not that you get an answer.":
            if logic < 2:
                "You dont have enough logic"
                jump genericQ1
            $ ranking_meter += higher_increase
            s "Okay, I have another question"
    return

label genericQ2:
    s "Mrs. Gadget, I read your paper on OWL ontologies. Would you ever consider revisiting it for a different programming language?"
    menu:
        "That’s funny, I thought I published that paper. Why then, am I still hearing about it?":
            $ ranking_meter -= lower_increase
            s "Okay, I have another question"
        "You’d have to ask one of the other authors - I can’t take all the credit!":
            s "Okay, I have another question"
        "It just so happened that we used Java. I suppose you could do it for another language but it would have to be an object-oriented one.":
            $ ranking_meter += lower_increase
            s "Okay, I have another question"
    return

label genericQ3:
    s "Juliá Gadgetó, ¿qué año es y cómo acabé en esta tierra extraña?"
    menu:
        "Qúe?":
            $ ranking_meter += lower_increase
            s "Okay, I have another question"
        "Umm… I’m afraid I have no idea what you just said.":
            s "Okay, I have another question"
        "El año es 2021, bendito, y la fractura del tiempo te trajo aquí con un viento del destino.":
            $ ranking_meter += higher_increase
            s "Okay, I have another question"
    return

label genericQ4:
    s "Are the local legends of the WereBear true in any way?"
    menu:
        "Absolutely. I transform into a bloodthirsty monster when idiotic students waste my time.":
            $ ranking_meter -= lower_increase
            s "Okay, I have another question"
        "Not really, I can assure you there’s negligible risk of you being torn to shreds and having your mangled corpse draped in your own intestines on Walpurgis Night.":
            $ ranking_meter += lower_increase
            s "Okay, I have another question"
        "Not in the most literal of senses. But the magic and spiritualism of such folklore is that it’s true in a higher cognitive sense. So long as the WereBear exists in the minds of a populace, it can exist in non-corporeal form. It would be a good exercise for you to comprehend the many features of the myth and see what they have in common with the Jungian Shadow. ":
            if creativity < 2:
                "You dont have enough creativity"
                jump genericQ4
            $ ranking_meter += higher_increase
            s "Okay, I have another question"
    return

label genericQ5:
    s "I dropped my milkshake on the floor and my day is ruined, please comfort me before I uncontrollably cry here and now."
    menu:
        "A milkshake? What the Sam Hill is this, a daycare centre?! How about I drop you on the floor and spill your strawberry-flavoured liquid everywhere? Get outta here!":
            $ ranking_meter -= lower_increase
            s "Okay, I have another question"
        "Hear ye, cruel Gods! Claim ye this wretched student’s shake? Damn your eyes, says I! O, heartless world - when the shakes are mercilessly pulled from our grasp (time together is so fleeting), all else is but wind and sand.":
            $ ranking_meter += lower_increase
            s "Okay, I have another question"
        "Here’s £10, get yourself a new one!":
            $ ranking_meter += higher_increase
            s "Okay, I have another question"
    return

label genericQ6:
    s "Doc Gadget! You’re the only lecturer who’s on-the-level. I got into an argument with my flatmate last night, and before you know it I hit him too hard and he’s dead. I cut the body into pieces on a sheet of plastic but I really don’t know what I’m doing. Any advice?"
    menu:
        "Try Nightline.":
            $ ranking_meter += lower_increase
            s "Okay, I have another question"
        "For both our sakes in a potential courtroom, this never happened, I don’t know you.":
            $ ranking_meter -= lower_increase
            s "Okay, I have another question"
        "The Chemistry department has some barrels of lye, put the chunks in there. That will get rid of any superficial distinguishing features such as tattoos or marks on the skin, but it’s only short term. You have to get the rest out when it’s slushy enough, and make sure you get any stray teeth or bone. I would wrap it in something, a bag that won’t break, wash any blood or fluids anywhere. Burn any dirtied clothes, and put some weights, rocks or bricks in the bag. Then, rent a boat and sail way, way out to sea. When you can barely see the shore, and the bag is sufficiently weighed down, you dump it.":
            if logic < 2:
                "You dont have enough logic"
                jump genericQ6
            $ ranking_meter += higher_increase
            s "Okay, I have another question"
    return

label genericQ7:
    s "Mrs. Gadget, if you have described something as indescribable, haven’t you already described it?"
    menu:
        "daydreaming again?!":
            $ ranking_meter -= lower_increase
            s "Okay, I have another question"
        "I mean… I guess you’re right in a way… Wait you really stopped me to ask this?":
            $ ranking_meter += lower_increase
            s "Okay, I have another question"
        "This sounds like a question for H.P. Lovecraft.":
            $ ranking_meter += lower_increase
            s "Okay, I have another question"
    return