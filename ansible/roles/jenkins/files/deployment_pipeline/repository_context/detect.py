from repository_context.language_enum import Language
from typing import Dict
from pathlib import Path

DETECTION_CRITERIAS: Dict[str, Language] = {
    "Makefile": Language.C,
    "app/pom.xml": Language.JAVA,
    "package.json": Language.JAVASCRIPT,
    "requirements.txt": Language.PYTHON,
    "app/main.bf": Language.BEFUNGE,
}


def detect_language() -> Language:
    for file, language in DETECTION_CRITERIAS.items():
        if Path(file).exists():
            return language
    raise Exception("Could not detect language")


def detect_standalone() -> bool:
    return not Path("Dockerfile").exists()


def detect_deployable() -> bool:
    return Path("whanos.yml").exists()
