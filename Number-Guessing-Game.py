import random
import time
import json
import os
from datetime import datetime

class NumberGuessingGame:
    def __init__(self):
        self.high_scores_file = "high_scores.json"
        self.high_scores = self.load_high_scores()
        self.difficulty_levels = {
            '1': {'name': 'Easy', 'chances': 10},
            '2': {'name': 'Medium', 'chances': 5},
            '3': {'name': 'Hard', 'chances': 3}
        }
    
    def load_high_scores(self):
        """Load high scores from JSON file"""
        if os.path.exists(self.high_scores_file):
            try:
                with open(self.high_scores_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_high_scores(self):
        """Save high scores to JSON file"""
        with open(self.high_scores_file, 'w') as f:
            json.dump(self.high_scores, f, indent=2)
    
    def display_welcome_message(self):
        """Display welcome message and game rules"""
        print("\n" + "="*50)
        print("      WELCOME TO THE NUMBER GUESSING GAME!")
        print("="*50)
        print("I'm thinking of a number between 1 and 100.")
        print("You'll have limited chances to guess the correct number.")
        print("\nGame Features:")
        print("• Multiple difficulty levels")
        print("• Hints when you're stuck")
        print("• Timer to track your speed")
        print("• High score tracking")
        print("="*50)
    
    def get_difficulty_level(self):
        """Get difficulty level from user"""
        print("\nPlease select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        
        while True:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice in self.difficulty_levels:
                return choice
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
    
    def get_user_guess(self, attempt, total_chances):
        """Get and validate user's guess"""
        while True:
            try:
                guess = int(input(f"\nEnter your guess [{attempt}/{total_chances}]: "))
                if 1 <= guess <= 100:
                    return guess
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    def provide_hint(self, secret_number, previous_guesses, chances_used, total_chances):
        """Provide hints based on the game situation"""
        if chances_used < 2:
            return  # Don't provide hints too early
        
        print("\n💡 HINT: ", end="")
        
        # Check if user is close to the number
        closest_guess = min(previous_guesses, key=lambda x: abs(x - secret_number))
        difference = abs(closest_guess - secret_number)
        
        if difference <= 5:
            print("You're very close! The number is within 5 of one of your previous guesses.")
        elif difference <= 15:
            print("You're getting warmer! The number is within 15 of one of your previous guesses.")
        else:
            print("You're still quite far from the number.")
        
        # Provide additional hints based on chances used
        if chances_used >= total_chances * 0.7:
            if secret_number % 2 == 0:
                print("💡 EXTRA HINT: The number is EVEN.")
            else:
                print("💡 EXTRA HINT: The number is ODD.")
        
        if chances_used >= total_chances * 0.8:
            if secret_number < 50:
                print("💡 EXTRA HINT: The number is less than 50.")
            else:
                print("💡 EXTRA HINT: The number is greater than or equal to 50.")
    
    def update_high_score(self, difficulty_name, attempts, time_taken):
        """Update high score if current game is better"""
        key = difficulty_name.lower()
        
        if key not in self.high_scores:
            self.high_scores[key] = {
                'attempts': attempts,
                'time': time_taken,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print(f"🎉 New high score for {difficulty_name} difficulty!")
            return True
        
        current_best = self.high_scores[key]
        
        # Update if fewer attempts or same attempts but faster time
        if (attempts < current_best['attempts'] or 
            (attempts == current_best['attempts'] and time_taken < current_best['time'])):
            
            self.high_scores[key] = {
                'attempts': attempts,
                'time': time_taken,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print(f"🎉 New high score for {difficulty_name} difficulty!")
            return True
        
        return False
    
    def display_high_scores(self):
        """Display current high scores"""
        if not self.high_scores:
            print("\nNo high scores yet. Play a game to set one!")
            return
        
        print("\n" + "="*40)
        print("           HIGH SCORES")
        print("="*40)
        
        for difficulty in ['easy', 'medium', 'hard']:
            if difficulty in self.high_scores:
                score = self.high_scores[difficulty]
                print(f"{difficulty.title():<8} - {score['attempts']} attempts, "
                    f"{score['time']:.1f}s on {score['date']}")
    
    def play_round(self):
        """Play one round of the game"""
        # Setup game
        secret_number = random.randint(1, 100)
        difficulty_choice = self.get_difficulty_level()
        difficulty = self.difficulty_levels[difficulty_choice]
        max_chances = difficulty['chances']
        
        print(f"\nGreat! You have selected the {difficulty['name']} difficulty level.")
        print(f"You have {max_chances} chances to guess the number.")
        print("Let's start the game!")
        
        # Game variables
        attempts = 0
        previous_guesses = []
        start_time = time.time()
        
        # Game loop
        while attempts < max_chances:
            attempts += 1
            remaining_chances = max_chances - attempts
            
            guess = self.get_user_guess(attempts, max_chances)
            previous_guesses.append(guess)
            
            if guess == secret_number:
                end_time = time.time()
                time_taken = end_time - start_time
                
                print(f"\n🎉 Congratulations! You guessed the correct number in {attempts} attempts!")
                print(f"⏰ Time taken: {time_taken:.1f} seconds")
                
                # Update high score
                self.update_high_score(difficulty['name'], attempts, time_taken)
                break
            
            else:
                # Give feedback
                if guess < secret_number:
                    print("Incorrect! The number is GREATER than your guess.")
                else:
                    print("Incorrect! The number is LESS than your guess.")
                
                # Show remaining chances
                if remaining_chances > 0:
                    print(f"💡 You have {remaining_chances} chance(s) remaining.")
                
                # Provide hint if needed
                if (remaining_chances <= 2 or 
                    attempts >= max_chances * 0.6):
                    self.provide_hint(secret_number, previous_guesses, attempts, max_chances)
        
        else:
            # This runs if while loop completes without break (user lost)
            print(f"\n💔 Game Over! You've run out of chances.")
            print(f"The correct number was: {secret_number}")
        
        # Show previous guesses
        if previous_guesses:
            print(f"\n📊 Your guesses: {', '.join(map(str, previous_guesses))}")
    
    def play_game(self):
        """Main game loop"""
        self.display_welcome_message()
        
        while True:
            self.play_round()
            self.display_high_scores()
            
            # Ask if user wants to play again
            play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
            if play_again not in ['y', 'yes']:
                print("\nThank you for playing! Goodbye! 👋")
                break
        
        # Save high scores before exiting
        self.save_high_scores()

# Run the game
if __name__ == "__main__":
    try:
        game = NumberGuessingGame()
        game.play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing! 👋")
    except Exception as e:
        print(f"\nAn error occurred: {e}")