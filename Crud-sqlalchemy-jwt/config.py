class config:
    SQLALCHEMY_DATABASE_URI= "mysql+pymysql://root:@localhost/auth-db"
    
    SQLALCHEMY_TRACK_MODIFICATION = False
    
    JWT_SECRET_KEY = "my_super_secret_key"