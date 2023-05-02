import services.serviceDatabase as serviceDatabase

# Create the database if it does not exist
def databaseInit():
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

