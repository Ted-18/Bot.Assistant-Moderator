import addons.Moderator.handlers.handlerBanWords as handlerBanWords

import addons.Moderator.settings.settingColors as settingColors
import addons.Moderator.settings.settingThumbnail as settingThumbnail    

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def banWordsAdd(ctx, word):
    
        # PERMISSIONS CHECK
        import addons.Moderator.functions.services.servicePermission as servicePermission
        if await servicePermission.permissionCheck(ctx, "cmdBanWordAdd") == False:
            return
    
        # COMMAND

        # Verify if the word is already in the database
        if handlerBanWords.isWordInList(ctx, word) == True:
            embed = discord.Embed(title="Ban Words", description="This word is already in the ban words list.\n\n`" + word + "`", color=settingColors.red)
            embed.set_thumbnail(url=settingThumbnail.adminIcon)

            await ctx.respond(embed=embed)
            return    

        embed = discord.Embed(
            title="Ban Words",
            description="The word has been added to the ban words list.\n\n`" + word + "`",
            color=settingColors.green
        )
        embed.set_thumbnail(url=settingThumbnail.adminIcon)

        await ctx.respond(embed=embed)

        # Add the word to the database
        handlerBanWords.banWordsAdd(ctx, word)