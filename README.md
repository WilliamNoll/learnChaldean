# Learn Chaldean

A Python-based flashcard application for learning Chaldean (Neo-Aramaic/Syriac/ܣܘܪܝܬ) vocabulary and grammar. The application supports both vocabulary learning and audio pronunciation practice.

## Features

- **Dual Learning Modes**
  - Syriac-to-English: Practice translating Syriac words to English
  - English-to-Syriac: Practice translating English words to Syriac

- **Comprehensive Content**
  - Chaldean Grammar: Nouns, Adjectives, Verbs, Pronouns, Prepositions
  - Introductory Chaldean: Basic vocabulary organized by topics
  - Audio pronunciation support for all entries

- **Interactive Interface**
  - Hierarchical topic selection with checkboxes
  - Scrollable topic lists
  - Hint system for learning assistance
  - Audio pronunciation feature
  - Progress tracking

## Installation

1. Ensure you have Python installed (Python 3.x recommended)
2. Install required dependencies:
   ```bash
   pip install tkinter pygame
   ```
3. Clone this repository
4. Place audio files in an `audio` directory within the project folder

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. **Select Learning Mode**
   - Use the "Switch Mode" button to toggle between Syriac-to-English and English-to-Syriac modes

3. **Choose Content**
   - Select a book (Chaldean Grammar or Introductory Chaldean)
   - Choose a category
   - Select specific topics using the checkboxes

4. **Practice**
   - View the word/phrase
   - Enter your answer
   - Click "Answer" to check
   - Use "Hint" for assistance
   - Click "Pronounce" to hear the pronunciation
   - Click "Next" for a new word

## Adding New Content

### Vocabulary Structure
Each vocabulary entry follows this format:
```python
("ܣܘܪܝܬ", "English", "audio_file.mp3", "MM:SS", "MM:SS")
# Syriac word, English meaning, audio file, start time, end time
```

### Adding to Existing Categories
1. Locate the appropriate Python file in the `IntroductoryChaldean` directory
2. Add new entries to the `syriac_letters` list following the format above
3. Ensure audio files are placed in the `audio` directory
4. Update timestamps to avoid overlap with existing entries

### Creating New Categories
1. Create a new Python file in the `IntroductoryChaldean` directory
2. Define the `syriac_letters` list with your entries
3. Add the new category to `book_categories` in `main.py`

## Special Character Input

When entering Syriac text, use these special combinations:
- `Shift+J`: Elongates a letter
- `Shift+J`: Produces a ̮ symbol
- `Right Alt+U`: Produces a syame silencer
- `Taw + Yoth / Taw + Alap + heh-yodh`: Creates a new symbol

## File Structure

```
learnChaldean/
├── main.py                 # Main application file
├── audio/                  # Audio files directory
├── IntroductoryChaldean/   # Basic vocabulary modules
│   ├── greetings.py
│   ├── family.py
│   └── ...
└── Chaldean Grammar/       # Grammar modules
    ├── nouns.py
    ├── verbs.py
    └── ...
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your content following the established format
4. Submit a pull request

## Notes

- Audio files should be in MP3 format
- Timestamps should be in MM:SS format
- Ensure proper Syriac font is installed (East Syriac Adiabene recommended)
- Audio files should be named consistently (e.g., audio_IC01.mp3, audio_CG01.mp3)

## License

[Add your license information here]
