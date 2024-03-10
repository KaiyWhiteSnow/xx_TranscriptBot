import discord
from discord.ext import commands
from .head import head

class Transcripts(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    
    def escape_html(self, text):
        return discord.utils.escape_markdown(discord.utils.escape_mentions(text))

    def escape_attachments(self, attachments):
        if not attachments:
            return ""

        attachment_list = []
        for attachment in attachments:
            attachment_list.append(f'<img src="{discord.utils.escape_markdown(attachment.url)}" style="max-width: 800px; max-height: 600px; margin: 5px" alt="Attachment">')

        return " ".join(attachment_list)


    @commands.hybrid_command(
        name="transcriptchannel", 
        usage="/transcriptChannel <channel name>", 
        description="Adds member to your clan",
    )
    async def transcriptchannel(self, ctx: commands.Context, channel: discord.TextChannel):
        threads = channel.archived_threads()
        async for thread in threads:
            with open(f"{thread.name}.html", "w", encoding="utf-8") as file:
                # Write some content to the file
                file.write(f"{head}")
                file.write(f"Thread ID: {thread.id}, Name: {thread.name}")
                async for message in thread.history(limit=None):
                    content = self.escape_html(message.content)
                    attachments = self.escape_attachments(message.attachments)
                    pfp = message.author.display_avatar
                    color = message.author.color
                    file.write(f'<div><img src="{pfp}" style="max-width: 40px; max-height: 40px; border-radius: 50%;"> <strong><a style="color: {color}">{message.author.name}</a>:</strong> {content}</div>')
                    file.write(f'<div>{attachments}</div>')

        
async def setup(bot: commands.Bot):
    await bot.add_cog(Transcripts(bot))