import os
import tempfile
import pytest

from api.app import app

@pytest.fixture
def api():
    app.config['TESTING'] = True
    api = app.test_client()
    yield api

def test_valid_transaction(api):
    retorno = api.get("/api/consulta-api")    
    assert  retorno.get_json()