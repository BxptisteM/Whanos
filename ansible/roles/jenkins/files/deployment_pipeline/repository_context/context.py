from dataclasses import dataclass
from repository_context.language_enum import Language
from repository_context.detect import detect_language
from repository_context.detect import detect_standalone


@dataclass
class Context:
    standalone: bool = False
    language: Language | None = None


def get() -> Context:
    ctx = Context()
    ctx.language = detect_language()
    ctx.standalone = detect_standalone()
    return ctx
