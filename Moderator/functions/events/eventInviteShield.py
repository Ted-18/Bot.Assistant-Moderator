import re

import addons.Moderator.handlers.handlerInvitesShield as handlerInvitesShield

import addons.Moderator.settings.settingColors as settingColors
import addons.Moderator.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def inviteShieldCheck(message):
    if message.author.bot:
        return
    
    # Make a Regex to check if the message contains a valid invite link ignoring the case
    pattern = re.compile(r"(https?:\/\/)?(www\.)?(discord\.(gg|io|me|li|com)|discordapp\.com\/invite)\/.+[a-z]", re.IGNORECASE)
    if pattern.search(message.content) == None:
        return
    
    # If the user has the permission to send invites
    if message.author.guild_permissions.manage_guild:
        return

    if handlerInvitesShield.inviteShieldCheck(message) != True:
        return

    # Send a message to the user
    embed = discord.Embed(
        title="Invite Shield", 
        description="You are not allowed to send invites in this server.", 
        color=settingColors.red
        )
    
    embed.set_thumbnail(url=settingThumbnail.adminIcon)
    
    embed.set_author(name="Moderator", icon_url=settingThumbnail.adminIcon)
            
    embed.set_footer(text=message.author, icon_url=message.author.display_avatar)

    await message.reply(embed=embed, mention_author=True, delete_after=20)

    # Delete the message
    await message.delete()
