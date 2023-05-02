import addons.Moderator.handlers.handlerBanWords as handlerBanWords

import addons.Moderator.settings.settingColors as settingColors
import addons.Moderator.settings.settingThumbnail as settingThumbnail    

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def banWordsRemove(ctx, word):
    
        # PERMISSIONS CHECK
        import addons.Moderator.functions.services.servicePermission as servicePermission
        if await servicePermission.permissionCheck(ctx, "cmdBanWordRemove") == False:
            return
    
        # COMMAND

        # Verify if the word is already in the database
        if handlerBanWords.isWordInList(ctx, word) == False:
            embed = discord.Embed(
                title = "Ban word not found",
                description = "This word is not in the ban words list.\n\n`" + word + "`",
                color = settingColors.red
                )
            embed.set_thumbnail(url=settingThumbnail.adminIcon)

            await ctx.respond(embed=embed)
            return
        
        # EMBED
        embed = discord.Embed(
            title = "Ban word removed",
            description = "The word `" + word + "` has been removed from the ban words list.",
            color = settingColors.green
            )
        
        embed.set_thumbnail(url=settingThumbnail.adminIcon)

        await ctx.respond(embed=embed)
        
        # DATABASE
        handlerBanWords.banWordsRemove(ctx, word)