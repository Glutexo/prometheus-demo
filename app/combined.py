from connexion import App
from prometheus_client import make_wsgi_app
from werkzeug.wsgi import DispatcherMiddleware


def create_app():
    connexion_app = App(
        'demo', specification_dir='swagger/', options={"swagger_ui": False}
    )
    connexion_app.add_api(
        'api.spec.yaml', validate_responses=True, strict_validation=True
    )

    prometheus_app = make_wsgi_app()
    dispatcher = DispatcherMiddleware(connexion_app, {"/metrics": prometheus_app})

    return dispatcher
