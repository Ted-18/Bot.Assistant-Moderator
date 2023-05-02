import addons.Moderator.handlers.handlerInvitesShield as handlerInvitesShield

import addons.Moderator.settings.settingColors as settingColors
import addons.Moderator.settings.settingThumbnail as settingThumbnail    

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def inviteShield(ctx, enabled: bool):

    # PERMISSIONS CHECK
    import addons.Moderator.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdInviteShield") == False:
        return
    
    # COMMAND
    if enabled == True:
        embed = discord.Embed(title="Invite Shield", description="The invite shield has been enabled.", color=settingColors.green)
        embed.set_thumbnail(url=settingThumbnail.adminIcon)

        await ctx.respond(embed=embed)

        # If the server ID is not in the database
        if handlerInvitesShield.inviteShieldCheck(ctx) == False:
            handlerInvitesShield.inviteShieldCreate(ctx, enabled)
        else:
            handlerInvitesShield.inviteShieldUpdate(ctx, enabled)

    elif enabled == False:
        embed = discord.Embed(title="Invite Shield", description="The invite shield has been disabled.", color=settingColors.red)
        embed.set_thumbnail(url=settingThumbnail.adminIcon)

        await ctx.respond(embed=embed)

        # If the server ID is not in the database
        if handlerInvitesShield.inviteShieldCheck(ctx) == False:
            handlerInvitesShield.inviteShieldCreate(ctx, enabled)
        else:
            handlerInvitesShield.inviteShieldUpdate(ctx, enabled)