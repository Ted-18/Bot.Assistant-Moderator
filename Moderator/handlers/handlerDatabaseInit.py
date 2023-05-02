import services.serviceDatabase as serviceDatabase
import settings.settingBot as settingBot

# Create the database if it does not exist
def databaseInit():
    if settingBot.databaseType == "MariaDB":
        # Table structure
        tableName = "addon_moderator_banwords"
        columns = [
            ["serverID", "BIGINT NOT NULL"],
            ["word", "VARCHAR(255) NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)

        # Table structure
        tableName = "addon_moderator_inviteshield"
        columns = [
            ["serverID", "BIGINT NOT NULL"],
            ["status", "BOOLEAN DEFAULT 0"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)


    elif settingBot.databaseType == "SQLite":
        # Table structure
        tableName = "addon_moderator_banwords"
        columns = [
            ["serverID", "integer NOT NULL"],
            ["word", "text NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)

        # Table structure
        tableName = "addon_moderator_inviteshield"
        columns = [
            ["serverID", "integer NOT NULL"],
            ["status", "integer DEFAULT 0"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)
