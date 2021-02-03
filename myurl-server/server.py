from app import app
from database import db
from routes.index import route as index

# Fetch the app and db instance
app = app()
db = db()

# Register the routes
app.register_blueprint(index)

if __name__ == '__main__':
	db.create_all()
	app.run();
