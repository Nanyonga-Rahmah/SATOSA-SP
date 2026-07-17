from pathlib import Path

from saml2.config import Config
from saml2.metadata import create_metadata_string

from .config import CONFIG

_PROJECT_ROOT: Path = Path(__file__).resolve().parents[0]

metadata = create_metadata_string(
    None,
    config=Config().load(CONFIG),
)

with open(str(_PROJECT_ROOT / "metadata" / "sp-metadata.xml"), "wb") as f:
    f.write(metadata)

print("Metadata generated.")
