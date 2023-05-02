# Github informations
enableGithub = True
author = "Ted-18"
repository = "Bot.Assistant-Moderator"
version = "1.0.2" 

# To activate this addon
cogEnabled = True

# Name of the addon
cogName = "moderator"

# Name of the file containing the cog
cogFile = "cogModerator"

# List of packages required by the addon
packageDependencies = [
    "py-cord",
    "mysql-connector-python",
    "prettytable"
]

# List of addons required by the addon
addonDependencies = [
    "Configuration"
]

# List of permissions required by the addon
addonPermissions = [
    "manage_roles",
    "send_messages",
    "manage_messages"
]

commandPermissions = {
    # Permission to check the addon's permissions
    "cmdRequirements" : "discord.permission.manage_guild",


    # Add a word to the BanWords list
    "cmdBanWordAdd" : "moderator.banword.add",

    # Remove a word from the BanWords list
    "cmdBanWordRemove" : "moderator.banword.remove",

    # List the words in the BanWords list
    "cmdBanWordList" : "moderator.banword.list",


    # Block all discord invites
    "cmdInviteShield" : "moderator.inviteshield"

}