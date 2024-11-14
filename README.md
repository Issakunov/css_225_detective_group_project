# css_225_detective_group_project
1. Code Hostingb                            
•	Repository: The code for this project is hosted on GitHub, where changes are tracked, and version control is managed. Team members can access the repository, view previous versions, and contribute via pull requests.
2. Languages and Technologies
•	Primary Language: Python (game logic, gameplay mechanics, and interactions are implemented in Python)
•	Libraries Used: Basic Python libraries (specify additional libraries here if needed).
3. System Requirements and Supported Platforms
•	Supported Operating Systems: Windows, macOS, Linux
•	Python Version: Python 3.8 or later
•	Required Dependencies: Libraries specified in requirements.txt
4. Building, Running, and Deploying the Game
•	Installation of Dependencies:
bash
Copy code
pip install -r requirements.txt
•	Running the Game.     :
bash
Copy code
python main.py
This command starts the game from the main entry point (main.py), initializing character selection and the game’s main loop.
5. Architecture Overview
•	Modules and Structure:
o	characters/: Contains separate classes or modules for each character (Arstan, Kymbatai, Ata, and Kadyrbek), along with their unique scenarios.                                        
o	scenarios/: Defines scenarios and alibis for each character’s storyline.
o	game_manager.py: Controls gameplay flow, manages character selection, and directs the narrative.
o	main.py: Entry point, initializing game settings and managing the main game loop.
•	Character Structure: Each character has unique chapters and scenarios with specific questions that contribute to the game’s investigation and storyline.
 
6. Starting the Game
1.	Character Selection: At the beginning of each game session, players select one of four available characters: Arstan (doctor), Kymbatai (taxi driver), Ata (singer), or Kadyrbek (high school teacher).
2.	Game Flow: After character selection the player need to read the randomly chosen scenario and be ready to respond to investigative questions. Each scenario advances based on player responses, leading to a conclusion.
3.	Restarting the Game: To replay with a different character, the game must be restarted from the beginning.
7. Error Handling and Logging
•	Error Handling: Try-except blocks should handle exceptions for invalid inputs or runtime issues.
•	Logging: Consider adding logging to track gameplay events, player choices, and any system errors.
8. Additional Notes
•	Expansion Possibilities: The game is designed to support additional characters and scenarios with minimal modification to the main structure.
•	Testing and Debugging: Test the game after adding any new scenarios or characters to ensure continuity and proper branching in the storyline.

