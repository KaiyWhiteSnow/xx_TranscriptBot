# xx_TranscriptBot

## Overview

This Discord bot provides functionality to create and send transcripts of archived threads in text channels. The transcripts are saved as HTML files and can be easily shared with users. The bot includes commands to create transcripts for specified channels and send them to selected users.
Features

- Transcript Creation: Generate HTML transcripts for archived threads in a specified text channel.
- User Interaction: Send generated transcripts to selected users via direct messages.

## Installation and Setup

- Clone the repository to your local machine.
- Install the required Python dependencies:

### Install requirements

```
pip install -r requirements.txt
```
### Create .env

In root create .env with following fields

```
eternal_prefix = "" // Deffault prefix is set as "!"
eternal_token = "" // Your token

```
Make sure to have the necessary permissions to run the bot on your Discord server.
Modify the head.py file to customize the HTML head content if needed.
Run the bot using the following command:

### run

```
python3 -m src
```

### Commands

1. /transcriptchannel

    Description: Creates transcripts for archived threads in the specified text channel.
    Usage: /transcriptchannel <channel name>
    Example: /transcriptchannel #general

2. /sendtranscript

    Description: Sends transcripts to the specified user via direct messages.
    Usage: /sendtranscript <username>
    Example: /sendtranscript @user123

## Project Structure

- /src/: Files for initialization.
- head.py: Contains the HTML head content for transcripts.
- out/: Directory to store generated transcripts in HTML format.

## Notes

    Ensure that the 'out' directory exists before using the bot.
    The bot requires the discord.py library. Install it using pip install discord.py.
    Customize the HTML head content in head.py as needed.

Feel free to extend and customize the bot according to your preferences and requirements. If you encounter any issues or have suggestions for improvement, please open an issue on the GitHub repository.

