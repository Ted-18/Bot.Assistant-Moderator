import services.serviceDatabase as serviceDatabase      
from services.serviceLogger import consoleLogger as Logger

from settings.settingBot import debug

def inviteShieldUpdate(ctx, enabled):
    # Update the invite shield status
    requestFormat = """
        UPDATE addon_moderator_inviteshield
        SET status = %s
        WHERE serverID = %s
    """
    requestSettings = (enabled, ctx.guild.id)

    try:
        if debug == True:
            Logger.debug("[HANDLER][MODERATOR][INVITE SHIELD][UPDATE] Updating the invite shield status -> " + str(enabled))

        serviceDatabase.makeRequest(requestFormat, requestSettings)

    except Exception as error:
        Logger.error("[HANDLER][MODERATOR][INVITE SHIELD][UPDATE] DB error inviteShield -> " + str(error))


def inviteShieldCreate(ctx, enabled):
    # Create the invite shield status
    requestFormat = """
        INSERT INTO addon_moderator_inviteshield (serverID, status)
        VALUES (%s, %s)
    """
    requestSettings = (ctx.guild.id, enabled)

    try:
        if debug == True:
            Logger.debug("[HANDLER][MODERATOR][INVITE SHIELD][CREATE] Creating the invite shield status -> " + str(enabled))

        serviceDatabase.makeRequest(requestFormat, requestSettings)

    except Exception as error:
        Logger.error("[HANDLER][MODERATOR][INVITE SHIELD][CREATE] DB error inviteShield -> " + str(error))


def inviteShieldCheck(ctx):
    # Check if the server ID is in the database
    requestFormat = """
        SELECT serverID
        FROM addon_moderator_inviteshield
        WHERE serverID = %s
    """
    requestSettings = (ctx.guild.id,)

    try:
        if debug == True:
            Logger.debug("[HANDLER][MODERATOR][INVITE SHIELD][CHECK] Checking if the server ID is in the database -> " + str(ctx.guild.id))

        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)

        if result == []:
            return False
        else:
            return True

    except Exception as error:
        Logger.error("[HANDLER][MODERATOR][INVITE SHIELD][CHECK] DB error inviteShield -> " + str(error))

        return False