# Telegram File Sharing Bot

This project is a Telegram bot designed for file sharing that requires users to join specified groups or channels set by the admin before accessing shared files or links. The bot allows the owner to designate other users as admins to assist with uploading files or links.

## Features

- **Admin Controls**: Admins can add or remove other admins, set required groups or channels, and manage file uploads.
- **User Access**: Users must join specified groups or channels to access shared files or links.
- **File Sharing**: Easily share files and links within the Telegram environment.

## Project Structure

```
telegram-file-sharing-bot
├── src
│   ├── bot.py               # Main entry point for the Telegram bot
│   ├── handlers
│   │   ├── admin.py         # Admin functionalities
│   │   ├── user.py          # User functionalities
│   │   └── __init__.py      # Initializes handlers module
│   ├── utils
│   │   ├── database.py       # Database interactions
│   │   ├── validators.py      # Input validation functions
│   │   └── __init__.py      # Initializes utils module
│   └── config.py            # Configuration settings
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd telegram-file-sharing-bot
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Configure the bot settings in `src/config.py`.
2. Run the bot:
   ```
   python src/bot.py
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.