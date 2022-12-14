from pathlib import Path

# Application
BASE_DIR = Path(__file__).parent

# Logging
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
LOG_DT_FORMAT = "%d.%m.%Y %H:%M:%S"

# Files
DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S"

# URLs
MAIN_DOC_URL = "https://docs.python.org/3/"
MAIN_PEPS_URL = "https://peps.python.org/"

#
EXPECTED_STATUS = {
    "A": ("Active", "Accepted"),
    "D": ("Deferred",),
    "F": ("Final",),
    "P": ("Provisional",),
    "R": ("Rejected",),
    "S": ("Superseded",),
    "W": ("Withdrawn",),
    "": ("Draft", "Active"),
}
