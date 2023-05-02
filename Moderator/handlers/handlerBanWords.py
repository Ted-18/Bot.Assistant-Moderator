import services.serviceDatabase as serviceDatabase      
from services.serviceLogger import consoleLogger as Logger

from settings.settingBot import debug

def isWordInList(ctx, word):
    # Check if the word is in the ban words list
    requestFormat = """
        SELECT word
        FROM addon_moderator_banwords
        WHERE serverID = %s AND word = %s
    """
    requestSettings = (ctx.guild.id, word)

    try:
        if debug == True:
            Logger.debug("[HANDLER][MODERATOR][BAN WORDS][CHECK] Checking if the word is in the ban words list -> " + str(word))

        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)

        if result == []:
            return False
        else:
            return True

    except Exception as error:
        Logger.error("[HANDLER][MODERATOR][BAN WORDS][CHECK] DB error isWordInList -> " + str(error))


def getBanWords(ctx):
    # Get all the words in the database for the server
    requestFormat = """
        SELECT word
        FROM addon_moderator_banwords
        WHERE serverID = %s
    """
    requestSettings = (ctx.guild.id,)

    try:
        if debug == True:
            Logger.debug("[HANDLER][MODERATOR][BAN WORDS][GET] Getting all the words in the database for the server -> " + str(ctx.guild.id))

        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)

        return result

    except Exception as error:
        Logger.error("[HANDLER][MODERATOR][BAN WORDS][GET] DB error getBanWords -> " + str(error))


def getBanWordsAutoComplete(ctx):
    # Get all the words in the database for the server
    requestFormat = """
        SELECT word
        FROM addon_moderator_banwords
        WHERE serverID = %s
    """
    requestSettings = (ctx.interaction.guild_id,)

    try:
        if debug == True:
            Logger.debug("[HANDLER][MODERATOR][BAN WORDS][GET] Getting all the words in the database for the server -> " + str(ctx.interaction.guild_id))

        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)

        return result

    except Exception as error:
        Logger.error("[HANDLER][MODERATOR][BAN WORDS][GET] DB error getBanWordsAutoComplete -> " + str(error))


def banWordsAdd(ctx, word):
    # Add a word to the ban words list
    requestFormat = """
        INSERT INTO addon_moderator_banwords (serverID, word)
        VALUES (%s, %s)
    """
    requestSettings = (ctx.guild.id, word)

    try:
        if debug == True:
            Logger.debug("[HANDLER][MODERATOR][BAN WORDS][ADD] Adding a word to the ban words list -> " + str(word))

        serviceDatabase.makeRequest(requestFormat, requestSettings)

    except Exception as error:
        Logger.error("[HANDLER][MODERATOR][BAN WORDS][ADD] DB error banWordsAdd -> " + str(error))


def banWordsRemove(ctx, word):
    # Remove a word from the ban words list
    requestFormat = """
        DELETE FROM addon_moderator_banwords
        WHERE serverID = %s AND word = %s
    """
    requestSettings = (ctx.guild.id, word)

    try:
        if debug == True:
            Logger.debug("[HANDLER][MODERATOR][BAN WORDS][REMOVE] Removing a word from the ban words list -> " + str(word))

        serviceDatabase.makeRequest(requestFormat, requestSettings)

    except Exception as error:
        Logger.error("[HANDLER][MODERATOR][BAN WORDS][REMOVE] DB error banWordsRemove -> " + str(error))


