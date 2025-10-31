<p align="center">
  <img src="imgs/cookies_banner.png" alt="Cookie Bot Banner">
</p>

<h1 align="center">Cookie</h1>

<p align="center">
  A feature-rich Discord bot for retrieving information about anime, manga, and more.
</p>

## 🌟 Features

- **Anime & Manga Information:** Get details about your favorite anime and manga series.
- **Random Recommendations:** Discover new anime, manga, and characters.
- **Top Rankings:** Find the top-rated anime and manga.
- **Genre & Magazine Information:** Browse by genre or magazine.
- **Translation:** Translate text to Japanese.
- **Utility Commands:** Check the bot's latency, server information, and more.

## 🚀 Commands

### Anime
- `/angenres`: Get a list of all anime genres.
- `/ranime`: Get a random anime recommendation.
- `/anime [name]`: Get information about a specific anime.
- `/topanimes`: Get a list of the top-rated anime.

### Manga
- `/mgenres`: Get a list of all manga genres.
- `/rmanga`: Get a random manga recommendation.
- `/manga [name]`: Get information about a specific manga.
- `/topmangas`: Get a list of the top-rated manga.
- `/magazines`: Get a list of manga magazines.

### Characters
- `/rchar`: Get a random character.
- `/character [name]`: Get information about a specific character.

### Utility
- `/help`: Shows a list of all available commands.
- `/ping`: Checks the bot's latency.
- `/serverinfo`: Displays information about the server.
- `/say [message]`: Makes the bot say something.
- `/injp [text]`: Translates text to Japanese.

## 🛠️ Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/CoderRony955/Cookie
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Create a `.env` file:**
   - Create a file named `.env` in the root directory.
   - Add your Discord bot token to the `.env` file:
     ```
     DISCORD_BOT_TOKEN=your_bot_token
     ```
4. **Run the bot:**
   ```bash
   python main.py
   ```

## 💻 Technologies Used

- [Python](https://www.python.org/)
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [Jikan API](https://jikan.moe/)

## 🙏 Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.
