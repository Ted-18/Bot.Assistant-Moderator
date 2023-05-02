import prettytable

import addons.Moderator.handlers.handlerBanWords as handlerBanWords

import addons.Moderator.settings.settingColors as settingColors
import addons.Moderator.settings.settingThumbnail as settingThumbnail    

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def banWordsList(ctx):
    
        # PERMISSIONS CHECK
        import addons.Moderator.functions.services.servicePermission as servicePermission
        if await servicePermission.permissionCheck(ctx, "cmdBanWordList") == False:
            return
    
        # COMMAND
        
        # EMBED
        embed = discord.Embed(
            title = "Ban words list",
            description = "Here is the list of all the words that are banned on this server.",
            color = settingColors.blue
            )
        
        embed.set_thumbnail(url=settingThumbnail.adminIcon)

        await ctx.respond(embed=embed)

        # DATABASE
        resultDatabase = handlerBanWords.getBanWords(ctx)

        banWords = []

        for banWord in resultDatabase:
            banWords.append(banWord[0])

        # Make a table with prettytable
        table = prettytable.PrettyTable()

        table.field_names = ["Ban words"]

        for banWord in banWords:
            table.add_row([banWord])

        # Send the table
        await ctx.send("`" + str(table) + "`")