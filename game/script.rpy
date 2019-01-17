init:
    $ claire_convo = 0
    $ coffeemaker = False
    $ claireweather1 = False
    $ claireweather2 = False
    $ claireweather3 = False
    $ claireplans1 = False
    $ claireplans2 = False
    $ claireplans3 = False
    $ clairenew1 = False
    $ clairenew2 = False
    $ clairenew3 = False


define i = Character ("Ish")
define s = Character ("Sylvie")
define l = Character ("Lachesis")
define u = Character ("???")
define k = Character ("Kassandra")
define c = Character ("Claire")

image sylvie normal = "Test_normal.png"
image sylvie worried = "Test_worried.png"
image sylvie happy = "Test_happy.png"
image sylvie angry = "Test_angry.png"
image sylvie sad = "Test_sad.png"

image testpoint = "testpoint.png"
image testpoint2 = "testpoint2.png"
image testpoint3 = "testpoint3.png"
image testpoint_idle = "idle.png"


label start:

    k "... And it seems that Leo speaks of interesting revelations for his constituents today!"
    k "So, if you're born anywhere between July 23rd and August 21st, keep your eyes peeled for something truly fantastic."
    k "Now, Kira with the Arts."

    scene bg apartment
    with fade

    show sylvie normal

    i "Interesting revelation, huh?"
    i "Auntie, got anything you're not sharing with me?"
    s "Hm... Not that I know of."
    s "Oh! I did meet this guy named Ricardo."

    show sylvie worried

    s "He was... interesting."
    i "Not quite your type?"
    s "Definitely not my type of interesting."

    show sylvie normal
    s "Anywho, what've you got planned for the day?"
    i "Well, I've got work for starters. Then, I'm meeting up with Claire and heading to the Firenote concert later tonight."

    show sylvie happy
    s "That sounds like quite the full day! I hope you have lots of fun."
    i "Thanks! Do you have anything planned?"

    show sylvie sad
    s "Not really... Just work, and then planning and packing for my trip tomorrow night."
    i "Oh? Is it another business trip?"
    s "Unfortunately, yeah. This time, though, I'll be just over the bridge in Grecia."
    s "They want me to hold a presentation on something."
    i "Ooo! What's it about? Do you have any projection images?"

    show sylvie normal
    s "Not this time, though I'll need to prepare at least a small something so that they don't get bored."
    s "It's the stiffs this time around."
    i "I see."
    i "That sounds kind of awful, actually."

    show sylvie sad

    s "It is, but what can you do?"
    s "I get paid well, my work outside of the board room isn't too terrible, and I get to spend a ton of time with you, best of all."
    i "Aw, shucks. Well, I'm glad I can spend time with you, too."
    "~Ding~"

    show sylvie angry

    s "Hate to break this happy moment up, but my ride's here."

    show sylvie normal

    s "Let's order some shrimp and fries tonight. We can probably catch up on {i}Intertwined Mystery{/i} if we try hard enough."
    i "Sounds like a plan! I'm looking forward to it."
    s "Alright! See ya later."

    hide sylvie
    with fade
    "(And there she goes.)"
    "(Dang. I don't think I've ever left {i}after{/i} her.)"
    "(A little lonely, actually.)"
    "(I guess I should start making my way downtown.)"
    "(Wait, where are my keys?)"
    "(Darn. Now I've gotta find those...)"

    jump searchmenu1

label searchmenu1:
    scene bg apartment
    with fade

    menu:
        "Check the kitchen.":
            jump kitchen
        "Check the bedroom.":
            jump bedroom
        "Check the bathroom.":
            jump bathroom
        "Check Aunt Sylvie's room.":
            jump sylviesroom
        "Leave.":
            jump leaveoption

label kitchen:

    "(Shoot, I might've left 'em in the kitchen.)"

    scene bg kitchen
    with fade



    "(... Nope. Uuuuggghhhh.)"

    jump kitchensearch

label kitchensearch:

    call screen kitchen

label coffeemaker:

    if coffeemaker == True:
        "(Hm...)"

    else:
        "(Wait. Is the coffee maker on?)"
        "(If I don't turn it off, it might keep making coffee...)"
    menu:
        "Turn it off." if coffeemaker == False:
            jump turnoff

        "Turn it on." if coffeemaker == True:
            jump turnon

        "Leave it on." if coffeemaker == False:
            jump leaveon

label turnoff:
    $ coffeemaker = True
    "(Alright, that's over with.)"
    "(Let's keep searching.)"

    jump kitchensearch

label turnon:
    $ coffeemaker = False
    "(Actually, maybe I should turn it back on.)"
    "(Auntie might want coffee if she gets back early enough.)"

    jump kitchensearch

label leaveon:
    "(Oh, wait.)"
    "(These have those auto-shutoff features.)"
    "(I should really stop staying up so late...)"
    "(Still gotta find my keys, though.)"

    jump kitchensearch

label bedroom:

    scene bg bedroom
    with fade

    "(Did I leave them in here...?)"
    "(I could've sworn I put them in my purse.)"
    "(Wait. That's my purse on the bed!)"
    "(Ish, you moron.)"
    "(Alright, let's get to work!)"

    jump livingroom

label bathroom:
    scene bg bathroom
    with fade

    "(Maybe I left them on the sink.)"
    "(Though, that would mean I left my whole bag on the sink.)"
    "(I think I'd remember something like that.)"
    "(I'll check just in case.)"
    "(And like I suspected. Not in here, either.)"
    "(At this rate, I'm gonna be late to work.)"

    jump searchmenu1

label sylviesroom:
    "(Nope.)"
    "(I don't wanna think about what she might say if I go in there.)"

    jump searchmenu1

label leaveoption:
    "(Ugh, I don't have time for this.)"
    "(I'll just lock the door and hope Aunt Sylvie doesn't scold me for it.)"
    "(Though, I feel like I might be forgetting something...)"

    jump livingroom


label livingroom:
    scene bg apartment
    with fade

    menu:
        "Go to the kitchen.":
            jump kitchen1
        "Go to the bedroom.":
            jump bedroom1
        "Go to the bathroom.":
            jump bathroom1
        "Go to Aunt Sylvie's room.":
            jump sylviesroom1
        "Leave. Like, {i}actually.{/i}":
            jump leaveoption1

label kitchen1:
    scene bg kitchen
    with fade

    "(Oof. I forgot how dirty we left it yesterday.)"
    "(But, I don't think I forgot anything here.)"

    jump livingroom

label bedroom1:
    scene bg bedroom
    with fade
    "(As comfy as my room is, this might be a little counterproductive to my need to go to work.)"
    "(I {i}do{/i} like my knick-knacks, though...)"
    "(I kinda wanna take 'em with me so I can put 'em on my desk.)"
    "(... Nah. Let's just get going.)"

    jump livingroom

label bathroom1:
    scene bg bathroom
    with fade
    "(Why's it always so cold in here?)"
    "(I still don't see the point of having a bathroom heater if we don't even use it.)"
    "(It's like that time Aunt Sylvie {i}insisted{/i} on buying the waffle iron.)"
    "(She wound up regifting it to Aunt Max for her birthday.)"
    "(What a waste.)"

    jump livingroom

label sylviesroom1:
    "(NO.)"

    jump livingroom

label leaveoption1:
    "(It's a probably a good idea to get over to work now; I'm at least a half-hour away.)"
    "(And it's super cold.)"
    "(I sure hope Vice Oracle Fatima made cocoa again.)"
    "(We'll all need something to warm our bones up for sure.)"

    jump streets1

label streets1:
    scene bg apartment night
    with fade
    "(It's still a little dark outside.)"
    "(I doubt anything's open for now, so I'll have to eat breakfast at work.)"
    u "Yo."
    "(Huh?)"
    i "Claire?"
    i "What're you doing out so early?"
    c "Dad screwed his back up, so Chase is helping him out at home."
    c "As such, I'm manning the bakery today."
    i "By yourself?!"
    c "I've done it before. I'm just gonna close early today."
    "(I feel like this might be a bad idea.)"
    "(Claire did {i}not{/i} handle it well last time.)"
    "(I had to take over for her because she practically had a meltdown.)"

    jump clairedecision

label clairedecision:
    "(What should I tell her?)"

    menu:
        "Encourage her!":
            jump encourage

        "Um...":
            jump maybenot

label encourage:
    i "Well, I'm rooting for you! I hope that things don't get too hectic today, though."
    c "No promises."
    c "Well, I'm gonna go now."
    c "We're still on for after you get off, yeah?"
    i "Mhm! I'll head straight over."
    c "Alright, see ya."
    i "Later!"

    return

label maybenot:
    i "Maybe that's not such a great idea."
    c "What's that supposed to mean?"
    i "I just think you shouldn't bite off more than you can chew."
    i "Last time didn't end too well."
    c "You aren't wrong, but who else is gonna take care of it?"
    i "I mean..."
    c "Then again, even last time, Eliza and Carlo were there to help me bake."
    i "Wait, what happened to them?"
    c "Carlo sprained his wrist last week and Eliza had her baby last week."
    c "Whoo."
    i "Oof... That's pretty rough."
    c "Yeah, on second thought, you might be right. This might be a terrible idea."
    i "Seconded."
    c "Where're you headed? Work?"
    i "Yeah."
    c "I'm joining you for the walk. It'll give me some time to think up an excuse for my dad later."
    i "Heh. Think your dad'll buy whatever it is?"
    c "Probably not. I might just tell him the truth."
    i "That'd be a pretty good idea."
    c "Yeah."
    c "..."
    i "..."
    c "..."
    i "....."
    c "... You wanna come up with a topic?"
    i "Oh! Um, sure."
    "(What would we even talk about, though...?)"
    "(...)"
    "(Wait, I know!)"

    jump convo1

label convo1:

    menu:
        "The weather" if claireweather1 == False:
            jump weather1

        "Vice Oracle Fatima" if claireweather1 == True and claireweather2 == False and claireweather3 == False:
            jump weather2

        "Untrustworthy Vice Oracle" if claireweather1 == True and claireweather2 == True and claireweather3 == False:
            jump weather3

        "Today's plans" if claireplans1 == False:
            jump plans1

        "Claire's indecsiveness" if claireplans1 == True and claireplans2 == False and claireplans3 == False:
            jump plans2

        "What's bothering Claire?" if claireplans1 == True and claireplans2 == True and claireplans3 == False:

            jump plans3

        "What's new with Claire" if clairenew1 == False:
            jump claire1

        "Rose Knights" if clairenew1 == True and clairenew2 == False and clairenew3 == False:
            jump claire2

        "Mysterious document" if clairenew1 == True and clairenew2 == True and clairenew3 == False:
            jump claire3

label weather1:
    $ claire_convo +=1
    $ claireweather1 = True
    i "It's kinda cold out today, isn't it?"
    c "It's six in the morning."
    c "Besides, we're pretty close to the beach, so naturally it'll be a bit colder."
    i "True."
    c "Good weather for cocoa, though. I kinda wanna make some before I go back home."
    i "I was just thinking that! I hope the Vice Oracle made some."
    c "She makes cocoa?"
    i "Some of the best cocoa I've ever had! She makes it with milk, marshmallows, and whipped cream."
    i "If she's really in the mood, she even puts chocolate shavings on top."
    c "Damn. I didn't take her for the nice type."
    i "I can see why. She's one of those..."
    c "RBF types?"
    i "Yeah. She looks mad, but she really isn't."
    c "Hm. The more you know."

    if claire_convo ==3:
        jump atwork

    else:
        jump convo1

label weather2:
    $ claire_convo +=1
    $ claireweather2 = True
    i "Come to think of it, you don't really like the Vice Oracle much, do you?"
    c "It's not that."
    c "I just don't trust her."
    c "She has those eyes that I've seen before."
    i "What do you mean?"
    i "She just has normal eyes, as far as I can tell."
    c "No."
    c "Those are the eyes of a dangerous woman."
    c "Someone who's hiding something, like a hitman, or a thief."
    i "I mean, yeah, she looks a little mean, but isn't that a little prejudiced?"
    c "Maybe. I don't have much else to say about her, honestly."
    "(Well, if that's how you feel...)"


    if claire_convo ==3:
        jump atwork

    else:
        jump convo1

label weather3:
    $ claire_convo +=1
    $ claireweather3 = True
    i "Have you met her before?"
    c "In person? Yeah."
    c "Right after my mom died."
    i "What? Why?"
    c "You didn't know?"
    c "My mom was an Oracle for the government."
    i "Wait, {i}what?{/i}"
    c "Yup."
    c "She came by to pay her respects."
    c "However, she also came to discuss some other stuff."
    c "My dad kicked me and my brother out of the room before they got into any details."
    i "So, that's why you find her untrustworthy."
    c "Not just her, either."
    c "I was looking through some of my mom's old stuff, and I found some documents."
    i "Oh...?"
    c "Yeah."
    c "It's written plainly, but I can't... \"wrap my head around it,\" if that makes sense."
    i "No, it totally does."
    i "That sounds like a future vision, but I've never heard of an Oracle writing them down."
    c "It'd make sense. Aren't visions from gods and goddesses?"
    i "Yeah, and it's done in a way that makes it hard on us to explain to our clients."
    c "Makes it harder to change the future?"
    i "Something like that."
    c "I see. That might be why it came out as gibberish, then."
    c "But... Do you think you might be able to decipher it?"
    i "How would I be able to decipher it if it's gibberish?"
    c "No, no. What I mean is--"
    i "I'm teasing you! I'll give it a try."
    c "Ugh..."
    c "Thanks, Ish."
    i "Hey, what're friends for?"
    "(...)"
    "(Hoo, boy.)"

    jump atwork

label plans1:
    $ claire_convo +=1
    $ claireplans1 =True
    i "So what were we going to do this afternoon again?"
    c "Well, we {i}were{/i} going to chill at the bakery, but that plan's changed."
    c "So, we can do pretty much anything else."
    i "Well, we can go to the Nanite Museum."
    c "Nope. Museums are boring."
    i "The beach?"
    c "Too cold."
    i "... The--"
    c "No pet stores."
    i "I was just going to suggest the arcade."
    c "Oh."
    c "..."
    c "No."
    i "Ugh. Then what {i}do{/i} you wanna do, then?"
    c "Don't know. It's up to you."
    i "..."
    "(We'll figure it out later.)"

    if claire_convo ==3:
        jump atwork

    else:
        jump convo1

label plans2:
    $ claire_convo +=1
    $ claireplans2 =True

    i "Something wrong?"
    c "What?"
    i "I mean, you're not usually this indecisive, or passive."
    c "Oh."
    c "I'm just... not really in the headspace to make decisions at the moment."
    i "That's unusual. You're usually the one taking charge."
    c "Yeah, well. Not today, it seems."
    i "Y'know you can tell me just about anything, right?"
    i "We're like the sisters neither of us had."
    c "I know, I know."
    c "Just don't know {i}how{/i} to talk about it."
    i "I-I see."
    c "Yeah."

    if claire_convo ==3:
        jump atwork

    else:
        jump convo1

label plans3:
    $ claire_convo +=1
    $ claireplans3 =True

    i "Well, do you wanna give it a try?"
    c "Not really, but I know you're going to be annoying about it until I do."
    i "I'm glad you remember."
    c "Ugh."
    c "So, y'know how my mom was an Oracle?"
    i "Your mom was an {i}Oracle?{/i}"
    c "Yup. Worked under High Oracle Ophelia as an assistant."
    i "Wow. The more you know."
    c "Yeah."
    c "Anyway, I found some old documents of hers, and I'm not sure what they could mean."
    c "I've been trying to figure them out since yesterday afternoon."
    i "And you think they might be some kind of revelation?"
    c "It's not a far-fetched idea."
    i "Definitely not, just... Are you {i}sure?{/i}"
    c "Yeah."
    c "I was hoping that you'd be able to look at it."
    "(... Oh, dang.)"
    i "Um."
    c "Hm?"
    i "Y-yeah. I can give it a go."
    c "Alright, we'll make that the plan, then."
    "(Well, don't know how I'm gonna pull this off, but I owe her a try, at least.)"

    jump atwork


label claire1:
    $ claire_convo +=1
    $ clairenew1 =True
    i "So what's new with you, sis?"
    c "Not a whole lot."
    c "Thinking about joining the Rose Knights this summer."
    i "WHOA! Seriously?"
    c "Yeah. I've been considering it for a while."
    c "I'd rather use my talents for something useful, y'know?"
    i "You don't think teaching kids magic is useful?"
    c "Eh. Maybe for them."
    c "I'm just tired of working at the bakery."
    c "I need something... {i}exciting{/i} in my life."
    i "Like a fox for the hunt."
    c "Yeah, something like that."

    if claire_convo ==3:
        jump atwork

    else:
        jump convo1

label claire2:
    $ claire_convo +=1
    $ clairenew2 =True
    i "I remember you saying you'd never join the Rose Knights."
    i "What changed?"
    c "Ugh, I forgot that you remember that."
    c "Well, recently, I've been looking more through my mom's things."
    c "Do you remember how she was an Oracle?"
    i "Wait, really? She was an Oracle?"
    c "Yeah, for like ten years. She worked right under High Oracle Ophelia."
    i "Wow... That's kinda wild."
    c "Yeah."
    c "Anywho, I was looking through her stuff, and I found a document."
    i "Oh?"
    c "Yeah. It's all in gibberish, though."
    "(I don't like the sound of that...)"

    if claire_convo ==3:
        jump atwork

    else:
        jump convo1

label claire3:
    $ claire_convo +=1
    $ clairenew3 ='True'
    i "Any idea of what's on the document?"
    c "Not really. I was hoping you'd know something about it."
    i "I mean, the only thing I can think of between gibberish and Oracles is a future vision."
    c "What?"
    i "Yeah. What, you didn't think we just {i}get{/i} our visions, do you?"
    i "Nah, we've gotta work for it. And then we have to figure out how to tell everyone else what we saw."
    i "It's rough work."
    "(Nailed it.)"
    c "Hm. Well, in that case, I think I've got the right girl."
    c "Do you think you can tackle it for me?"
    i "I, uh..."
    "(Oh, no.)"
    "(My lies finally caught up to me.)"
    "(Wait... Maybe not...)"
    i "Yeah, sure. I'll give it a try."
    c "Thanks."
    c "That means a lot to me."

    jump atwork


label atwork:
    "(Ah, here we are.)"
    c "So, this is the Great Temple of Ilya."
    c "Looks kind of intimidating up close."
    i "You've really never seen it before?"
    c "Nope. Mom always kept me away from this place."
    c "Plus, most of my business is towards the Market District, not near the government sector."
    i "I see. Well, hopefully I can give you a tour someday."
    c "Don't count on it."
    c "This place creeps me out."
    i "I... Hm."
    c "Catch ya later, Ish."
    i "L-later!"
    "(... Geez.)"
    "(Welp, here I am at work again.)"
    "(That... place I don't belong in.)"


    return
