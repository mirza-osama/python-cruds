class Config:
    # XAMPP default: localhost, port 3306
    # Format: mysql+pymysql://username:password@host/database_name
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/studentdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False