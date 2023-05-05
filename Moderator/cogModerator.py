# ADDON IMPORTS
import addons.Moderator.init as init

import addons.Moderator.functions.commands.commandRequirements as commandRequirements
import addons.Moderator.functions.commands.commandInviteShield as commandInviteShield
import addons.Moderator.functions.commands.commandBanWordsAdd as commandBanWordsAdd
import addons.Moderator.functions.commands.commandBanWordsRemove as commandBanWordsRemove
import addons.Moderator.functions.commands.commandBanWordsList as commandBanWordsList

import addons.Moderator.functions.events.eventInviteShield as eventInviteShield
import addons.Moderator.functions.events.eventBanWords as eventBanWords

import addons.Moderator.handlers.handlerDatabaseInit as handlerDatabaseInit
import addons.Moderator.handlers.handlerBanWords as handlerBanWords

# BOTASSISTANT IMPORTS
from services.serviceLogger import Logger
from services.serviceDiscordLogger import discordLogger as DiscordLogger
from settings.settingBot import debug

# INIT BOT VARIABLES
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()



class Moderator(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_message(self, message):
        await eventInviteShield.inviteShieldCheck(message)
        await eventBanWords.banWordsCheck(message)

    # AUTOCOMPLETE
    async def getBanWordsList(ctx: discord.AutocompleteContext):
        resultDatabase = handlerBanWords.getBanWordsAutoComplete(ctx)

        banWords = []

        for banWord in resultDatabase:
            banWords.append(banWord[0])

        return banWords


    groupModerator = discordCommands.SlashCommandGroup("moderator", "🔶 Group of commands to manage the Moderator addon.")
    groupeBanWords = groupModerator.create_subgroup("banwords", "🔶 Group of commands to manage the ban words list.")

    # Verify if the bot has the prerequisites permissions
    @groupModerator.command(name="requirements", description="Check the prerequisites permissions of the addon.")
    async def cmdPermissions(self, ctx: commands.Context):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the requirements command.", str(ctx.command))
        await commandRequirements.checkRequirements(ctx)
        

    # INVITE SHIELD
    @groupModerator.command(name="inviteshield", description="Enable or disable the invite shield.")
    async def cmdInviteShield(
        self, 
        ctx: commands.Context, 
        
        enabled: discord.Option(
            discord.SlashCommandOptionType.boolean,
            required=True,
            description="Enable or disable the invite shield."
        )
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the inviteshield command.", str(ctx.command))
        await commandInviteShield.inviteShield(ctx, enabled)

    

    
    # BAN WORDS ADD
    @groupeBanWords.command(name="add", description="Add a word to the ban words list.")
    async def cmdBanWordsAdd(
        self, 
        ctx: commands.Context, 
        
        word: discord.Option(
            discord.SlashCommandOptionType.string,
            required=True,
            description="The word to add to the ban words list."
        )
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the banword add command.", str(ctx.command))
        await commandBanWordsAdd.banWordsAdd(ctx, word)


    # BAN WORDS REMOVE
    @groupeBanWords.command(name="remove", description="Remove a word from the ban words list.")
    async def cmdBanWordsRemove(
        self,
        ctx: commands.Context,

        # Autocomplete
        word: discord.Option(
            discord.SlashCommandOptionType.string,
            required=True,
            description="The word to remove from the ban words list.",
            autocomplete=getBanWordsList
        )
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the banword remove command.", str(ctx.command))
        await commandBanWordsRemove.banWordsRemove(ctx, word)


    # BAN WORDS LIST
    @groupeBanWords.command(name="list", description="List all the words from the ban words list.")
    async def cmdBanWordsList(
        self,
        ctx: commands.Context
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the banword list command.", str(ctx.command))
        await commandBanWordsList.banWordsList(ctx)


def setup(bot):
    Logger.debug("Loading cog: " + init.cogName)
    handlerDatabaseInit.databaseInit()
    bot.add_cog(Moderator(bot))
    
    