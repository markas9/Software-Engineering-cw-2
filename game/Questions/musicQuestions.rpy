define musicQuestions = ["music_question1", "music_question2", "music_question3"]
$ renpy.random.shuffle(musicQuestions)

label music_question1:
    s "I really enjoy the song American Pie by Don McLean, but what exactly was that song about?"
    menu:
        "Don’t get me wrong, but do I look like a walking encyclopedia or history book? Do what all you youngsters do and look it up on google.":
            s "Response"
            $ ranking_meter -= lower_increase
        "Sorry but I’m afraid I can’t help you with that.":
            s "Response"
        "I believe it was about some sort of accident that happened, I think it was some sort of fire.":
            s "Response"
            $ ranking_meter += lower_increase
        "Oh that song was about Buddy Holly’s plane crash, an excellent piece of music.":
            if creativity < 2:
                "You dont have enough creativity"
                jump music_question1
            s "Response"
            $ ranking_meter += higher_increase
    return

label music_question2:
    s "I keep having to listen to these classical pieces of string bands, but I don’t understand the difference between a cello and a bass, would you mind explaining it?"
    menu:
        "Mate, one gets used in my favorite music genre, death metal, and the other requires you to sit down and use a bow of some sort.":
            s "Response"
            $ ranking_meter -= lower_increase
        "My knowledge of music instruments is close to none, so you should ask someone else to help you.":
            s "Response"
        "The cello is smaller than the bass and gives a fuller range of sounds than the bass, which is more for low background sounds. ":
            s "Response"
            $ ranking_meter += higher_increase
        "Think of the cello like the guitar of string instruments, and the bass like the bass.":
            s "Response"
            $ ranking_meter += lower_increase
    return

label music_question3:
    s "Hey Mrs. Gadget, did you watch Eurovision? I’m a bit sad that so many countries decide to make English songs instead of songs in their native languages. It would be much more beautiful if they weren’t all singing in English."
    menu:
        "True, they should stop using our language. Brexit means Brexit, those Europeans just don’t get it.":
            s "Response"
            $ ranking_meter -= lower_increase
        "Sorry, I’ve never watched Eurovision.":
            s "Response"
        "I think that singing in English just allows them to reach a bigger demographic in an attempt to gain more points.":
            s "Response"
            $ ranking_meter += lower_increase
        "I agree with you, their native languages add to the atmosphere and are more refreshing to hear.":
            s "Response"
            $ ranking_meter += higher_increase
        "Okayyyyy you don’t even know how much I agree with you. I would love to have the Italians singing in Italian while the Spanish and French sing in Spanish and French respectively. Even the Germans could do some yodeling with the Swiss, and we could see who does it better. Even better yet, the French, Italians, Spanish and Portuguese could all send very attractive young men to sing seductively in their own languages. I bet that would really get the crowd going. I would pay good money to go see them live if they could get that to happen.":
            if creativity < 2:
                "You dont have enough creativity"
                jump music_question2
            s "Response"
            $ ranking_meter += higher_increase + lower_increase
    return

