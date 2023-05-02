import re

import addons.Moderator.handlers.handlerBanWords as handlerBanWords

import addons.Moderator.settings.settingColors as settingColors
import addons.Moderator.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()


async def banWordsCheck(message):

    if message.type != discord.MessageType.default:
        return
    
    if message.author.bot:
        return

    # Get all the words in the database for the server
    wordsDB = handlerBanWords.getBanWords(message)

    words = []

    for word in wordsDB:
        words.append(word[0])

    # Compare the message with the words in the database
    for word in words:
        if word in message.content:

            # Replace the word with asterisks
            asterisks = ""

            for i in range(len(word)):
                asterisks += "x"

            message.content = message.content.replace(word, asterisks)

            embed = discord.Embed(
                title="Message edited",
                description=message.content,
                color=settingColors.discordEmbed
            )

            embed.set_author(name="Moderator", icon_url=settingThumbnail.adminIcon)
            
            embed.set_footer(text=message.author, icon_url=message.author.display_avatar)

            await message.channel.send(embed=embed)

            try:
                await message.delete()
            except:
                pass
    