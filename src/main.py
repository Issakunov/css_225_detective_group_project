import random
import service

# Dictionary to map chapters for easier selection
chapters = {
    1: Chapter1,
    2: Chapter2,
    3: Chapter3,
    4: Chapter4
}

def main():
    # Step 1: Player selects a chapter
    print(service.game_objective)
    print("Choose a chapter (1-4):")
    for i in chapters:
        print(f"{i}. {chapters[i].title}")

    chosen_chapter = int(input("Enter chapter number: "))
    if chosen_chapter not in chapters:
        print("Invalid chapter choice. Please choose between 1 and 4.")
        return
    
    # Step 2: Randomly assign a scenario within the selected chapter
    selected_chapter = chapters[chosen_chapter]
    chosen_scenario = random.choice(selected_chapter.scenarios)
    
    # Step 3: Display Scenario Description and Questions
    print("\nScenario Title:", chosen_scenario.title)
    print(chosen_scenario.description)
    
    # Step 4: Loop through each question and get player answers
    correct_answers = 0
    for question in chosen_scenario.questions:
        print(f"\n{question.text}")
        for option in question.options:
            print(f"{option.id}. {option.text}")
        
        # Player selects an option
        answer_id = int(input("Choose your answer (by option ID): "))
        
        # Step 5: Check if the selected option is correct
        selected_option = next((opt for opt in question.options if opt.id == answer_id), None)
        if selected_option:
            if selected_option.is_correct:
                print("Correct answer!")
                correct_answers += 1
            else:
                print("Incorrect answer.")
        else:
            print("Invalid option selected.")
    
    # Step 6: Determine win or loss based on correct answers
    if correct_answers == len(chosen_scenario.questions):
        print("\nCongratulations, you won this scenario!")
    else:
        print("\nSorry, you lost this scenario. Better luck next time!")

# Run the game
main()