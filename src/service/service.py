# Define classes for QuestionOption, Question, and Scenario

class ChapterIntro:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"Intro: {self.text}"


class QuestionOption:
    def __init__(self, id, text, correct_option=False):
        self.id = id
        self.text = text
        self.correct_option = correct_option

    def __repr__(self):
        return f"{self.text} (Correct: {self.correct_option})"


class Question:
    def __init__(self, id, text, options):
        self.id = id
        self.text = text
        self.options = options

    def __repr__(self):
        return f"Question: {self.text}"


class Scenario:
    def __init__(self, id, title, description, chapter_intro, questions):
        self.id = id
        self.title = title
        self.description = description
        self.chapter_intro = chapter_intro
        self.questions = questions

    def __repr__(self):
        return f"Scenario '{self.title}'"


class Character:
    def __init__(self, id, name, scenario, title):
        self.id = id
        self.name = name
        self.scenario = scenario
        self.title = title

    def __repr__(self):
        return f"Character: id = {self.id}, name = {self.name}, title = {self.title}"

game_objective = """
    As The Oceanic Dream set sail on its 20-day journey across the open sea, excitement buzzed among the passengers. 
    The ship, a floating paradise of luxury, promised adventure, relaxation, and escape. 
    Doctor Arstan, a seasoned physician, was eager to leave behind the pressures of his practice, while Ata Kuba, 
    the ship’s talented singer, looked forward to dazzling the guests with his performances. Mr. Kadyrbek, 
    a retired teacher, and Kymbatai, a taxi driver seeking a break from the city’s hustle, were just a few of the 
    diverse group on board, each ready for a much-needed getaway.

    The first days were filled with laughter, new friendships, and the excitement of exploration. The passengers 
    settled into a routine of sunbathing, fine dining, and evening entertainment, enjoying the peace and beauty of 
    the endless horizon. But beneath the surface of this idyllic voyage, something dark was looming. The calm before 
    the storm had begun, and soon, what promised to be the trip of a lifetime would turn into something far more sinister.
    """

    # Define and print Kymbatai's scenarios
    # Scenario 1: An Evening in the Sauna
chapter1_intro = ChapterIntro(
        """
        Kymbatai, the taxi driver, was lounging on the deck, enjoying a rare moment of peace, 
        when a ship's officer approached her, casting a shadow over her reclined chair.

        "Ms. Kymbatai," the officer said with a tense expression, "I’m sorry to disturb your relaxation, 
        but I have some important news. An elderly passenger, Mrs. Agnes Walker, was found dead in her cabin earlier today. 
        It’s being treated as suspicious."

        Kymbatai sat up, her brow furrowed. "Dead? That’s terrible. What happened?"

        "We don’t have all the details yet," the officer explained, "but you’ll need to be available for questioning 
        as part of the investigation. The detective will be speaking with everyone onboard."

        Kymbatai nodded, feeling the weight of the situation sink in. What was supposed to be a carefree vacation was 
        quickly turning into something far more unsettling.
        """
    )

options_kymbatai_q1_s1 = [
        QuestionOption(2, "I was at the lounge bar, having a drink and chatting with other passengers.", False),
        QuestionOption(3, "I was taking a walk around the ship’s deck, enjoying the sea breeze.", False),
        QuestionOption(1, "I was in the ship’s sauna, relaxing in the steam and letting the warm air soothe me.", True)
    ]

options_kymbatai_q2_s1 = [
        QuestionOption(4, "I was quietly relaxing and enjoying a smoothie; a few passengers were around, but I didn’t speak with anyone in particular.", True),
        QuestionOption(5, "I met with some friends in the lounge and spent time chatting with them.", False),
        QuestionOption(6, "I went back to my cabin right after my swim and didn’t go to the lounge.", False)
    ]

options_kymbatai_q3_s1 = [
        QuestionOption(8, "I returned around midnight after spending more time at the lounge.", False),
        QuestionOption(7, "I returned to my cabin around 8:30 p.m., relaxed, and went to bed early, around 10 p.m.", True),
        QuestionOption(9, "I stayed out until about 9:30 p.m. and then went to meet some friends in the crew area.", False)
    ]

questions_kymbatai_s1 = [
        Question(1, "Where were you from 5 p.m. to 6 p.m., and what were you doing?", options_kymbatai_q1_s1),
        Question(2, "Did you interact with anyone from 7 p.m. to 8 p.m. in the spa lounge?", options_kymbatai_q2_s1),
        Question(3, "When did you return to your cabin, and what did you do afterward?", options_kymbatai_q3_s1)
    ]

description_scenario1_kymbatai = """
    At 5 p.m., Kymbatai decided to relax in the ship’s sauna. The warm, steamy air surrounded her, 
    and she enjoyed the soft sounds of water for about an hour, letting the heat melt away her worries. 
    Afterward, she took a quick swim in the pool to cool off. The refreshing water felt great as she swam a few laps, 
    enjoying the quiet of the almost empty area. Once she dried off, she headed to the spa’s lounge.
    From 7 p.m. to 8 p.m., Kymbatai relaxed in a comfy chair, sipping a fruity smoothie with a slice of pineapple 
    on the side while listening to soft music. The calm atmosphere helped her recharge as she watched other 
    passengers come and go. Feeling refreshed, she returned to her cabin by 8:30 p.m. The cozy space welcomed her 
    as she thought about her day, feeling thankful for the simple pleasures of the cruise before drifting off to sleep.
    """
    
scenario1_kymbatai = Scenario(1, "An Evening in the Sauna", description_scenario1_kymbatai, chapter1_intro, questions_kymbatai_s1)
# Scenario 2: Sunset at Sea
chapter1_intro = ChapterIntro(
    """
    Kymbatai, the taxi driver, was lounging on the deck, enjoying a rare moment of peace, 
    when a ship's officer approached her, casting a shadow over her reclined chair.

    "Ms. Kymbatai," the officer said with a tense expression, "I’m sorry to disturb your relaxation, 
    but I have some important news. An elderly passenger, Mrs. Agnes Walker, was found dead in her cabin earlier today. 
    It’s being treated as suspicious."

    Kymbatai sat up, her brow furrowed. "Dead? That’s terrible. What happened?"

    "We don’t have all the details yet," the officer explained, "but you’ll need to be available for questioning 
    as part of the investigation. The detective will be speaking with everyone onboard."

    Kymbatai nodded, feeling the weight of the situation sink in. What was supposed to be a carefree vacation was 
    quickly turning into something far more unsettling.
    """
)

options_kymbatai_q1_s2 = [
    QuestionOption(10, "I was taking in the sunset view, sipping orange juice, and taking some photos and selfies.", True),
    QuestionOption(11, "I was watching the sunset but mostly chatting with other passengers around me.", False),
    QuestionOption(12, "I was on the deck, but I spent more time walking around than watching the sunset.", False)
]

options_kymbatai_q2_s2 = [
    QuestionOption(14, "Yes, I ran into a few people and stayed to chat for a while.", False),         
    QuestionOption(13, "No, I didn’t see anyone as I returned to my cabin around 7 p.m.", True),
    QuestionOption(15, "Yes, I saw a fellow passenger, and we decided to go to the lounge for a drink.", False)
]

options_kymbatai_q3_s2 = [
    QuestionOption(17, "We only talked for a few minutes, and then I went back out to walk on the deck around 9 p.m.", False),
    QuestionOption(18, "I didn’t call anyone; I went straight to bed at 8:30 p.m.", False),
    QuestionOption(16, "I talked with my friend from 8 p.m. until 9:30 p.m., sharing photos and chatting before going to bed.", True)
]

questions_kymbatai_s2 = [
    Question(4, "From 5 p.m. to 7 p.m., what were you doing on the upper deck?", options_kymbatai_q1_s2),
    Question(5, "After watching the sunset, did you encounter anyone on your way back to the cabin?", options_kymbatai_q2_s2),
    Question(6, "How long did you talk with your friend after you returned to your cabin?", options_kymbatai_q3_s2)
]

description_scenario2_kymbatai = """
At 5 p.m., Kymbatai headed to the upper deck with a glass of freshly squeezed orange juice, eager to catch the sunset. 
She found a quiet spot by the railing, where the sky was transitioning into brilliant hues of orange and pink. The cool sea 
breeze and the sound of the waves added to the serenity of the moment. While enjoying the view, Kymbatai took out her phone 
to snap a few pictures of the stunning sunset, as well as a couple of selfies with the ocean in the background. 
She exchanged brief smiles with a few nearby passengers but mostly kept to herself. For the next two hours, she stayed on deck, 
soaking in the peaceful atmosphere as the sun finally disappeared below the horizon.

At 7 p.m., after taking the last photo of the starry sky, Kymbatai finished her drink and returned to her cabin. 
Around 8 p.m., she decided to chat with her friend, also sharing photos she had taken earlier. They chatted until 9:30 p.m., 
after which she went to bed.
"""

scenario2_kymbatai = Scenario(2, "Sunset at Sea", description_scenario2_kymbatai, chapter1_intro, questions_kymbatai_s2)


# Scenario 3: A Refreshing Yoga Class
chapter1_intro = ChapterIntro(
    """
    Kymbatai, the taxi driver, was lounging on the deck, enjoying a rare moment of peace, 
    when a ship's officer approached her, casting a shadow over her reclined chair.

    "Ms. Kymbatai," the officer said with a tense expression, "I’m sorry to disturb your relaxation, 
    but I have some important news. An elderly passenger, Mrs. Agnes Walker, was found dead in her cabin earlier today. 
    It’s being treated as suspicious."

    Kymbatai sat up, her brow furrowed. "Dead? That’s terrible. What happened?"

    "We don’t have all the details yet," the officer explained, "but you’ll need to be available for questioning 
    as part of the investigation. The detective will be speaking with everyone onboard."

    Kymbatai nodded, feeling the weight of the situation sink in. What was supposed to be a carefree vacation was 
    quickly turning into something far more unsettling.
    """
)

options_kymbatai_q1_s3 = [
    QuestionOption(20, "I was in the lounge, having a drink with some passengers.", False),
    QuestionOption(21, "I was in my cabin, relaxing and reading.", False),
    QuestionOption(19, "I attended a yoga class on the ship.", True)
]

options_kymbatai_q2_s3 = [
    QuestionOption(24, "I went to the pool area to relax after the class.", False),
    QuestionOption(23, "I went to the deck to watch the sunset.", False),
    QuestionOption(22, "I went back to my cabin around 6 p.m., changed clothes, and had a light dinner.", True)
]

options_kymbatai_q3_s3 = [
    QuestionOption(25, "I stayed in my cabin from 7 p.m. onward, reading a book until I went to sleep.", True),
    QuestionOption(26, "I left my cabin around 10 p.m. to meet some friends at the bar.", False),
    QuestionOption(27, "I went out for a walk on the deck around midnight.", False)
]

questions_kymbatai_s3 = [
    Question(7, "What did you do between 5 p.m. and 6 p.m.?", options_kymbatai_q1_s3),
    Question(8, "Where did you go immediately after yoga, and what did you do?", options_kymbatai_q2_s3),
    Question(9, "What time did you settle down for the night, and did anyone visit or see you afterward?", options_kymbatai_q3_s3)
]

description_scenario3_kymbatai = """
At 5 p.m., Kymbatai decided to join a yoga class on the ship to unwind and rejuvenate. The studio had soft lighting and calming scents, 
creating a peaceful environment. As the class began, she rolled out her mat in the front row and followed the instructor through 
a series of poses, focusing on deep breathing. After the hour-long session, she felt energized and refreshed, chatting with 
fellow participants about their experiences and sharing tips. By 7 p.m., Kymbatai returned to her cabin, still buzzing from the 
positive energy of the class. She changed into comfortable clothes and enjoyed a light dinner, then settled down with a good book, 
reflecting on the peaceful experience of the evening. Feeling content, she spent the rest of the night unwinding in her room.
"""

scenario3_kymbatai = Scenario(3, "A Refreshing Yoga Class", description_scenario3_kymbatai, chapter1_intro, questions_kymbatai_s3)

scenario_list_kymbatai = [scenario1_kymbatai, scenario2_kymbatai]

# Scenario 1: A Quiet Evening of Preparation
chapter2_intro = ChapterIntro(
    """
    Dr. Arstan was in the ship’s medical clinic, reviewing patient records, when the door swung open, revealing the ship’s captain, 
    his face unusually grim.

    "Doctor Arstan," the captain said, closing the door behind him, "I need to inform you of a situation. 
    One of our passengers, Mrs. Agnes Walker, an elderly woman, was found dead early this morning in her cabin. 
    It appears suspicious."

    Dr. Arstan set his papers aside, his mind immediately racing. "Dead? I hadn’t seen her recently—was she ill?"

    "We’re not sure of the cause yet," the captain continued, "but the detective onboard will be conducting interviews. 
    We’ll need you to be ready for questioning."

    Dr. Arstan nodded slowly, a knot forming in his stomach. He had been on this ship to relax, but now, things had taken a dark turn.
    """
)

options_arstan_q1_s1 = [
    QuestionOption(10, "I was in the clinic organizing supplies and reviewing patient records.", True),
    QuestionOption(11, "I was in the dining hall having dinner with a group of passengers.", False),
    QuestionOption(12, "I was in my cabin resting, trying to avoid the crowds.", False)
]

options_arstan_q2_s1 = [
    QuestionOption(14, "Yes, I had a long conversation with Mrs. Walker about her health.", False),
    QuestionOption(13, "No, I mostly stayed in the clinic and didn’t see many people, just a few crew members passing by.", True),
    QuestionOption(15, "Yes, I was consulting with another doctor about a passenger's condition.", False)
]

options_arstan_q3_s1 = [
    QuestionOption(17, "I went out to the deck for fresh air and ended up chatting with other crew members.", False),
    QuestionOption(18, "I only stayed for an hour after the emergency before heading to bed.", False),
    QuestionOption(16, "I stayed in the clinic, finishing my notes, and I didn’t leave until I locked up around 2 a.m.", True)
]

questions_arstan_s1 = [
    Question(4, "Where were you from 5 p.m. to 7 p.m.?", options_arstan_q1_s1),
    Question(5, "Did you meet anyone during your work?", options_arstan_q2_s1),
    Question(6, "What did you do after 10 p.m.?", options_arstan_q3_s1)
]

description_scenario1_arstan = """
From 5 p.m. to 2 a.m., Dr. Arstan spent the evening in the medical clinic preparing for a seminar he was supposed to give later in the cruise.

5 p.m. to 7 p.m.: He organized medical supplies, ensuring everything was stocked and ready for emergencies. He checked the temperature 
of medications, wrote down any items that needed replenishing, and familiarized himself with passenger records.

7 p.m. to 10 p.m.: He worked on his presentation, typing notes on his laptop, occasionally stepping out to grab a cup of tea from 
the nearby café. During his breaks, he glanced out at the ocean, enjoying the view and the peacefulness of the ship.

10 p.m. to 2 a.m.: He continued refining his notes, practicing his speech aloud in the empty clinic, and jotting down last-minute thoughts. 
He felt a sense of accomplishment, unaware of the dark events unfolding around him.
"""

scenario1_arstan = Scenario(1, "A Quiet Evening of Preparation", description_scenario1_arstan, chapter2_intro, questions_arstan_s1)

# Scenario 2: An Unexpected Emergency
chapter2_intro = ChapterIntro(
    """
    Dr. Arstan was in the ship’s medical clinic, reviewing patient records, when the door swung open, revealing the ship’s captain, 
    his face unusually grim.

    "Doctor Arstan," the captain said, closing the door behind him, "I need to inform you of a situation. 
    One of our passengers, Mrs. Agnes Walker, an elderly woman, was found dead early this morning in her cabin. 
    It appears suspicious."

    Dr. Arstan set his papers aside, his mind immediately racing. "Dead? I hadn’t seen her recently—was she ill?"

    "We’re not sure of the cause yet," the captain continued, "but the detective onboard will be conducting interviews. 
    We’ll need you to be ready for questioning."

    Dr. Arstan nodded slowly, a knot forming in his stomach. He had been on this ship to relax, but now, things had taken a dark turn.
    """
)

options_arstan_q1_s2 = [
    QuestionOption(19, "I was in the clinic preparing for my seminar when I was called to attend to a passenger.", True),
    QuestionOption(20, "I was outside enjoying the sunset.", False),
    QuestionOption(21, "I was having a meeting with the ship's crew about health protocols.", False)
]

options_arstan_q2_s2 = [
    QuestionOption(23, "Yes, she was wandering around, looking for her cabin.", False),
    QuestionOption(22, "No, I didn’t see her at all during my shift.", True),
    QuestionOption(24, "Yes, she came in for some medicine earlier in the evening.", False)
]

options_arstan_q3_s2 = [
    QuestionOption(25, "I stayed until around 2 a.m., ensuring the passenger was stable and attending to others who needed help.", True),
    QuestionOption(26, "I left the clinic around midnight to socialize with other passengers.", False),
    QuestionOption(27, "I only stayed for an hour after the emergency before heading to bed.", False)
]

questions_arstan_s2 = [
    Question(7, "What were you doing when the emergency occurred?", options_arstan_q1_s2),
    Question(8, "Did you see Mrs. Walker that night?", options_arstan_q2_s2),
    Question(9, "How long did you stay in the clinic after the emergency?", options_arstan_q3_s2)
]

description_scenario2_arstan = """
From 5 p.m. to 2 a.m., Dr. Arstan received an emergency call about a passenger who had collapsed on the deck.

5 p.m. to 6 p.m.: He was in the clinic preparing for the next day when he was informed about the emergency over the ship’s intercom. 
He quickly gathered his medical kit, adrenaline pumping as he raced to the scene.

6 p.m. to 9 p.m.: After attending to the collapsed passenger, he performed basic checks, stabilized them, and provided first aid. 
He took the passenger’s vitals and talked to them to keep them conscious, all while calming the gathered crowd.

9 p.m. to 2 a.m.: He remained in the clinic, checking on the patient’s progress, attending to other minor medical issues that arose, 
and documenting the incident in the medical log. He occasionally stepped out to reassure the concerned family of the passenger.
"""

scenario2_arstan = Scenario(2, "An Unexpected Emergency", description_scenario2_arstan, chapter2_intro, questions_arstan_s2)

# Scenario 3: Socializing with Passengers
chapter2_intro = ChapterIntro(
    """
    Dr. Arstan was in the ship’s medical clinic, reviewing patient records, when the door swung open, revealing the ship’s captain, 
    his face unusually grim.

    "Doctor Arstan," the captain said, closing the door behind him, "I need to inform you of a situation. 
    One of our passengers, Mrs. Agnes Walker, an elderly woman, was found dead early this morning in her cabin. 
    It appears suspicious."

    Dr. Arstan set his papers aside, his mind immediately racing. "Dead? I hadn’t seen her recently—was she ill?"

    "We’re not sure of the cause yet," the captain continued, "but the detective onboard will be conducting interviews. 
    We’ll need you to be ready for questioning."

    Dr. Arstan nodded slowly, a knot forming in his stomach. He had been on this ship to relax, but now, things had taken a dark turn.
    """
)

options_arstan_q1_s3 = [
    QuestionOption(29, "I was in the clinic preparing for the next day's schedule.", False),
    QuestionOption(30, "I was in my cabin, reading a book.", False),
    QuestionOption(28, "I was having dinner with passengers in the dining hall.", True)
]

options_arstan_q2_s3 = [
    QuestionOption(31, "No, I didn’t see her at dinner.", True),
    QuestionOption(32, "Yes, she was at the table next to us, talking to other guests.", False),
    QuestionOption(33, "I think I saw her leave the dining hall early.", False)
]

options_arstan_q3_s3 = [
    QuestionOption(35, "I stayed in the lounge to enjoy more of the evening entertainment.", False),
    QuestionOption(34, "I returned to my cabin to relax and jot down some thoughts.", True),
    QuestionOption(36, "I went out on deck for some fresh air and saw a few crew members.", False)
]

questions_arstan_s3 = [
    Question(10, "Where were you from 5 p.m. to 8 p.m.?", options_arstan_q1_s3),
    Question(11, "Did you see Mrs. Walker during dinner?", options_arstan_q2_s3),
    Question(12, "What did you do after 10 p.m.?", options_arstan_q3_s3)
]

description_scenario3_arstan = """
From 5 p.m. to 2 a.m., Dr. Arstan chose to unwind by socializing with other passengers instead of working.

5 p.m. to 8 p.m.: He enjoyed dinner with a group of guests, laughing and sharing stories. 
He participated in discussions about health and wellness, entertaining guests with his medical knowledge.

8 p.m. to 10 p.m.: He joined in on trivia night in the lounge, answering questions and engaging with other passengers. 
He felt a sense of camaraderie as they cheered and groaned over trivia answers.

10 p.m. to 2 a.m.: After trivia, he returned to his cabin, where he reflected on the evening and wrote notes about 
his experiences and interactions with passengers. He made a mental note to follow up on some discussions during his next shift.
"""

scenario3_arstan = Scenario(3, "Socializing with Passengers", description_scenario3_arstan, chapter2_intro, questions_arstan_s3)

# Print Dr. Arstan's scenarios

scenario_list_arstan = [scenario1_arstan, scenario2_arstan, scenario3_arstan]

# Scenario 1: A Quiet Night Alone
chapter3_intro = ChapterIntro(
    """
    Ata Kuba was sitting in his cabin, quietly strumming his guitar when there was a sudden knock on the door. 
    Startled, he set his guitar aside and opened the door to see one of the ship’s security officers, looking unusually serious.

    "Mr. Ata," the officer said, his voice low, "I’m afraid there’s been an incident. An elderly passenger, a woman, was found dead earlier this morning. 
    We’re conducting an investigation, and the detective on board will need to speak with you."

    Ata blinked, his heart skipping a beat. "Dead? Who?"

    "A woman named Mrs. Agnes Walker, 73 years old. We need to ask all staff and passengers a few questions. 
    Please be prepared for an interrogation later today."

    Ata felt a chill run through him, the peacefulness of the voyage suddenly shattered.
    """
)

options_kuba_q1_s1 = [
    QuestionOption(2, "I was in the lounge having a drink with a friend from the band before we started rehearsing together.", False),
    QuestionOption(3, "I was attending a crew meeting about upcoming events and entertainment schedules.", False),
    QuestionOption(1, "I was in my cabin, doing my usual vocal warm-ups and rehearsing a few songs I’ve been working on.", True)
]

options_kuba_q2_s1 = [
    QuestionOption(4, "No, instead of performing in the lounge, I decided to head to the rehearsal room to practice privately. I wanted to focus on some new music.", True),
    QuestionOption(5, "Yes, I did an impromptu performance in the lounge because the crowd wanted to hear more.", False),
    QuestionOption(6, "Yes, I gave a special performance for a private party that was held in the VIP section of the ship.", False)
]

options_kuba_q3_s1 = [
    QuestionOption(7, "I was there from about 7 p.m. to 10 p.m. It was completely quiet, and I didn’t see anyone the whole time.", True),
    QuestionOption(8, "I stayed there until midnight, practicing my new songs.", False),
    QuestionOption(9, "I left after an hour because the room was booked for another event, and I didn’t have time to finish practicing.", False)
]

options_kuba_q4_s1 = [
    QuestionOption(11, "I went back to my cabin around midnight and stayed up until 3 a.m. working on more music.", False),
    QuestionOption(10, "I went back to my cabin around 10:30 p.m., made myself a snack, and spent the rest of the night relaxing and listening to music. I went to bed at 1 a.m.", True),
    QuestionOption(12, "I returned to my cabin at 11 p.m., but then I went out again to meet some friends at the crew bar before finally heading to bed around 2 a.m.", False)
]

questions_kuba_s1 = [
    Question(1, "Where were you from 5 p.m. to 7 p.m.?", options_kuba_q1_s1),
    Question(2, "Did you perform for any passengers that night?", options_kuba_q2_s1),
    Question(3, "How long were you in the rehearsal room?", options_kuba_q3_s1),
    Question(4, "When did you return to your cabin, and what did you do after that?", options_kuba_q4_s1)
]

description_scenario1_kuba = """
From 5 p.m. to 2 a.m., Ata Kuba, the ship's singer, spent a quiet evening alone. At 5 p.m., he decided to skip his usual warm-up routine, 
feeling confident in his performance abilities after several days of shows. Instead, he relaxed in his cabin, reading a novel he had been trying to finish. 
Around 7 p.m., Ata made himself a cup of tea and continued reading until he became sleepy. By 9 p.m., he was still in his cabin, 
this time writing new lyrics for a song he had been working on for his next album. He spent the next few hours writing and occasionally 
looking out the window, enjoying the calm of the ocean. At midnight, he decided to call it a night and drifted off to sleep, without ever leaving his cabin.
"""

scenario1_kuba = Scenario(1, "A Quiet Night Alone", description_scenario1_kuba, chapter3_intro, questions_kuba_s1)

# Scenario 2: A Late-Night Walk
chapter3_intro = ChapterIntro(
    """
    Ata Kuba was sitting in his cabin, quietly strumming his guitar when there was a sudden knock on the door. 
    Startled, he set his guitar aside and opened the door to see one of the ship’s security officers, looking unusually serious.

    "Mr. Ata," the officer said, his voice low, "I’m afraid there’s been an incident. An elderly passenger, a woman, 
    was found dead earlier this morning. We’re conducting an investigation, and the detective on board will need to speak with you."

    Ata blinked, his heart skipping a beat. "Dead? Who?"

    "A woman named Mrs. Agnes Walker, 73 years old. We need to ask all staff and passengers a few questions. 
    Please be prepared for an interrogation later today."

    Ata felt a chill run through him, the peacefulness of the voyage suddenly shattered.
    """
)

options_kuba_q1_s2 = [
    QuestionOption(14, "9 p.m.", False),
    QuestionOption(13, "7 p.m.", True),
    QuestionOption(15, "11 p.m.", False)
]

options_kuba_q2_s2 = [
    QuestionOption(16, "In the ship's lounge, performing your set", True),
    QuestionOption(17, "In your cabin, working on your song and playing the guitar", False),
    QuestionOption(18, "In the dining area, having dinner with the crew", False)
]

options_kuba_q3_s2 = [
    QuestionOption(20, "Yes, I saw a fellow passenger", False),
    QuestionOption(21, "No, I didn’t see anyone during my walk", False),
    QuestionOption(19, "Yes, I ran into a crew member", True)
]

options_kuba_q4_s2 = [
    QuestionOption(23, "Still wandering on the deck", False),
    QuestionOption(22, "Back in your cabin, trying to rest", True),
    QuestionOption(24, "In the ship’s lounge, having a drink", False)
]

questions_kuba_s2 = [
    Question(5, "Ata, you mentioned a late-night walk. At what time did you leave your cabin?", options_kuba_q1_s2),
    Question(6, "Where were you between 5 p.m. and 9 p.m. that night?", options_kuba_q2_s2),
    Question(7, "Did you encounter anyone during your walk around the ship’s deck?", options_kuba_q3_s2),
    Question(8, "What was your location at midnight?", options_kuba_q4_s2)
]

description_scenario2_kuba = """
Ata Kuba had a restless evening on the night of the incident. At 5 p.m., he started his vocal warm-up in his cabin as usual 
but soon felt unsettled, distracted by the thought of a new song he had been working on. After his warm-up, he decided not 
to perform his usual set in the lounge. Instead, he stayed in his cabin, playing his guitar and working on the song. 
Around 9 p.m., feeling the need to clear his head, he left his cabin for a late-night walk around the ship’s deck. 
He spent the next few hours wandering the quieter parts of the ship, lost in thought and enjoying the cool evening air. 
By midnight, he returned to his cabin and lay down to rest. He was in and out of sleep, unsure of when exactly he drifted off, 
but he never crossed paths with anyone during his walk.
"""

scenario2_kuba = Scenario(2, "A Late-Night Walk", description_scenario2_kuba, chapter3_intro, questions_kuba_s2)

# Scenario 3: A Private Practice Session
chapter3_intro = ChapterIntro(
    """
    Ata Kuba was sitting in his cabin, quietly strumming his guitar when there was a sudden knock on the door. 
    Startled, he set his guitar aside and opened the door to see one of the ship’s security officers, looking unusually serious.

    "Mr. Ata," the officer said, his voice low, "I’m afraid there’s been an incident. An elderly passenger, a woman, 
    was found dead earlier this morning. We’re conducting an investigation, and the detective on board will need to speak with you."

    Ata blinked, his heart skipping a beat. "Dead? Who?"

    "A woman named Mrs. Agnes Walker, 73 years old. We need to ask all staff and passengers a few questions. 
    Please be prepared for an interrogation later today."

    Ata felt a chill run through him, the peacefulness of the voyage suddenly shattered.
    """
)

options_kuba_q1_s3 = [
    QuestionOption(26, "Meeting with other performers in the lounge", False),
    QuestionOption(27, "Having dinner with passengers in the dining area", False),
    QuestionOption(25, "Rehearsing new songs softly in your cabin", True)
]

options_kuba_q2_s3 = [
    QuestionOption(28, "In your cabin, resting", True),
    QuestionOption(29, "Walking around the ship’s deck", False),
    QuestionOption(30, "In the ship's small rehearsal room, playing the piano", False)
]

options_kuba_q3_s3 = [
    QuestionOption(32, "Yes, I spoke briefly to another performer", False),
    QuestionOption(31, "Yes, a crew member came by to check on me", True),
    QuestionOption(33, "No, I was alone the entire time in the rehearsal room", False)
]

options_kuba_q4_s3 = [
    QuestionOption(35, "Made a late-night snack and listened to music", False),
    QuestionOption(36, "Called a friend to chat", False),
    QuestionOption(34, "Went straight to bed", True)
]

questions_kuba_s3 = [
    Question(9, "Ata, can you confirm your activity between 5 p.m. and 6 p.m.?", options_kuba_q1_s3),
    Question(10, "Where were you between 7 p.m. and 10 p.m.?", options_kuba_q2_s3),
    Question(11, "Did anyone see you between 7 p.m. and 10 p.m. while you were practicing?", options_kuba_q3_s3),
    Question(12, "What did you do after returning to your cabin at 10:30 p.m.?", options_kuba_q4_s3)
]

description_scenario3_kuba = """
Yesterday evening, Ata Kuba had an impromptu private practice session. From 5 p.m. to 6 p.m., he was in his cabin rehearsing 
a new set of songs he wanted to debut soon, singing softly to avoid disturbing his neighbors. Feeling inspired, he decided 
to head to the ship’s small, rarely used rehearsal room to continue practicing. From 7 p.m. to 10 p.m., Ata was in the room 
playing the piano and experimenting with new arrangements, completely losing track of time. It was a secluded spot, so he 
saw no one the entire time. By 10:30 p.m., feeling exhausted but creatively fulfilled, he returned to his cabin, made himself 
a late-night snack, and spent the rest of the night listening to music. He finally went to bed around 1 a.m., but no one saw 
him the entire evening, as he remained in isolated parts of the ship.
"""

scenario3_kuba = Scenario(3, "A Private Practice Session", description_scenario3_kuba, chapter3_intro, questions_kuba_s3)

scenario_list_kuba = [scenario1_kuba, scenario2_kuba, scenario3_kuba]

# Scenario 1: A Night of Reading and Reflection
chapter4_intro = ChapterIntro(
    """
    Mr. Kadyrbek was enjoying a quiet moment in the library, flipping through a novel, when a crewmember approached him, 
    their voice hushed but urgent.

    "Mr. Kadyrbek," the crewmember began, "I’m afraid I have some distressing news. One of our passengers, 
    a 73-year-old woman named Mrs. Agnes Walker, was found dead in her cabin this morning under suspicious circumstances."

    Mr. Kadyrbek gasped, his hand covering his mouth. "Oh my… what do you mean suspicious?"

    "The ship’s detective is investigating, and we’re asking all passengers to be ready for questioning," the crewmember continued. 
    "You’ll be asked to meet with him later today."

    Mr. Kadyrbek closed his book, his thoughts racing. The serenity of the cruise had been shattered, 
    and now, he found himself a potential witness in what appeared to be a sinister situation.
    """
)

options_kadyrbek_q1_s1 = [
    QuestionOption(1, "I was in the ship’s library, reading a history book.", True),
    QuestionOption(2, "I was in the lounge, having a drink and socializing with other passengers.", False),
    QuestionOption(3, "I was having dinner in the main dining hall with some new friends I met earlier in the day.", False),
    QuestionOption(4, "I attended a trivia game night organized for the passengers in the entertainment area.", False)
]

options_kadyrbek_q2_s1 = [
    QuestionOption(6, "I went to my cabin to take a nap and slept until midnight.", False),
    QuestionOption(7, "I joined a dance class that was being held in the ship's ballroom.", False),
    QuestionOption(5, "I took a short walk around the deck to stretch my legs and enjoy the night air.", True),
    QuestionOption(8, "I had a private meeting with the captain about ship activities for the next few days.", False)
]

options_kadyrbek_q3_s1 = [
    QuestionOption(10, "Yes, I had a lengthy conversation with another passenger in the library.", False),
    QuestionOption(9, "No, I mostly kept to myself and didn’t engage with anyone the entire evening.", True),
    QuestionOption(11, "Yes, I met a crew member and we talked for a while near the café.", False),
    QuestionOption(12, "Yes, I spoke with a few passengers during my walk around the deck.", False)
]

options_kadyrbek_q4_s1 = [
    QuestionOption(13, "I went to bed around 1:30 a.m., after listening to some classical music.", True),
    QuestionOption(14, "I fell asleep at 10 p.m., right after returning to my cabin.", False),
    QuestionOption(15, "I stayed up until 3 a.m., writing some thoughts for a new blog post.", False),
    QuestionOption(16, "I went to sleep immediately after returning to my cabin at 9 p.m.", False)
]

questions_kadyrbek_s1 = [
    Question(1, "Where were you between 5 p.m. and 8 p.m.?", options_kadyrbek_q1_s1),
    Question(2, "What did you do after 8 p.m.?", options_kadyrbek_q2_s1),
    Question(3, "Did you interact with anyone during the evening?", options_kadyrbek_q3_s1),
    Question(4, "What time did you go to sleep?", options_kadyrbek_q4_s1)
]

description_scenario1_kadyrbek = """
From 5 p.m. to 2 a.m., Mr. Kadyrbek, the retired teacher, spent his evening quietly in the ship’s library. 
At 5 p.m., he made himself comfortable with a history book he had been meaning to read. Engrossed in the pages, 
he remained seated at the same table until 8 p.m., taking a brief break only to get a cup of tea from the nearby café. 
Afterward, he returned to his spot and read until 10 p.m., when the library started to empty out. Feeling restless, 
he decided to take a walk around the deck, watching the stars and reflecting on his years in the classroom. 
Around midnight, he returned to his cabin and listened to classical music until he dozed off at around 1:30 a.m. 
He didn’t speak to anyone during this time and remained largely unnoticed.
"""

scenario1_kadyrbek = Scenario(1, "A Night of Reading and Reflection", description_scenario1_kadyrbek, chapter4_intro, questions_kadyrbek_s1)

# Scenario 2: Socializing in the Lounge
chapter4_intro = ChapterIntro(
    """
    Mr. Kadyrbek was enjoying a quiet moment in the library, flipping through a novel, when a crewmember approached him, 
    their voice hushed but urgent.

    "Mr. Kadyrbek," the crewmember began, "I’m afraid I have some distressing news. One of our passengers, 
    a 73-year-old woman named Mrs. Agnes Walker, was found dead in her cabin this morning under suspicious circumstances."

    Mr. Kadyrbek gasped, his hand covering his mouth. "Oh my… what do you mean suspicious?"

    "The ship’s detective is investigating, and we’re asking all passengers to be ready for questioning," the crewmember continued. 
    "You’ll be asked to meet with him later today."

    Mr. Kadyrbek closed his book, his thoughts racing. The serenity of the cruise had been shattered, 
    and now, he found himself a potential witness in what appeared to be a sinister situation.
    """
)

options_kadyrbek_q1_s2 = [
    QuestionOption(17, "I was in the lounge, chatting with other passengers over drinks.", True),
    QuestionOption(18, "I was playing cards with some crew members in the recreation area.", False),
    QuestionOption(19, "I attended a special guest lecture on the ship’s history in the auditorium.", False),
    QuestionOption(20, "I spent the evening in my cabin, watching a documentary.", False)
]

options_kadyrbek_q2_s2 = [
    QuestionOption(21, "I stayed in the lounge to listen to the live jazz performance until around 11 p.m.", True),
    QuestionOption(22, "I went to the casino to try my luck at the roulette table.", False),
    QuestionOption(23, "I visited the ship’s cinema to watch a late-night movie.", False),
    QuestionOption(24, "I returned to my cabin and went straight to bed after dinner.", False)
]

options_kadyrbek_q3_s2 = [
    QuestionOption(25, "I left the lounge around midnight and took a walk on the deck.", True),
    QuestionOption(26, "I left the lounge at 9 p.m. and went back to my cabin to sleep.", False),
    QuestionOption(27, "I left at 10 p.m. to attend a private event in the ballroom.", False),
    QuestionOption(28, "I stayed in the lounge until 1 a.m. and then headed to the crew bar.", False)
]

options_kadyrbek_q4_s2 = [
    QuestionOption(29, "No, I didn’t speak to any crew members. I only interacted with a few passengers.", True),
    QuestionOption(30, "Yes, I spoke with the bartender during my time in the lounge.", False),
    QuestionOption(31, "Yes, I had a conversation with the ship’s entertainment director after the performance.", False),
    QuestionOption(32, "Yes, I chatted with a few of the waitstaff during dinner.", False)
]

questions_kadyrbek_s2 = [
    Question(5, "What did you do between 5 p.m. and 7 p.m.?", options_kadyrbek_q1_s2),
    Question(6, "Where did you go after your conversation in the lounge?", options_kadyrbek_q2_s2),
    Question(7, "What time did you leave the lounge?", options_kadyrbek_q3_s2),
    Question(8, "Did you interact with the crew at all during the evening?", options_kadyrbek_q4_s2)
]

description_scenario2_kadyrbek = """
From 5 p.m. to 2 a.m., Mr. Kadyrbek decided to mingle with other passengers after spending several quiet days alone. 
At 5 p.m., he made his way to the ship’s lounge, where a few people were already gathered for cocktails and casual conversation. 
He spent the next couple of hours engaging in lighthearted discussions with fellow travelers, enjoying the atmosphere. 
Around 8 p.m., after a light dinner, he returned to the lounge for the evening’s entertainment—a live jazz performance by the ship’s singer. 
He remained in the lounge until about 11 p.m., sipping his drink while the music played. At midnight, he took a stroll on the deck, 
then retired to his cabin around 12:30 a.m., spending the last hour reading until he fell asleep.
"""

scenario2_kadyrbek = Scenario(2, "Socializing in the Lounge", description_scenario2_kadyrbek, chapter4_intro, questions_kadyrbek_s2)

# Scenario 3: A Private Writing Session
chapter4_intro = ChapterIntro(
    """
    Mr. Kadyrbek was enjoying a quiet moment in the library, flipping through a novel, when a crewmember approached him, 
    their voice hushed but urgent.

    "Mr. Kadyrbek," the crewmember began, "I’m afraid I have some distressing news. One of our passengers, 
    a 73-year-old woman named Mrs. Agnes Walker, was found dead in her cabin this morning under suspicious circumstances."

    Mr. Kadyrbek gasped, his hand covering his mouth. "Oh my… what do you mean suspicious?"

    "The ship’s detective is investigating, and we’re asking all passengers to be ready for questioning," the crewmember continued. 
    "You’ll be asked to meet with him later today."

    Mr. Kadyrbek closed his book, his thoughts racing. The serenity of the cruise had been shattered, 
    and now, he found himself a potential witness in what appeared to be a sinister situation.
    """
)

options_kadyrbek_q1_s3 = [
    QuestionOption(34, "I was at the pool, relaxing and talking to some other passengers.", False),
    QuestionOption(35, "I attended the evening show in the main lounge.", False),
    QuestionOption(36, "I went to the spa for a massage session.", False),
    QuestionOption(33, "I was in my cabin, writing my memoir and focusing on my work.", True)
]

options_kadyrbek_q2_s3 = [
    QuestionOption(37, "Yes, around 9 p.m., I went to the café to get a coffee, but then I returned to my cabin.", True),
    QuestionOption(38, "No, I stayed in my cabin the entire night without stepping out.", False),
    QuestionOption(39, "Yes, I attended a party on the upper deck around 11 p.m.", False),
    QuestionOption(40, "Yes, I went to the ship’s gym for a late-night workout.", False)
]

options_kadyrbek_q3_s3 = [
    QuestionOption(41, "I wrote from 5 p.m. until around midnight, then took some time to organize my notes.", True),
    QuestionOption(42, "I only wrote for about an hour, then went to bed early.", False),
    QuestionOption(43, "I spent the entire evening socializing and didn’t get any writing done.", False),
    QuestionOption(44, "I wrote until 3 a.m., losing track of time completely.", False)
]

options_kadyrbek_q4_s3 = [
    QuestionOption(45, "I went to bed around 1 a.m. after finishing my notes.", True),
    QuestionOption(46, "I went to bed at 10 p.m. right after returning from the café.", False),
    QuestionOption(47, "I stayed up until 2 a.m., reading after I finished writing.", False),
    QuestionOption(48, "I went to bed shortly after 9 p.m., feeling exhausted.", False)
]

questions_kadyrbek_s3 = [
    Question(9, "What were you doing between 5 p.m. and 9 p.m.?", options_kadyrbek_q1_s3),
    Question(10, "Did you leave your cabin at any point during the night?", options_kadyrbek_q2_s3),
    Question(11, "How long did you spend writing that night?", options_kadyrbek_q3_s3),
    Question(12, "What time did you go to bed?", options_kadyrbek_q4_s3)
]

description_scenario3_kadyrbek = """
From 5 p.m. to 2 a.m., Mr. Kadyrbek dedicated his evening to working on his memoir. At 5 p.m., he set up his writing materials 
on the small desk in his cabin and began typing away on his laptop. For hours, he remained focused, recounting memories of his 
teaching days and the students who had made an impact on him. Around 9 p.m., he took a short break, stepping out to the café 
to grab a coffee, but quickly returned to his cabin to continue writing. By midnight, he had written several pages and felt 
satisfied with his progress. He spent the final hour organizing his notes and reviewing his work before going to bed around 1 a.m. 
No one saw him during this time, as he stayed in his cabin for most of the night.
"""

scenario3_kadyrbek = Scenario(3, "A Private Writing Session", description_scenario3_kadyrbek, chapter4_intro, questions_kadyrbek_s3)

scenario_list_kadyrbek = [scenario1_kadyrbek, scenario2_kadyrbek, scenario3_kadyrbek]


character_list = [Character(1, "kymbatai", scenario_list_kymbatai, "Taxi Driver"), Character(2, "arstan", scenario_list_arstan, "Doctor"), Character(3, "kuba", scenario_list_kuba, "Singer"), Character(4, "kadyrbek", scenario_list_kadyrbek, "Teacher")]

