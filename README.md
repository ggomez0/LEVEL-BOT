# LevelBot

LevelBot is a Python project designed to fetch flight prices from the FlyLevel API and send notifications via Telegram when prices drop below a specified threshold. This project utilizes GitHub Actions to run the script on a schedule.

## Project Structure

```
levelbot
├── src
│   └── index.py          # Main logic for fetching flight prices and sending notifications
├── .github
│   └── workflows
│       └── cronjob.yml   # GitHub Actions workflow for scheduling the script
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd levelbot
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Telegram:**
   - Obtain your Telegram bot token and chat ID.
   - Update the `telegram_token` and `telegram_chat_id` variables in `src/index.py` with your credentials.

## Usage

The script is designed to run automatically every 20 minutes via GitHub Actions. However, you can also run it locally by executing:

```bash
python src/index.py
```

## GitHub Actions

The project includes a GitHub Actions workflow defined in `.github/workflows/cronjob.yml`, which schedules the script to run every 20 minutes using the following cron job configuration:

```
*/20 * * * *
```

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.