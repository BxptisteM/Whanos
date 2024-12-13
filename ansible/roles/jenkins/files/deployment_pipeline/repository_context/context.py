from dataclasses import dataclass
from repository_context.language_enum import Language
from repository_context.detect import (
    detect_language,
    detect_standalone,
    detect_deployable,
)
from repository_context.deployment_props import DeploymentProps, parse_deployment_props
from typing import Optional


@dataclass
class Context:
    standalone: bool = False
    language: Language | None = None
    deployable: bool = False
    project_name: str = "whanos"
    deployment_props: Optional[DeploymentProps] = None


def get(project_name: str) -> Context:
    ctx = Context()
    ctx.language = detect_language()
    ctx.standalone = detect_standalone()
    ctx.deployable = detect_deployable()
    ctx.project_name = project_name
    if ctx.deployable:
        ctx.deployment_props = parse_deployment_props()
    return ctx
