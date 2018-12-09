from connexion import App


def create_app():
    connexion_app = App(
        'demo', specification_dir='swagger/', options={"swagger_ui": False}
    )
    connexion_app.add_api(
        'api.spec.yaml', validate_responses=True, strict_validation=True
    )
    return connexion_app
