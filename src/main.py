import random

from service import service

# Dictionary to map chapters for easier selection

def main():
    # Step 1: Player selects a chapter
    correct_answers = 0
    print(service.game_objective)
    print("Available characters:")

    for character in service.character_list:
        print(character)
    
    character_id = int(input("Choose a character by ID: "))
    chosen_character = get_character_by_id(character_id)
    chosen_scenario = random.choice(chosen_character.scenario)

    
    # Step 3: Display Scenario Description and Questions
    print("***************************************")
    print("Please read the Scenario carefully!")
    print("***************************************")
    print("\nScenario Title:", chosen_scenario.title)
    print(chosen_scenario.description)

    # Step 4: Loop through each question and get player answers
    for question in chosen_scenario.questions:
        print("Answer the following question: ")
        print(question.text)
        for option in question.options:
            print(f"{option.id}. {option.text}")
        
        # Player selects an option
        answer_id = int(input("Choose your answer (by option ID): "))
        
        # Step 5: Check if the selected option is correct
        selected_option = next((opt for opt in question.options if opt.id == answer_id), None)
        if selected_option:
            if selected_option.correct_option:
                print("Correct answer!")
                correct_answers += 1
            else:
                print("Incorrect answer.")
        else:
            print("Invalid option selected.")
    
    # Step 6: Determine win or loss based on correct answers
    if correct_answers == 0:
        print("\nYour response to all four questions were incorrect, raising serious concerns regarding your involvement. You are now the primary suspect in this murder investigation and are placed under arrest!")
    elif correct_answers == 1:
        print("\nWith only one correct answer out of four, your responses have revealed significant inconsistencies. You are under strong suspicion and are now being taken into custody for further investigation.")
    elif correct_answers == 2:
        print("\nAlthough you answered two questions correctly, there are still unresolved discrepancies in your statements. You remain a suspect, and further investigation is required. You will be detained for additional questioning.")
    elif correct_answers == 3:
        print("\nYour responses to three of the four questions were correct, which dears up some doubts but does not fully eliminate suspicion. While you are not being arrested, you are still considered a person of interest and may be called for further questioning.")
    else:
        print("\nAll faur of your answers were correct, indicating consistency in your statements. At this time, there is no evidence to suspect your involvement in the murder, and you are free to go.")
    
    # if correct_answers == len(chosen_scenario.questions):
    #     print("\nCongratulations, you won this scenario!")
    # else:
    #     print("\nSorry, you lost this scenario. Better luck next time!")

# Run the game

def get_character_by_id(id):
    for character in service.character_list:
        if character.id == id:
            return character
        
main()