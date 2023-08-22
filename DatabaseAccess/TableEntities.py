from DatabaseAccess.Repository    import    Repository

class PasswordEntity:
    Table = "Password"
    def __init__(self):
        self.ID = None
        self.Password = None

class PasswordRepo(Repository):
    def __init__(self, databasePath = "Database/Database"):
        Repository.__init__(self, PasswordEntity, databasePath)

class FaceFeatureEntity:
    Table = "FaceFeature"
    def __init__(self):
        self.ID = None
        self.FaceFeature = None

class FaceFeatureEntity(Repository):
    def __init__(self, databasePath = "Database/Database"):
        Repository.__init__(self, PasswordEntity, databasePath)