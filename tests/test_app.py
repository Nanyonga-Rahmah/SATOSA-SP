"""Tests for the SP Flask application."""


def test_home_page_loads(client) -> None:
    """The home page should return HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_metadata_returns_xml(client) -> None:
    """The metadata endpoint should return valid-looking XML."""
    response = client.get("/metadata")
    assert response.status_code == 200
    assert response.content_type == "application/xml"
    assert b"EntityDescriptor" in response.data


def test_acs_without_saml_response_returns_400(client) -> None:
    """POSTing to /acs with no SAMLResponse should fail cleanly."""
    response = client.post("/acs", data={})
    assert response.status_code == 400


def test_login_redirects(client) -> None:
    """The login route should redirect to the IdP's SSO endpoint."""
    response = client.get("/login")
    assert response.status_code == 302
    assert "localhost:8080" in response.headers["Location"]
