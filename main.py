import random
import os
import json
import matplotlib.pyplot as plt
from datetime import datetime

wordList = [
    { "word": "rainbow", "hint": "A colorful arc in the sky" },
    { "word": "javascript", "hint": "A popular programming language" },
    { "word": "hangman", "hint": "The game you are playing" },
    { "word": "apple", "hint": "A popular fruit" },
    { "word": "banana", "hint": "A yellow fruit" },
    { "word": "car", "hint": "A vehicle that runs on roads" },
    { "word": "computer", "hint": "An electronic device for processing data" },
    { "word": "mountain", "hint": "A large natural elevation of the earth's surface" },
    { "word": "ocean", "hint": "A vast body of salt water" },
    { "word": "guitar", "hint": "A stringed musical instrument" },
    { "word": "tree", "hint": "A tall plant with a trunk and branches" },
    { "word": "dog", "hint": "A domesticated carnivorous mammal" },
    { "word": "cat", "hint": "A small domesticated carnivorous mammal" },
    { "word": "house", "hint": "A building for human habitation" },
    { "word": "sun", "hint": "The star that provides light and heat to the earth" },
    { "word": "moon", "hint": "Earth's natural satellite" },
    { "word": "star", "hint": "A luminous point in the night sky" },
    { "word": "book", "hint": "A set of written or printed pages" },
    { "word": "school", "hint": "A place for education" },
    { "word": "laptop", "hint": "A portable personal computer" },
    { "word": "phone", "hint": "A device for voice communication" },
    { "word": "camera", "hint": "A device for taking photographs" },
    { "word": "bicycle", "hint": "A two-wheeled vehicle powered by pedaling" },
    { "word": "football", "hint": "A popular sport played with a round ball" },
    { "word": "basketball", "hint": "A sport played with a ball and hoops" },
    { "word": "soccer", "hint": "A sport played with a round ball, also known as football" },
    { "word": "IceCream", "hint": "A frozen dessert made from dairy products" },
    { "word": "chocolate", "hint": "A sweet treat made from cocoa" },
    { "word": "beach", "hint": "A sandy shore beside a body of water" },
    { "word": "city", "hint": "A large town or populated area" },
    { "word": "vacation", "hint": "An extended period of leisure travel" },
    { "word": "shopping", "hint": "The activity of buying goods" },
    { "word": "party", "hint": "A social gathering" },
    { "word": "holiday", "hint": "A day of celebration or relaxation" },
    { "word": "friend", "hint": "A person with whom you share a close bond" },
    { "word": "family", "hint": "A group of related individuals" },
    { "word": "weather", "hint":"The state of the atmosphere at a particular time" },
    { "word": "temperature", "hint": "A measure of the warmth or coldness of an object or environment" },
    { "word": "earth", "hint": "The third planet from the Sun" },
    { "word": "sky", "hint": "The expanse of air above the earth" },
    { "word": "cloud", "hint": "A visible mass of condensed water vapor" },
    { "word": "rain", "hint": "Water droplets falling from the sky" },
    { "word": "snow", "hint": "Frozen water crystals that fall from the sky" },
    { "word": "wind", "hint": "The movement of air" },
    { "word": "lightning", "hint": "A flash of light produced by an electrical discharge" },
    { "word": "thunder", "hint": "The sound caused by lightning" },
    { "word": "volcano", "hint": "An opening in the Earth's crust through which lava and gases escape" },
    { "word": "earthquake", "hint": "A sudden shaking of the ground" },
    { "word": "desert", "hint": "A barren area of land with little water and vegetation" },
    { "word": "forest", "hint": "A large area covered chiefly with trees" },
    { "word": "river", "hint": "A large, flowing body of water" },
    { "word": "lake", "hint": "A large body of water surrounded by land" },
    { "word": "island", "hint": "A piece of land surrounded by water" },
    { "word": "continent", "hint": "One of the main landmasses on Earth" },
    { "word": "country", "hint": "A nation with its own government" },
    { "word": "flag", "hint": "A piece of fabric with a design used as a symbol" },
    { "word": "nationality", "hint": "The status of belonging to a particular nation" },
    { "word": "government", "hint": "The group of people governing a country" },
    { "word": "president", "hint": "The head of state in some countries" },
    { "word": "capital", "hint": "The city where the government is based" },
    { "word": "currency", "hint": "A system of money used in a country" },
    { "word": "market", "hint": "A place where goods are bought and sold" },
    { "word": "economy", "hint": "The wealth and resources of a country or region" },
    { "word": "job", "hint": "A role in which someone works for pay" },
    { "word": "career", "hint": "A profession or occupation" },
    { "word": "salary", "hint": "A fixed regular payment for work" },
    { "word": "company", "hint": "A business or firm" },
    { "word": "employee", "hint": "A person employed by a company" },
    { "word": "employer", "hint": "A person or organization that hires employees" },
    { "word": "manager", "hint": "A person responsible for managing a company or department" },
    { "word": "team", "hint": "A group of people working together" },
    { "word": "leader", "hint": "A person who leads a group or organization" },
    { "word": "meeting", "hint": "An assembly of people for discussion" },
    { "word": "conference", "hint": "A large formal meeting" },
    { "word": "phone", "hint": "A device used to make calls" },
    { "word": "address", "hint": "The location where someone lives or works" },
    { "word": "message", "hint": "A communication or information sent" },
    { "word": "letter", "hint": "A written or printed message" },
    { "word": "email", "hint": "A method of sending messages electronically" },
    { "word": "text", "hint": "A written message sent by mobile phone" },
    { "word": "social media", "hint": "Websites and apps for social interaction" },
    { "word": "website", "hint": "A collection of web pages" },
    { "word": "blog", "hint": "A website containing posts on various topics" },
    { "word": "internet", "hint": "A global computer network" },
    { "word": "technology", "hint": "The application of scientific knowledge for practical purposes" },
    { "word": "robot", "hint": "A machine capable of carrying out tasks automatically" },
    { "word": "artificial intelligence", "hint": "The simulation of human intelligence in machines" },
    { "word": "data", "hint": "Facts and statistics collected for reference" },
    { "word": "programming", "hint": "The process of writing code for computers" },
]

TRIES = 6
SCORE_FILE = "hangman_scores.json"

def hangman(tries):
    stages = [
        """
        1st state 
                           --------
                           |      |
                           |
                           |
                           |
                           |
                           -
                        """,
        """
        2nd state
                           --------
                           |      |
                           |      O
                           |
                           |
                           |
                           -
                        """,
        """
        3rd state
                           --------
                           |      |
                           |      O
                           |     /|
                           |      |
                           |
                           -
                        """,
        """
        4th state
                           --------
                           |      |
                           |      O
                           |     /|\\
                           |      |
                           |
                           -
                        """,
        """
        5th state
                           --------
                           |      |
                           |      O
                           |     /|\\
                           |      |
                           |     /
                           -
                        """,
        """
        6th state
                           --------
                           |      |
                           |      O
                           |     /|\\
                           |      |
                           |     / \\
                           -
                        """,
    ]
    return stages[TRIES - tries]

def get_word():
    word_dict = random.choice(wordList)
    return word_dict["word"].upper(), word_dict["hint"]

def load_scores():
    """Load scores from file or create default score data"""
    if os.path.exists(SCORE_FILE):
        try:
            with open(SCORE_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Score file corrupted. Creating new score file.")
    
    # Default score data
    return {
        "player_name": "Player",
        "games": [],
        "total_wins": 0,
        "total_losses": 0,
        "stats": {
            "last_played": None,
            "longest_streak": 0,
            "current_streak": 0
        }
    }

def save_scores(scores):
    """Save scores to file"""
    with open(SCORE_FILE, 'w') as file:
        json.dump(scores, file, indent=4)

def update_scores(scores, won, word):
    """Update scores with game result"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Update game history
    game_record = {
        "date": now,
        "word": word,
        "result": "win" if won else "loss",
        "letters_left": 0 if won else word.count('_')
    }
    scores["games"].append(game_record)
    
    # Update totals
    if won:
        scores["total_wins"] += 1
        scores["stats"]["current_streak"] += 1
    else:
        scores["total_losses"] += 1
        scores["stats"]["current_streak"] = 0
    
    # Update stats
    scores["stats"]["last_played"] = now
    if scores["stats"]["current_streak"] > scores["stats"]["longest_streak"]:
        scores["stats"]["longest_streak"] = scores["stats"]["current_streak"]
    
    # Save updated scores
    save_scores(scores)
    return scores

def show_score_stats(scores):
    """Display score statistics"""
    print("\n----- HANGMAN STATISTICS -----")
    print(f"Player: {scores['player_name']}")
    print(f"Total Games: {scores['total_wins'] + scores['total_losses']}")
    print(f"Wins: {scores['total_wins']}")
    print(f"Losses: {scores['total_losses']}")
    
    if scores['total_wins'] + scores['total_losses'] > 0:
        win_percent = (scores['total_wins'] / (scores['total_wins'] + scores['total_losses'])) * 100
        print(f"Win Rate: {win_percent:.1f}%")
    
    print(f"Current Streak: {scores['stats']['current_streak']}")
    print(f"Longest Streak: {scores['stats']['longest_streak']}")
    
    if scores["stats"]["last_played"]:
        print(f"Last Played: {scores['stats']['last_played']}")
    print("-----------------------------")

def show_progress_graph(scores):
    """Display a graph showing win/loss comparison"""
    if not scores["games"]:
        print("No game data available to display graph.")
        return
        
    # Extract win/loss data for graph
    games_count = min(len(scores["games"]), 20)  # Show at most last 20 games
    recent_games = scores["games"][-games_count:]
    
    # Prepare data for plotting
    game_numbers = list(range(1, games_count + 1))
    results = [1 if game["result"] == "win" else 0 for game in recent_games]
    
    # Calculate cumulative wins and win rate
    cumulative_wins = []
    win_rates = []
    win_count = 0
    
    for i, result in enumerate(results):
        if result == 1:
            win_count += 1
        cumulative_wins.append(win_count)
        win_rates.append(win_count / (i + 1))
    
    try:
        # Create plot
        plt.figure(figsize=(10, 6))
        
        # Plot bars for win/loss
        plt.subplot(2, 1, 1)
        plt.bar(game_numbers, results, color=['green' if r == 1 else 'red' for r in results])
        plt.title('Hangman Game Results (Recent Games)')
        plt.xlabel('Game Number')
        plt.ylabel('Result (1=Win, 0=Loss)')
        plt.yticks([0, 1], ['Loss', 'Win'])
        
        # Plot win rate line
        plt.subplot(2, 1, 2)
        plt.plot(game_numbers, win_rates, 'b-', marker='o')
        plt.title('Win Rate Progression')
        plt.xlabel('Game Number')
        plt.ylabel('Win Rate')
        plt.ylim(0, 1.1)
        
        plt.tight_layout()
        plt.savefig('hangman_progress.png')
        plt.close()
        
        print("\nProgress graph saved as 'hangman_progress.png'")
        print("You can view it in an image viewer.")
    except Exception as e:
        print(f"\nCouldn't create graph: {e}")
        print("Make sure matplotlib is installed (pip install matplotlib)")

def play(word, hint, initial_tries, scores):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = initial_tries

    print("\n-------------Welcome to Hangman-------------\n")
    print(f"Player: {scores['player_name']} | Wins: {scores['total_wins']} | Losses: {scores['total_losses']}")
    print(f"Current Streak: {scores['stats']['current_streak']} | Best Streak: {scores['stats']['longest_streak']}")
    print("\nHint:", hint)
    print(hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Guess a letter or the whole word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Invalid guess. Please enter a letter or a valid word.")

        print(hangman(tries))
        print(word_completion)
        print(f"Tries left: {tries}")
        print(f"Guessed letters: {', '.join(guessed_letters)}\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Better luck next time!")
    
    # Update scores
    update_scores(scores, guessed, word)
    return guessed

def setup_player(scores):
    """Set up player name if not already set"""
    if scores.get("player_name") == "Player":
        name = input("Enter your name (or press Enter to stay as 'Player'): ").strip()
        if name:
            scores["player_name"] = name
            save_scores(scores)
    return scores

def main():
    # Load scores from file
    scores = load_scores()
    scores = setup_player(scores)
    
    while True:
        print("\n=== HANGMAN GAME MENU ===")
        print("1. Play Game")
        print("2. View Statistics")
        print("3. Show Progress Graph")
        print("4. Change Player Name")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            word, hint = get_word()
            play(word, hint, TRIES, scores)
        elif choice == '2':
            show_score_stats(scores)
        elif choice == '3':
            show_progress_graph(scores)
        elif choice == '4':
            name = input("Enter new player name: ").strip()
            if name:
                scores["player_name"] = name
                save_scores(scores)
                print(f"Player name changed to {name}")
        elif choice == '5':
            print("Thanks for playing Hangman! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()