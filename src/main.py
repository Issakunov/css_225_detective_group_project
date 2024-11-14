# Import your service.py file, assuming it's structured to contain all your data
import service

def play_game():
    chapter = 1
    player_answers = {}  # A dictionary to store the player's answers

    while chapter <= 4:  # Looping through the chapters
        print(f"Welcome to Chapter {chapter}\n")
        
        # Chapter 1: Present the user with scenarios
        if chapter == 1:
            print("Choose a scenario to read:")
            print("1. A Night of Reading and Reflection")
            print("2. Socializing in the Lounge")
            print("3. A Private Writing Session")
            scenario_choice = int(input("Enter the number of your choice: "))
            
            if scenario_choice == 1:
                scenario = service.scenario1_kadyrbek
            elif scenario_choice == 2:
                scenario = service.scenario2_kadyrbek
            elif scenario_choice == 3:
                scenario = service.scenario3_kadyrbek
            else:
                print("Invalid choice, please choose a valid scenario.")
                continue

        # Chapter 2: Present the user with different scenarios
        elif chapter == 2:
            print("Choose a scenario to read:")
            print("1. An Evening in the Sauna")
            print("2. Sunset at Sea")
            print("3. A Refreshing Yoga Class")
            scenario_choice = int(input("Enter the number of your choice: "))
            
            if scenario_choice == 1:
                scenario = service.scenario1_kymbatai
            elif scenario_choice == 2:
                scenario = service.scenario2_kymbatai
            elif scenario_choice == 3:
                scenario = service.scenario3_kymbatai
            else:
                print("Invalid choice, please choose a valid scenario.")
                continue

        # Chapter 3: Similarly handle Chapter 3 scenarios
        elif chapter == 3:
            print("Choose a scenario to read:")
            print("1. A Quiet Evening of Preparation")
            print("2. An Unexpected Emergency")
            print("3. Socializing with Passengers")
            scenario_choice = int(input("Enter the number of your choice: "))
            
            if scenario_choice == 1:
                scenario = service.scenario1_arstan
            elif scenario_choice == 2:
                scenario = service.scenario2_arstan
            elif scenario_choice == 3:
                scenario = service.scenario3_arstan
            else:
                print("Invalid choice, please choose a valid scenario.")
                continue

        # Chapter 4: Similarly handle Chapter 4 scenarios
        elif chapter == 4:
            print("Choose a scenario to read:")
            print("1. A Quiet Night Alone")
            print("2. A Late-Night Walk")
            print("3. A Private Practice Session")
            scenario_choice = int(input("Enter the number of your choice: "))
            
            if scenario_choice == 1:
                scenario = service.scenario1_kuba
            elif scenario_choice == 2:
                scenario = service.scenario2_kuba
            elif scenario_choice == 3:
                scenario = service.scenario3_kuba
            else:
                print("Invalid choice, please choose a valid scenario.")
                continue

        # Present scenario description
        print(f"\n--- Scenario: {scenario.title} ---")
        print(scenario.description)
        
        # Ask questions related to the chosen scenario
        for question in scenario.questions:
            print(f"\n{question.text}")
            for option in question.options:
                print(f"{option.id}. {option.text}")
            
            # Let the user choose an answer for each question
            answer_choice = int(input("Enter your choice number: "))
            
            # Store the answer
            player_answers[question.id] = answer_choice

        # After answering all questions in the current chapter, move to the next chapter
        chapter += 1

        # If it's the last chapter (chapter 4), end the game after answering questions
        if chapter > 4:
            print("\nGame Over! Checking your answers...\n")
            check_answers(player_answers)

def check_answers(player_answers):
    correct_answers = 0
    total_answers = 0

    # Loop through all scenarios in all chapters and evaluate answers
    for scenario in [service.scenario1_kadyrbek, service.scenario2_kadyrbek, service.scenario3_kadyrbek]:
        for question in scenario.questions:
            correct_option = next((opt for opt in question.options if opt.is_correct), None)
            player_answer = player_answers.get(question.id)

            if player_answer == correct_option.id:
                correct_answers += 1
            total_answers += 1

    for scenario in [service.scenario1_mysterious_visitor, service.scenario2_stormy_night, service.scenario3_hidden_message]:
        for question in scenario.questions:
            correct_option = next((opt for opt in question.options if opt.is_correct), None)
            player_answer = player_answers.get(question.id)

            if player_answer == correct_option.id:
                correct_answers += 1
            total_answers += 1

    # Repeat for other chapters as needed...

    # Evaluate win/loss
    win_percentage = (correct_answers / total_answers) * 100

    if win_percentage >= 75:
        print(f"You won! You answered {correct_answers}/{total_answers} correctly ({win_percentage}% success rate).")
    else:
        print(f"You lost. You answered {correct_answers}/{total_answers} correctly ({win_percentage}% success rate).")

# Start the game
play_game()