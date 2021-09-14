import pytest
from conftest import client

def test_sanity(client):
	assert client != None