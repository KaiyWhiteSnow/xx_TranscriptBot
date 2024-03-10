import discord
from discord.ext import commands
from .head import head
import os

class Transcripts(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.out_dir = os.path.join(os.path.dirname(__file__), 'out')
    
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
        description="creates transcripts",
    )
    async def transcriptchannel(self, ctx: commands.Context, channel: discord.TextChannel):
        threads = channel.archived_threads()
        
        async for thread in threads:
            with open(os.path.join(self.out_dir, f"{thread.name}.html"), "w", encoding="utf-8") as file:
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
                    
    @commands.hybrid_command(
            name="sendtranscript", 
            usage="/sendtranscript <username>", 
            description="sends transcript to selected user",
        )
    async def sendtranscripts(self, ctx: commands.Context, user: discord.User):
        # Check if the 'out' directory exists
        if not os.path.exists(self.out_dir):
            await ctx.send("Error: 'out' directory not found.")
            return

        # Get a list of HTML files in the 'out' directory
        html_files = [file for file in os.listdir(self.out_dir) if file.endswith('.html')]

        # Check if there are HTML files in the 'out' directory
        if not html_files:
            await ctx.send("Error: No HTML files found in 'out' directory.")
            return

        # Get the path to the style.css file
        style_css_path = os.path.join(self.out_dir, 'style.css')

        # Check if style.css file exists
        if not os.path.exists(style_css_path):
            await ctx.send("Error: style.css file not found.")
            return

        try:
            # Send style.css file
            await user.send(file=discord.File(style_css_path))

            # Send each HTML file
            for html_file in html_files:
                html_file_path = os.path.join(self.out_dir, html_file)
                await user.send(file=discord.File(html_file_path))

            await ctx.send(f"Transcripts sent to {user.name}")
        except discord.errors.Forbidden:
            await ctx.send("Error: Unable to send files to the specified user. Make sure the user allows direct messages.")

        
async def setup(bot: commands.Bot):
    await bot.add_cog(Transcripts(bot))