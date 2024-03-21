import asyncio
import logging

import discord
from discord.ext import commands

from .config import logger_config
from .config.discord_config import BOT_PREFIX

# Configure loggers - This must run before SQLAlchemy is initialized
logger_config.configure_logger(
    [
        "Bot.Main",
        "discord",
        "discord.http",
        "Bot.Transcript"
    ]
)


logger: logging.Logger = logging.getLogger("Bot.Main")
transcript_logger = logging.getLogger("Bot.Transcript")

# Setup bot instance
intents: discord.Intents = discord.Intents.all()
bot: commands.Bot = commands.Bot(BOT_PREFIX, intents=intents)


async def load_extensions():
    await bot.load_extension(__package__ + ".commands.transcript")


asyncio.run(load_extensions())


@bot.event
async def on_ready():
    # Sync commands once possible
    logger.debug("Waiting until bot is ready...")
    await bot.wait_until_ready()
    logger.debug("Syncing commands...")
    await bot.tree.sync()
    logger.debug("Commands synced!")
    # Announce version info and set status
    logger.info("Running discord.py %s", discord.__version__)
    logger.info("We have logged in as %s", bot.user.name)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=f"over xx Public Discord"
        )
    )
    logger.info("Ready!")


# bot.run is implemented in __main__