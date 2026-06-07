define config.default_text_cps = 30
define you  =  Character("[name]" , coloir =  "#FF0000" )
define aunt  = Character("Aunt")
define commentator =  Character("Commentator")
define ev  = Character("Evidence group")
define commissioner  =  Character(" Comissioner")
define facilitator  = Character("Facilitator")
define salesman = Character(" Salesman")
define vet  = Character(" Former Vateran")
define roxy  =  Character( "roxy")
define friend = Character("Hiccup")
define hacker  = Character(" hacker")
define left  =  Position(xalign = -1.75) 
define slightleft  = Position(xalign  = 0.0)
define center = Position(xalign = 0.5)
define right  = Position(xalign = 4.5)
define slightright  = Position(xalign = 1.0)
define slightrightmore = Position(xaligh = 3.0 )
transform double_zoom:
  zoom 1.5

  


label start:
  show bg room
  "After the war ended the  people  felt the consequences of it’s"
  "the broken  country stabbed the people with "
  "  depression" 
  "  poverty "
  "  hunger"
  " and  the  loss of loved ones "
  "people had lost all the  hope from the government"
  "the last option for the government is to listen to the country people"
  "and so they started the" 
  "citizen assembly"   
  jump morning


label morning:
  window hide
  show bg act1
  with fade
  
  pause 2
  
  
  window show
  hide bg act1
  
  show bg room
  with fade
  "before taking my leave for my friend house"
  "which is no longer in this world" 
  "why…"
  "because he was in the army  and got shot during war"
  "today "
  "I am going to visit his mother"
  "for the letter he gave me for her mother "
  "I couldn’t give her before "
  " because I was so terrified  of her mother..."
  " the only son she have that she lost "
  " i don't want to give her a trauma"
  "but today I will give it to her no… "
  "I need to "
  "...."
  "its my duty"
  "as his best friend "
  "as I was leaving the house "
  "I got a letter .."
  "from the  citizen assembly "
  "as a   lucky 100  person to join it .. "
  "at first I want to laugh at the letter "
  "that what are they excepting... "
  "from the people..."
  "from just a mere citizen "
  "before leaving i send my name with the letter to the assembly"
  $ name =  renpy.input("enter your name citizen")
  $ name =  name.strip()
  you "I take my leave for my friends house"
  you "its just a 15 min bus ride far"
  show bg door
  with fade
  you "I knock on the door "
  you "...."
  you "...."
  you "...."
  you "I thought no ones at the home "
  you "... but suddenly a lady"
  you "open the door slowly..."
  show grandma neutral
  you "It was her mother "
  you "Ohh good morning  aunt "
  aunt "ohh you are my sons friend sir right?? "
  you "yes"
  aunt "Come come"
  aunt "my son used to talk about you a lot"
  aunt " how you.."
  you "she was looking paler than before  "
  you " wrinkles all over her face"
  you " it feels like she age 10 years more than her actual age "
  you "wearing a black coat "
  hide grandma neutral
 
  show bg grannyroom
  with fade
  you "She provided me some tea and biscuits " 
  you "we talked to some random stuff of here and there  "
  you "about how brave her son was.."
  you " I think she calmed down now from before"
  you " and accepted the  truth of his son as well "
  you "I think I can give her the letter now.......... "
 
  menu lettergiving:
    
    "give letter ":
      jump after_giving_letter

  label after_giving_letter: 
    show grandma neutral 
    you "Ahh.."
    you "aunt this is a letter given by your son "
    you " i can see her shocked face"
    you "I am sorry I cant give you before  "
    you "I thought its not the right time .... "
    you "to give when you had such a nightmare  "
    aunt "ohh …."
    aunt " It’s okey thank you for your concerns  "
    you "I can see on her face  that she will  cry while reading"
    you "losing her only child  "
    you " surprisingly ..."
    hide grandma neutral
    show grandma happy
    you "she didn’t cry instead she had  a proud look over her face "

    you "I am glad though "
    you "I don’t want to see a old grandma crying "
    aunt "thank you for providing me this letter "
    aunt "my mind is clear now "
    you "no no don't thank me "
    you " i didn't do much"
    you " i am still currious what's in the letter "
    
    menu letterasking:
    
      "ask for what's in the letter":
        jump letterask
      "don't ask for the letter ":
        jump letterasked

    label letterask:


      jump letterasked


    label letterasked :
      aunt "when he didn’t think before "
      aunt "signing for the war "
      aunt " i realize how  patriotic he is for his country"
      aunt "if i want i just can send him to some other country to study "
      aunt " but he choose to fight "

      you "yes you right "
      aunt "by the way.."
      hide grandma happy
      show grandma neutral
      aunt "do you know about the citizen assembly "
      you " ahh yes i am also...."
      aunt " i heared that its gonna be an important assembly .."
      aunt "for the future of the country   "
      aunt " wheather the we should fight for a next war or not.."
      aunt "citizens are raging and angry ..."
      aunt "they want revenge.. "
      aunt " govenment cannot decide if this will be right move or not"
      aunt "in the assembly they are definitely make an... "
      aunt " argument for the next war "
      you "ahh"
      aunt " more war more death "
      aunt "no.. my son gave his life to stop the war not to start a new war "
      you " + i stay silent and listen to what she say's i didn't say anything on that moment... +"
      you " after talking to her a little bit more  i decided to take my leave "
      you " + i didn't say anything abut me being a member of the citizen assembly +"
      you " + i dont want her to have her hopes on me .... +"
      hide grandma 
      hide grannyroom
      
      show bg door
      with fade 
      you " okey aunt i am going home now "
      show grandma happy
      aunt" ohh you leaving why not have dinner with us"
      you " no no its fine"
      hide grandma happy
      you " i take my leave "
      you " while taking the bus ride for the home.. "
      you " even though i don't want to put aunt hopes on me "
      show bg room
      with fade
      you " i still wanted to grant her wish "
      you " and i decided as a member of the citizen assembly i do everything to stop the next war"
      you " next day i take my leave for the assembly "
      you "assembly was held at the central building which is 2 km far from the parliment and major government bodies "
      you " i realize that politician will definetly be involve in this matter "
      you " i go insde the assembly talked to one of the facilitators show my  pass to them "
      you " and got my card in which there was my name , age  ,  profession  and extra information related to me "
      hide bg room

      show bg assemblyroom
      with fade
      pause 1.0
      show commentator neutral
      commentator"welcome 100 lucky citizen .... "
      commentator " now the country fate is on your hands "
      commentator" welecome to citizen assembly"



label at_the_assembly:
 
  commentator "I hope everyone don’t have any difficulty coming here "
  commentator"for next ,.. 7 days we are going to take care of everyone here "
  commentator"so this country can have a solution for all this problems"
  commentator"well even if a solution not come we all can have free coffee"
  commentator"ha ha ha ...."
  commentator"Just kidding "
  commentator"we are not here to just talk and for coffee we are here for a solution "
  commentator"so I want everyone with different experiences and different role in their life to make the best decision For this country "
  commentator"We have many people to help you with ..."
  commentator"me as the commentators ..."
  commentator" the facilitators , Evidence group  , stake holder  ,  implementation team  , commissioner and many more "
  
  menu optionalname:
    
    "what is the role of stake holder":
      jump stakeholder
    "what is the role of commissioner":
      jump commissioner
    "what is the role of coffee":
      jump coffee
      
label stakeholder:
  "to ensure all points of view of the issue being discussed are represented."
  " They help influence how the assembly is designed. Super important to get this group right to avoid bias."
  jump continueassembly

label commissioner:
  "They set up the assembly.."
  " Usually a public authority (like a local council), or a civil society organisation."
  " Responsible for ensuring the assembly achieves actual outcomes. "
  jump continueassembly

label coffee:
  "It plays a significant role in enhancing mental alertness, improving cognitive functions, and providing energy."
  "I don’t think we need to discuss about coffee for now though .. "
  "but I like coffee so I think we can drink together some day do you want my contact number"
  


  menu contactasking:
    
    "yes":
      "here you go.."
      "9999999999.."
      jump continueassembly
      
    "no it's okay":
      " okay no problem"
      jump continueassembly

label continueassembly:
  commentator"in these assembly of 7 days we talked about problems regarding..."
  commentator"poverty , hunger , ecnomey and most the important topic of citizens demanding for the next war"
  commentator"should we conduct a war or should we ignore them "
  commentator" for the next 4 days our topic will be on poverty and hunger .."
  commentator"because its major reason of the anger and rage of the citizen "
  commentator"we are going to distribute everyone in a  group of 10 to discusse about the problem .. "
  commentator"and later for solutions "
  commentator"you don’t need to feel hopeless the facilitators and evidence group is going to help you"
  commentator"i want everyone to grab a coffee"
  you " i grab the coffee as said and the facilitators guide me to a group of peoples"
  you "i take my seat and sit down .. "
  hide bg assemblyroom
  hide commentator neutral
  show bg plain
  with fade
  you "hmm.. noboady is saying anything  "
  you" ahh .."
 
  show commisioner happy at center
  with moveinleft
  commissioner "okey everyone I hope everyone having a good time"
  
  commissioner "- So does anyone wants to say about why we choose our first topic on hunger and poverty??"
  
  
  show salesman neutral at slightright
  with moveinright
  
  
  salesman "isn’t it obvious everyone in the city can’t even buy a single piece of bread and beggars are all on the streets"
 
  salesman "people are coming to roads marching for their lives  "
  

  commissioner" well yes... anyone else???"
  menu firstdiscussion:
    
    "talk about rising of inflation ":
      "Well the rise of inflation is too much even the upper middle can’t afford the goods and servies "
      jump continueassembly2
    "talk about war":
      "Well if we don’t take part in the next war I think the hunger and povet…"
      commissioner" i think we should stick to the topic for now we can discuss about war later"
      "but...."
      jump continueassembly2

label continueassembly2:
  show ev smile at left 
  with moveinleft
  ev " lets first try to compare  the post war effects … "
  ev " well so the global marked has dropped to 35 percent with Increase in global inflation in Germany and Ukraine"
  ev " still better than our boarder country with total currency collapse and a destroyed economy "
  ev " and at last our country with a moderate inflation of 35 percentage"
  ev " Within next 6 months with the help of our neighbouring country we can reduce to at least 15 percentage but I don’t think its possible for now "

  menu whynotpossible:
    "why not possible":
      hide commisioner happy
      show facilitator neutral  at slightleft
      with moveinleft
      facilitator"The neighbouring country also felt a heavy loss …there could be minor trade but it’s not going to be enough the country needs to stand on their own foot"
    
        
      menu optional_name:
      
        "ask why inflation goes to 35 percentage ?":
          jump inflation
   
        

        
      jump inflation

    "ask why Germany and Ukraine have high inflation ?":
      hide commisioner happy 
      show facilitator neutral  at slightleft
      with moveinleft
      facilitator"Both are active frontliners in the war with heavy trade restriction from neighbhour country ..."
      facilitator" also  printing money for war devalues their money internationally "
      
      menu moneydevalues:
        
        "ask how printig money devalues their currency":
          ev "its basically more money tends to go for the same amounts of goods and services  "
          ev" This can result in higher prices for goods and services, as businesses and sellers adjust their prices in response to the increased availability of money"
          jump inflation
        
          
        "ask why inflation goes to 35 percentage ? ":
          jump inflation
        


label inflation:
  ev "  Well the main reason of inflation is of the lost of the country north land"
  ev " that we lost in the war.. our major goods  and manufacturing factories were there so the supply chain broke…"
  show salesman angry
  salesman "- that’s the one of the reason we can’t give our land "
  salesman "our homes to enemy hands  we should conduct a war against the enemy  as soon as possible what’s the need of even a citizen ass.. "
  
  facilitator "sir I know that the country citizen wants their land back but if we put a fight right now then the  situation becomes even worse "
  show veternan neutral at right
  with moveinright
  vet "you think war is a child play kid "
  salesman " what do you think you are..  "
  vet"you think you know more than a Former veteran ... "
  ev " even  we fight right now america and other nation will try to intervien"
  vet "even if we don't participate in the war they will still  going to intervien with our goverment"
  facilitator " okay okay i think we are going off topic now "
  facilitator "  we should discuss about the problems currently we have .."
  vet"hmmph"
  ev " yeah so .... the next report is related to hunger and food shortage problem"
  ev " government have few ways to handle the food shortage problem so it's still not a major problem"
  ev " currently because of our supply chain broken the problem aroused a little but the harvesting season is near"
  ev " so we can deal with it for now but i still want solution realted to it.. later "
  menu foodshortage:
    
    "what are we going to do until the harvesting season ":
      ev  "right now we can import cheaper food from other countries and limit our exports "
      ev   "for now we need to stop citizen from going into a panic state "
      vet  " we need to stop the  black market they are  taking  advantage of the situation "
      facilitator " yes we also have resereve food for later if the emergency comes to us  "

      menu foodshortage2:
      
        "who are we going to prioritize cities or rurals ":
          salesman" isn't it obvious cities is much important there are many saleryman like me "
          salesman " and they are the most active in this whole drama "
          facilitator" hmm "
          facilitator " what do you think about this roxy? "
          hide ev smile
          show roxy neutral at left
          with moveinleft
          roxy "huh ..."
          roxy "...."
          roxy "...."
          roxy " yeah i think cities is more important right now"  
          vet " huh.. what are you talking about ?"
          show roxy sad at left
          roxy " ahh? i mean is that .."
          vet " you think villgers  are not going to see this unfair distribution "
          show roxy happy at left
          roxy " ahh yeah"
          vet " they are also important citizen of our country "
          vet " if they realize that their is a unfair distribution of food with them"
          vet " then that would be turn into a new problem to face "
          you " hmm they are also the one who does the major food production "    
          show roxy sad at left
          roxy " ahh sorry"
          facilitator " okey okey don't make roxy feel guilty"
          you " ahh okey.."
          facilitator " roxy is important asset in this assembly she have a lot of experience"
          facilitator" she have currently three NGO's running in our country also she cooperate with many internation commities "
          facilitator " and now she in the citizen assembly "
          vet " ohh and what kind's of NGO's you are currently running "
          show roxy happy at left

          roxy " ahh ..."
          roxy "ahh .. 2 in villages  ,  1 in a city focuisng on shortage of food and providing shelter in emergency situation  "
          roxy " we also have partnership with landlords and  small farmers to help them distribute their harvest in nearby areas "
         
          roxy " and we are also raising funds for internatinal aid  "
          roxy "ahh ...that's all we do "
          show roxy neutral at left
          roxy " we ... i am sorry we don'd do muc.. ohh yes ... we also do free health checkups on sunday"
          vet "..."
          vet "is there anything else you miss.. "
          roxy "ahh noo noo.."
          facilitator "well i think we should take a break from here until then why don't everyone  go and take a coffe break"
          you " okay...."
          hide veternan neutral
          hide roxy neutral
          hide salesman angry
          hide facilitator neutral

label break:
  
  you " +i didn't think of  a break this early+ "
  you " +but...+"
  you " +i don't think everyone just want a war to happen in this country... but the war supports opinion are also not wrong+ "
  "???" " umnn.."
  you " ahh..... oh hello "
  you " +I didn’t realized she was beside me +"
  show roxy happy
  pause 1.0
  show roxy neutral
  roxy " umnn i just have a question from you regarding the war atmosphere "
  roxy " are you in  favor of war?? "
  menu importantquestioin:
    "are you in favor of war?"
    "Yes":
      you " i mean if we can take the landback then i don't think there's a problem "
      you " but you know.."
      you " its not easy even though every country is struggling with financial and national security"
      you " and this could be the perfect chance to attack"
      jump break2

    "NO":
      you " no war is not the solution of every problem i think we should discuss about it more  "
      jump break2

label break2:
  default alliance  = False
  roxy " hmm "
  show roxy angry
  roxy " i .. am against this fight "
  roxy " there are childrens in the schools where we supply foods and i want to help them "
  roxy " we should focus on our literaccy rate rather than sending them in a war"
  roxy "I want to open more school for the childrens " 
  roxy "but with the current situation going on its getting difficult to run the NGO's" 
  show roxy happy
  roxy "so i want to form an alliance ,  when the voting happens i want you to support me "
  menu allliance:
    
    "do you want to form an alliance with roxy"
    
    "yes":
      you " okay i am also thinking the same let's stop this war"
      roxy " ohh thanks a lot"
      roxy " well we need more member in future  "
      $ alliance = True       
    "no":
      you " i respect your offer but i think i will need some time regarding the matter...  "
      roxy " ohh okey its fine you can join when you like to join"
      
label break3:
  roxy "looks like the everyone is going back to their discusion table i meet you next time at the coffee point "
  you " thanks for your offer"
  roxy " no its fine thanks for listening "
  hide roxy happy
  you "+ we both went to our table and start debating more regarding the topic ... +"

label endingassembly:
  show facilitator happy
  facilitator " okay everyone i hope everyone have a good time today before ending the day i want everyone to think of solution regarding this matter  "
  facilitator "tommorow will will going to do our first voting "
  facilitator "thank you for everyone to join in"
  hide facilitator happy
  you " ahh finally "
  you " now i can go and sleep "
  "??" " hey are you having fun"
  you " woah..."
  show guitarist happy
  friend "it's been a while ..."  
  friend "how come a life saviour come to all this politics  "
  you  "look who saying"
  you "i dont think a pop singer needs to be here though "
  you "  what happen did your fans leave you or what "
  friend " ha ha my fans are loyal to me and to my band ,if i start a new party for the election i take all the vote easily"
  you "i hope you don't "
  friend"did you say something ... "
  you "no no nothing"
  you "i am going to my hotel now ,  meet you tommorow"
  friend "bye bye and listen to my new song it's released yesterday "
  friend "and i have a show day after tommorow "
  you " yeah yeah"
  hide guitarist happy

label assemblysolutionday1:
  you " hahh.. time to think of a solution "   
  you "let try to create a solution with the information given by the evidence group "
  if alliance:
    you "ohh i can talk to roxy for more better solutions"
    menu callroxy:
      "should i call roxy"
      "call roxy":
        "Beep Beep ..."
        "Beep Beep ..."
        roxy " Hello ..."
        you " ohh hii roxy" 
        you "i just wanted some help regarding the solutions "
        roxy " ohh its fine [you] ,  working in group or assemblies can be quite hard "
        roxy " what's your problem"
        menu tellingroxyproblems:
          "what problem do you have"
          "how do i create a strong solution ":
            roxy "this is a citizen assembly so i don't think you need to think about everykind of citzen"
            roxy " just create a solution which is problamtic to you"
            roxy " every citzen solution is going to be respect to their everyday life problems or if not it be genric problem "
            you " ohh thanks a lot i try to use your advice to create a solution "
            roxy " just try to make a solution so  majority of the people can be accept"
            roxy " their will never be a solution for everyone"
            roxy " okay i am going now bye "
            you"bye "
            "Beep"
            you "let's see what kind of  document evidence group give us " 
            
            

          "how can i get more information ":
            roxy "well currently the best material you can get is from assembly itself"
            roxy "there are even some documents that's not even common to citizens "
            roxy "if you want extra information there always books and internet  "
            jump findingsolution1 
            
        
      "do not call roxy":

        you "she must be tired  with all this work today "
        you "i call her later"
        you "let's see what kind of  document evidence group give us "
        jump findingsolution1

      

    
  else:
    you "i think it should be better if i just form an alliance with roxy now it's really a hurdle to think all of it by myself "
    you " let's see what kind of document evidence group give us " 
    jump findingsolution1
                                   
label findingsolution1:
  show bg warpapers1
  with fade
  pause 2.0
  show bg warpapers2
  with fade
  pause 2.0
  show bg warpapers3
  with fade
  pause 2.0
  show bg warpapers4
  with fade
  pause 2.0
  show bg warpapers5
  with fade
  pause 2.0

  " beep beep ...."
  roxy "hey watch the news quickly "
  you " why..."
  roxy " just watch..."
  you "..... "
  show bg plain
  " the first decision that comes from the citizen assembly is ...."
  you " wait what "
  " that the government is going to increase the rate of salt   "
  you "SALT !!!"
  "because of ecnomic pressure they are trying to increase the rate of salt  "
  "this is what assembly are doing they are now going against their own country by increasing the rate of salt  "
  " such a essential mineral ..."
  roxy " did you see the news "
  you "what are they talking about ... "
  you "we didn't even discuss the solution  "
  roxy "i try to contact the assembly but authorities are not responding "
  you " what we should do ..."
  roxy "...."
  roxy " let's wait for tomorrow for now we need to discuss in the assembly"
  you " you think the public is going to keep in rest till" 
  roxy " i don't know"
  roxy " but the assembly security is good enough to hold them so i think we will be fine "
  roxy " okay i meet you tomorrow"
  you " hmmm okay"
  you "let's see what we can make as a solution"
  $ solutionmaking  = renpy.input("write a solution")
  
  you " okay it's done time to go for sleep "
  you " i hope tommorow everything goes fine"


  label assemblyday2:
    you " i reached the assembly at the morning i can see the rumbling between people  "
    
    "stranger1" " hey did you hear the news "
    "stranger2" "i heared that the citizen started attack on the govt infra  "
    "stranger3" " yeah  yeah they lit fire on buses "
    "stranger4" " hey are we even safe from all this "
    "stranger5" "they made their own decision without telling us "
    "stranger6" " what's the point of assembly if they want to make changes on their own"
    "stranger6" "also they are saying that citzen assemb..... "

    show commentator neutral 
    with moveinbottom
    commentator "okay everyone calm down i know you alre.. "

    "what's the meaning of all this ?"
    "yeah are you trying to kill us ? "
    " if you don't want assembly we can leave right now "
    
    commentator " i ... know you all have doubts regarding this but listen we are also"
    "Shut up .."
    "...."
    commissioner " give me the mic "
    commentator  "yeah "
    
    hide commentator neutral
    show commisioner neutral at center
    with moveinbottom
    
    commissioner " listen everyone !!!!"
    commissioner "you are not like any citzens you are the citzens of the assembly "
    commissioner "right now we need to think carefully this is a national emergency "
    "what about the news towards the  assembly...."
    
    show facilitator happy at left
    with moveinleft

    facilitator "i think it would be better to listen to  what commissioner had to say first"
    facilitator " i want everyone to take a seat and calm down "
    you " as the facilitator said we all decide to take the seat and listen to them "
   
    commissioner "so the news that came yesterday was all a rumor"
    " wait what then why everyone in the media is saying that we took this decision"
    commissioner " the media had already  claim their fault for all of it"
    hide commisioner neutral
    hide facilitator happy
    
    show commentator neutral at center
    with moveinbottom
    commentator " the panic that created between people is now calm down "
    commentator " so you guys don't need to worry about your life"
    show veternan neutral at right
    with moveinright
    vet  "and why they started this stupid rumor "
    commentator "well from what they say that the assembly contact them and told them to broadcast all about this salt thing  "
    salesman " and  who  told them to talk all this rubbish  ? "
    commentator " well we still couldn't find out about it "
    show salesman neutral at left
    with moveinleft 
    salesman " as expected... "
    commentator "whatever we are going to continue the assembly as how its was "
    show roxy neutral at slightleft 
    with moveinbottom
    
    roxy " what if the same thing happens next time"
    commentator " the best we can do is  try to prevent that this doesn't happen "
    vet " is there a chance that a someone from this assembly does it "
    commentator " ....."
    commentator " ....."
    commentator " there's a chance"
    salesman " wait what, why someone is trying to create chaos to it's country "
    commentator "who knows but don't worry we try to prevent it anyway that this does not happen "
    vet "i hope you take your words"
    commentator " well let's start our dicussion after a coffee break we are going to listen to your solution and conduct a voting  "
    commentator " so everyone calm your head and let's continue what we are here for  "
    "fine ...."
    "whatever..."
    hide roxy neutral
    hide salesman angry
    hide veternan neutral
    hide commentator neutral

    show bg plain
    
    show roxy happy at center
    with moveinbottom
    roxy "ohh hey [you] "
    you " ahh hello roxy"
    roxy " so what do you think about the rumor stuff?"
    menu rumor:
      
      "talk about the traitor ":
        you " i guess it's a work from a member of the assembly"
        roxy " hmmph "
        show roxy neutral at center
        roxy "rumor just after the first discussion  "
        you " also blaming the citzen assembly "
        roxy "too be honest this assembly is suspicious to me "
        jump hackerentry
      "talk about  assembly":
        you " if the thing is that they are blaming the assembly "
        roxy "heads of the assembly is also taking this lightly  "
        you " yeah don't you think they should stop the assembly if someone inside the assembly is spreading fake news "
        show roxy angry at center
        roxy "too be honest this assembly is suspicious to me "      
        jump hackerentry

label hackerentry:

  hacker " they are suspicious "
  show roxy neutral at center
  show hacker angry at left
 
  
  hacker " i knew something was off first this sudden assembly and now this rumor"
  roxy "...."
  you " ...."
  roxy " may i ask who are you? "
  show hacker neutral at right
  hacker "one of the members of this assembly "
  hacker "look at these papers roxy you are the most experienced one here what do you think about all this ?  "
  roxy "what are these .... "
  roxy "......"
  roxy "......"
  show roxy sad at center
  roxy ".........................are you serious?"
  roxy ".... how ? .. "
  roxy "wait does that mean ........ "
  
  you " what happen explain me?"
  show roxy neutral at center
  roxy " how did you get these papers"
  show hacker thinking at right
  hacker " well you can say i breached their security online "
  hacker " they know that someone breached it but they still could't find out who did it "
  hacker " as expected.........."
  
  you " what are you all talking about "
  roxy "what if i told you that this citizen assembly is a fake citizen assembly whole time  "
  you " what does that mean that's the only place where they are holding this one week assembly "
  you "they are also providing us free coffee and hotel to live and .. "
  roxy "that's not what i mean "
  show roxy angry at center
  roxy "what i mean is that they have already made the decision of the assembly"
  
  you " huh.. wait.. "
  you " then what's the point of doing a citizen assembly and what the's decision! "
  show hacker angry at right 
  hacker " hey lower your voice "
  you " ohh sorry"
  roxy "looks like the internal discussion is gone wrong and the allies country is not supporting us for the war"
  you "huh ... and what about our enemy country  "
  hacker "there's nothing written about them but looks like they are not going for the  war "
  hacker " but regarding the national security they are trying a new strategy"
  you " what? "
  hacker "they are trying to launch a biological wepeon  "
  hacker " its estimated to kill 75 percent of world polulation"
  you " hey wait wait wait ..what ,  are they on drugs or something"
  you " and what about us ?"
  hacker " they have a vaccination for our country so we will all be immune   "
  hacker " they want to balance the whole world to our country so there's no one sided war "
  you "wait... still we can't kill the whole world like that   "
  hacker "well that's the plan for now "
  you "so what the point of a citzen assembly for why don't they just use the weapon "
  hacker " currently i think is to keep the watchdogs away "
  you  "and then what should we do now ?"
  hacker" that's the reason i came here to talk to roxy  "
  roxy "the only connection i have with  government is from the government funding agency "
  hacker " that's doesn't work "
  you "we need someone who have close connection with government so we can change their plans  "
  roxy " do you know any of them "
  hacker "i think that saleryman works close with the government  "
  roxy " what really"
  you "i don't think he will help he 's in favor of the war this whole time  "
  hacker"this is not war this is a mass murder without telling anyone about it  "
  commentator "okey everyone we are going to start the discussion in next 2 minutes so comeback to you tables"
  roxy "well let's get back to our seats for now we talk about this next break  "
  you "fine "
  hacker " yeah"
  you "i try to talk to some trust worthy who can help us "
  hacker " are you sure ??"
  roxy " this can be dangereous there's already a member from the government "
  you " don't worry i try not to do anything reckless"
  roxy " fine "
  hide roxy 
  menu whototell:
    "who do you want to trust"

    "commissioner":
      you "i told everyone thing to commissioner "
      you " everything related to the weopen and related to fake citzen assembly"
      show commisioner neutral
      
      commissioner " i see ... i see ..."
      commissioner " don't worry i can talk to them don't worry about it "
      commissioner " by the way how did you get this papers "


      menu tellabouthacker:

        
        "tell commissioner about hacker":
          commissioner "ohh really a guy from the assembly breached their security  "
          commissioner " we really need to improve our security i guess"
          commissioner " by the way can you come with me to the office i need some documents to carry "
          jump ending1
        "do not tell comissioner about hacker ":
          commissioner " okay if you don't want to tell its okay"
          commissioner " by the way can you come with me to the office i need some documents to carry "
          jump  ending2
      
    "saleryman":
      show salesman neutral
      you "i told everyone thing to saleryman "
      you " everything related to the weopen and related to fake citzen assembly"
      salesman " hmmm hmmmm"
      salesman " i can understand what you are trying to say  "
      salesman " but i don't work that deeply with the government that i can change their opinion "
      salesman " i am against this but i don't think i can help you with this  i think you should talk to commissioner about this "
      hide salesman neutral
      jump whototell

    "veteran":
      show veternan neutral
      you "i told everyone thing to the Veteran "
      you " everything related to the weopen and related to fake citzen assembly"
      vet " hmmm ... hmmm"
      vet " hahah haha "
      vet " what a plan i can't imagine our government can play that dirty "
      vet " don't you think it's a good plan it's better than nuclear missiles "
      vet " before they can even figure out who did this there country is done for "
      you " ahh i am sorry i don't think i ..."
      vet " it's okay kid i can understand what you mean"
      vet " the voting is going to start now ,  we can talk about this later"
      vet " vote whoever you want now i am not even interseted in this voting "
      you " yes and thank you for you cooperation"
      hide veternan neutral
      jump votingtime




label ending1:
  roxy " the next day both hacker and [you] didn't come to the assembly"
  roxy " how am i going to solve this problem by myself"
  commissioner " umnn roxy mam"
  roxy " yess!"
  commissioner "yes ... can you come to my office there's some documents can you carry them for me"
  "roxy  , hacker , [you] all three of them get's eliminated by government "
  "ENDING 1"
  return

label ending2:
  roxy " the next day [you] didn't come to the assembly"
  roxy " how am i going to solve this problem with hacker "
  hacker" did you see [you] him today "
  roxy " no "
  hacker " whatever let's get back to work"
  hacker " i knew we can't depend on [you]"
  roxy " but ... "
  roxy " whatever let's go they are starting"
  "[you] get eliminated by the government"
  "ENDING 2"
  return

  
  
  

label votingtime:
  you " after a lot  of discussion related to our solution the time have come for the voting"
  you " the only three solution that can come for the final voting are from roxy  , hacker  , and me  "
  roxy " if we take the help of my NGO's and my funds from international committee we can stablize the panic "
  salesman "we just need to take our land back and we get our food banks and factories the supply chain will work and panic resolve "
  you "[solutionmaking]"
  menu vote:
    "which solution do you want to vote"
    "you":
      jump votingresult

    "roxy":
      jump votingresult
          
    "saleryman ":
      jump votingresult      
  
  
label votingresult:
  "roxy solution with 45 percent of votes "
  "saleryman solution with 5 percent  votes "
  " [you] solution with 50 percent  votes"
  show commisioner happy at center
  commentator" with the voting is clear that the solutiion the assembly going  with [you] solution  "
  commentator "thank you every citizen of this country for participating for our first voting  "
  show veternan happy at Right
  vet "so what's the next problem now "
  commentator "well the next problem is about the ecnomy conditions and connections with our allies country  "
  commentator "let's start our meeting as we are low in time today  "
  show roxy happy at Left
  roxy " umnnn can we take a little break i am not felling good and my throat is also not okay "
  commentator" but ... it's only take a hour so i don't thi.."
  facilitator " its okey the citizens is our first priority here"
  
  facilitator " we are going to take a 10 minute break so everyone relax yourself"
  hide commisioner happy
  hide veternan happy
  hide roxy happy
  hacker " good job roxy "
  show hacker thinking at center
  you " good she make time so we can discuss now what to do"
  "everyone starts to go where they can relax "
  show roxy neutral at right
  roxy "so is there anyone you talk to "
  you " yeah he is a "
  show veternan happy at Left
  vet "hello i am the previous veteran of this country army i am sorry that you lost your precious land "
  roxy " no no beacause of you and your people we are still living "
  hacker " ahh so are you in close relation to the government "
  vet " if you say so yes i used to be but right now i am not  "
  hacker " can you do something related to the problem we are facing "
  vet " biological weopen huh "
  vet " do you know who's the member who spread the information regarding salt?"
  roxy " no we don't"
  vet " I .."
  hacker " even if we know , we don't try to talk to him"
  you " yeah that's right and how do we even find him he's not doing any moment since the rumor"
  vet " i know who started the rumor "
  roxy " wait what"
  vet "there's him  "

  roxy " that's salesman ??"
  vet " he's the current veteran "
  you "don't tell me , that's why he so in favor of this war thing  "
  hacker " so he's making a disguise and try to start a war"
  vet "yeah he is concern that the government will listen to the assembly "
  vet "he's a new veteran so i don't think he knows about this weopen thing"
  hacker "still we can't tell him about this he's dangerous to tell him "
  ve " no .. even if he in favour of war he's still used to be good soldier who used to fight for his country"
  vet " he can still work for us "
  roxy " hey wait are you serious i don't believe this guy and what plan do you even have in your mind"
  vet " what plan we could have our government is against us  ,  the best bet we can take is take the support of the world"
  hacker " are you saying we are just going to spread this information to the world"
  roxy " but isn't it better to just stop them from doing it " 
  roxy " if we reveal this to world the government could go against us "
  vet "so what are you thinking just tell them to stop their biological weopen "
  vet " tell them and you are executed the next day"
  you "what we will do if the world try to attack our country after this and how are we even going to tell the whole world about it"
  vet " we just need someone to spread this information to the world in at least 5 minutes before the government could take the action "
  hide hacker thinking
  
  friend "heyyyyyyy [you] what are you guys talking about  "
  you " i think we have someone to spread this information to the world"
  vet "don't worry about the attack for now it's not something that could happen right away we can manage that  "
  vet "our new veteran have some good foreign relationship  "
  roxy "i can also talk to some international committe about it "
  you " but still the new veteran is kind of "
  vet " it also could go wrong but do you want to take the risk"
  vet "do you want take the help  "
  menu veteranhelp:
    
    "take saleryman help":
      "as the veteran said we talk to the saleryman or the new veteran and told him about everything "
      " and he agreed to help us "
      "[friend] agreed for our request"
      " before the show the new veteran give a sheet of paper to [friend]" 
      " we revealed everything to the world through that performance , all the evidence to the big screens  "
      friend " everyone throughout the world i know you all get scared but i don't want a war to happen i want peace "
      friend "towards my fans towards my loyal fans who lives in this world and i want to stop this killing of each other  "
      friend " let's create a world where in future we don't need to fight with weopen "
      friend " let's create an assembly.... "
      friend " a world assembly where everyone thoughts will be listened "
      friend " where all races  , genders  , and countries citzen  can talk to each other "
      friend " WIN FOR PEACE!!!!"
      " after some time the government realized it and the show was canceled right away "
      "[friend] was captured "
      "after an hour world politician comes to give their ideas respect to this  "
      " after 2 hours citizen assembly got cancelled "
      " [friend] after 5 hours get bail because of the citizens and fans of him "
      " the world was safed but hacker and veteran was captured "
      " after 8 hours they captured me "
      " after 9 hours roxy leaves the country "

      " by the words of [friend] the countries that were against us take their hands to help us "
      " citizens throughout the whole world started doing campaigns and charity "
      " some countries tries to launch their own assembly "

      " after 10 hours the court gave us the punishment for 1 year "
      "ending 4 "
      " the world got saved "
      " no one executed"
      return

    "don't take saleryman help":
      "we denied to take the saleryman help or the new veteran "
      "[friend] agreed for our request"
      " the next day"
      "the show started the song was great the performance was great  "
      " we revealed everything to the world through that performance ,  all the evidence to the big screens  "
      " after some time the government realized it and  the show was canceled right away "
      "[friend] was captured "
      " after an hour world politician comes to give their ideas respect to this  "
      " after 2 hours citizen assembly got cancelled "
      " [friend] after 5 hours get bail because of the citizens and fans of him "
      " the world was safed but hacker and veteran was captured "
      " after 8 hours they captured me "
      " after 9 hours roxy leaves the country "
      " after 11 hours hacker and veteran got executed "
      " after 12 hours court declared 5 years jail for me"
      " The war got saved "
      " but with cost"
      "ENDING 4"
      return
     

  










             

    



    
    



    





      
       


   
    




 

   
  


  
 




