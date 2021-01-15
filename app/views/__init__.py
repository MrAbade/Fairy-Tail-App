from flask import Flask


def config_views(app: Flask):
    from .sorcerer_view import bp_sorcerer
    app.register_blueprint(bp_sorcerer, url_prefix='/sorcerer')
    
