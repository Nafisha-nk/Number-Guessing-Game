# Number-Guessing-Game

A fun and interactive command-line number guessing game where you test your intuition and number sense against the computer!

## Features ✨

- **Multiple Difficulty Levels**: Easy (10 chances), Medium (5 chances), Hard (3 chances)
- **Smart Hint System**: Get helpful clues when you're stuck
- **Timer Tracking**: See how fast you can guess the number
- **High Score System**: Track your best performances across sessions
- **Multiple Rounds**: Play as many times as you want
- **Beautiful CLI Interface**: Clean, user-friendly command-line experience
- **Persistent Data**: Your high scores are saved automatically

## How to Play 🎮

1. The computer randomly selects a number between 1 and 100
2. Choose your difficulty level
3. Enter your guesses based on the feedback
4. Use hints when you need help
5. Try to guess the number in the fewest attempts possible!

## Installation & Setup 🚀

### Prerequisites
- Python 3.6 or higher

### Running the Game

1. **Download the game:**
   ```bash
   # Save the code as number_guessing_game.py
   ```

2. **Run the game:**
   ```bash
   python number_guessing_game.py
   ```
   
   Or if you have multiple Python versions:
   ```bash
   python3 number_guessing_game.py
   ```

### Verification
To check if Python is installed:
```bash
python --version
# or
python3 --version
```

## Game Instructions 📖

### Difficulty Levels
- **Easy**: 10 chances - Perfect for beginners
- **Medium**: 5 chances - Balanced challenge
- **Hard**: 3 chances - For the truly adventurous!

### Hint System
The game provides intelligent hints when:
- You're running low on chances
- You've made several guesses
- You're close to the number

Hints may include:
- "You're getting warmer/cold"
- Even/Odd information
- Range hints (above/below 50)

### High Scores
Your best performances are saved in `high_scores.json` and include:
- Fewest number of attempts
- Fastest completion time
- Date of achievement

## Sample Gameplay 🎯

```
==================================================
      WELCOME TO THE NUMBER GUESSING GAME!
==================================================

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice (1-3): 2

Great! You have selected the Medium difficulty level.
You have 5 chances to guess the number.

Enter your guess [1/5]: 50
Incorrect! The number is LESS than your guess.

Enter your guess [2/5]: 25
Incorrect! The number is GREATER than your guess.

💡 HINT: You're getting warmer! The number is within 15 of your previous guesses.

Enter your guess [3/5]: 35
Incorrect! The number is LESS than your guess.

💡 HINT: You're very close! 
💡 EXTRA HINT: The number is ODD.

Enter your guess [4/5]: 33

🎉 Congratulations! You guessed the correct number in 4 attempts!
⏰ Time taken: 25.3 seconds
🎉 New high score for Medium difficulty!
```

## File Structure 📁

```
number_guessing_game.py    # Main game file
high_scores.json          # Auto-generated high score data (created after first play)
```

## Troubleshooting 🔧

### Common Issues

1. **"python: command not found"**
   - Install Python from [python.org](https://python.org)
   - Or try `python3` instead of `python`

2. **Permission Errors** (Linux/macOS)
   ```bash
   chmod +x number_guessing_game.py
   ```

3. **Syntax Errors**
   - Ensure you copied the entire code correctly
   - Check for missing brackets or quotes

4. **File Not Found**
   - Make sure you're in the correct directory
   - Use `ls` (Linux/macOS) or `dir` (Windows) to verify

### Testing Your Setup
```bash
echo "print('Python works!')" > test.py
python test.py
```
If you see "Python works!", you're ready to play!

## Game Tips 🏆

- **Start with medium guesses** (like 50) to divide the range quickly
- **Pay attention to patterns** in the feedback
- **Use hints strategically** - don't wait until your last chance
- **Track your previous guesses** to avoid repeating numbers
- **Practice makes perfect** - try different strategies!

## Features in Detail 🔍

### Smart Hint System
- Proximity detection based on previous guesses
- Mathematical properties (even/odd)
- Range suggestions when critically low on chances
- Adaptive hint frequency based on performance

### High Score Tracking
- Separate records for each difficulty level
- Considers both attempts and completion time
- Persistent storage between game sessions
- Timestamp of achievements

### User Experience
- Input validation for all user entries
- Clear progress indicators
- Visual feedback with emojis
- Graceful error handling

## Contributing 🤝

Feel free to modify and enhance the game! Some ideas:
- Add more difficulty levels
- Implement a multiplayer mode
- Create a graphical interface
- Add sound effects
- Include statistics and analytics

## License 📄

This is a free educational project. Feel free to use and modify as needed!

https://roadmap.sh/projects/number-guessing-game

---

**Ready to test your guessing skills? Run the game and see if you can beat the high scores!** 🎯✨
