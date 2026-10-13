from flask_shop import create_app,db
from flask_migrate import Migrate




app = create_app('development')


Migrate(app, db)


if __name__ == "__main__":
    app.run()