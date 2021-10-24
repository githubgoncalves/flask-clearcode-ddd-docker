from flask import Blueprint, jsonify,Response, json, request,current_app
from api.domain.decorators.authenticator_jwt.auth_jwt import token_creator, token_verify
from api.infra.config import create_database

from api.main.composer import (
    register_user_composer,
    consulta_api_composer,
)

from api.main.adapter import flask_adapter

from healthcheck import HealthCheck

api_routes_bp = Blueprint("api_routes", __name__)

def api_check():
    """ Monitoramento de micro-serviços - healthcheck """
    current_app.logger.info("HealthCheck")
    return True, "API DISPONÍVEL"

health = HealthCheck()
health.add_check(api_check)
api_routes_bp.add_url_rule("/healthcheck", view_func=lambda: health.run())


@api_routes_bp.route("/api/create_data_base", methods=["GET"])
def create_data_base():
    """ Criar Base de Dados"""
    current_app.logger.info("criar base de dados")
    create_database.CreateDataBase()


@api_routes_bp.route("/api/consulta-api", methods=["GET"])
@token_verify
def consulta_api(token):
    """ register user route """

    current_app.logger.info("consulta api")

    message = {}

    response = flask_adapter(request=request, api_route=consulta_api_composer())

    if response.status_code < 300:
        message = response.body

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/create_user", methods=["POST"])
def register_user():
    """ register user route """

    current_app.logger.info("registrar usuario")

    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())

    if response.status_code < 300:
        message = {
            "type": "users",
            "id": response.body.id,
            "attributest": {"name": response.body.name},
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/login", methods=["POST"])
def login():
    """ IMPLEMENTAR """


@api_routes_bp.route("/api/secret", methods=["GET"])
@token_verify
def secret_route(token):
    """ Devemos chegar aqui """

    current_app.logger.info("teste validação token")

    return jsonify({
        'data': 'Mensagem secreta',
        'token': token
    }), 200


@api_routes_bp.route("/api/auth", methods=["POST"])
def authorization_route():
    """ auth """

    current_app.logger.info("auth")

    token = token_creator.create(uid=12)
    return jsonify({
        'token': token
    }), 200
