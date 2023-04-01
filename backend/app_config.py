from constants import DB_USER, DB_NAME, DB_PORT, DB_PASSWORD


# class ProductionConfig:
#     FLASK_ENV = 'prod'
#     DEBUG = False
#     TESTING = False
#     SQLALCHEMY_DATABASE_URI = (
#         f'postgresql://{DB_USER}:{DB_PASSWORD}'
#         f'@localhost:{DB_PORT}/{DB_NAME}'
#     )


class DevelopmentConfig:
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_USER}:{DB_PASSWORD}'
        f'@localhost:{DB_PORT}/{DB_NAME}'
    )
