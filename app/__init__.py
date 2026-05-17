from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register blueprints
    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app.routes.shop import shop as shop_blueprint
    app.register_blueprint(shop_blueprint, url_prefix='/shop')

    from app.routes.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    # Seed system defaults on first request
    @app.before_request
    def seed_system_data():
        """Run once — seed default order statuses, then remove this hook."""
        app.before_request_funcs[None].remove(seed_system_data)
        try:
            from app.models.order import OrderStatus
            OrderStatus.seed_defaults(db.session)
        except Exception:
            pass  # Table might not exist yet during migrations

    return app
