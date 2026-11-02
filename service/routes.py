"""
Account Service REST API
"""
from flask import jsonify, request, make_response, abort, url_for
from service.models import Account, DataValidationError
from service.common import status
from . import app


@app.route("/health")
def health():
    """Health Status"""
    return jsonify(status="OK"), status.HTTP_200_OK


@app.route("/")
def index():
    """Root URL response"""
    return jsonify(name="Account REST API Service", version="1.0"), status.HTTP_200_OK


@app.route("/accounts", methods=["POST"])
def create_accounts():
    """Create an account"""
    check_content_type("application/json")
    account = Account()
    try:
        account.deserialize(request.get_json())
        account.create()
    except DataValidationError as error:
        abort(status.HTTP_400_BAD_REQUEST, str(error))

    location_url = url_for("get_account", account_id=account.id, _external=True)
    return make_response(
        jsonify(account.serialize()),
        status.HTTP_201_CREATED,
        {"Location": location_url},
    )


@app.route("/accounts", methods=["GET"])
def list_accounts():
    """List all accounts"""
    accounts = Account.all()
    results = [account.serialize() for account in accounts]
    return jsonify(results), status.HTTP_200_OK


@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):
    """Read an account"""
    account = Account.find(account_id)
    if not account:
        abort(status.HTTP_404_NOT_FOUND, f"Account {account_id} was not found")
    return jsonify(account.serialize()), status.HTTP_200_OK


@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    """Update an account"""
    check_content_type("application/json")
    account = Account.find(account_id)
    if not account:
        abort(status.HTTP_404_NOT_FOUND, f"Account {account_id} was not found")

    try:
        account.deserialize(request.get_json())
        account.update()
    except DataValidationError as error:
        abort(status.HTTP_400_BAD_REQUEST, str(error))

    return jsonify(account.serialize()), status.HTTP_200_OK


@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    """Delete an account"""
    account = Account.find(account_id)
    if not account:
        abort(status.HTTP_404_NOT_FOUND, f"Account {account_id} was not found")

    account.delete()
    return "", status.HTTP_204_NO_CONTENT


def check_content_type(media_type):
    """Check request content type"""
    content_type = request.headers.get("Content-Type")
    if content_type and content_type == media_type:
        return

    abort(
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        f"Content-Type must be {media_type}",
    )
