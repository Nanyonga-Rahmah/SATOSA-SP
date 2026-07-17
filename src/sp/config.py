from pathlib import Path

from saml2 import BINDING_HTTP_POST

_PROJECT_ROOT: Path = Path(__file__).resolve().parents[0]


CONFIG: dict[str, object] = {
    "entityid": "http://localhost:8000/metadata",
    "service": {
        "sp": {
            "endpoints": {
                "assertion_consumer_service": [
                    (
                        "http://localhost:8000/acs",
                        BINDING_HTTP_POST,
                    )
                ]
            },
            "allow_unsolicited": True,
            "want_assertions_signed": True,
            "authn_requests_signed": False,
        }
    },
    "key_file": str(_PROJECT_ROOT / "certs" / "sp.key"),
    "cert_file": str(_PROJECT_ROOT / "certs" / "sp.crt"),
    "metadata": {
        "local": [
            str(_PROJECT_ROOT / "metadata" / "satosa-metadata.xml"),
        ]
    },
    "debug": 1,
}
