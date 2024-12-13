from dataclasses import dataclass, field
from typing import Dict, List
from typing import Optional
import yaml

FILE_PATH = "whanos.yml"


@dataclass
class DeploymentProps:
    replicas: int = 1
    resources: Dict[str, Dict[str, str]] = field(default_factory=dict)
    ports: List[int] = field(default_factory=list)


def parse_deployment_props() -> Optional[DeploymentProps]:
    try:
        with open(FILE_PATH, "r") as file:
            config = yaml.safe_load(file)

        if not isinstance(config, dict) or "deployment" not in config:
            print(f"Error: Invalid whanos.yml structure in {FILE_PATH}")
            return None

        deployment = config.get("deployment", {})

        whanos_deploy = DeploymentProps()

        if "replicas" in deployment:
            replicas = deployment["replicas"]
            if not isinstance(replicas, int) or replicas < 1:
                print(f"Warning: Invalid replicas value {replicas}. Defaulting to 1.")
                whanos_deploy.replicas = 1
            else:
                whanos_deploy.replicas = replicas

        if "resources" in deployment:
            resources = deployment["resources"]
            if isinstance(resources, dict):
                whanos_deploy.resources = resources
            else:
                print("Warning: Resources must be a dictionary. Skipping.")

        if "ports" in deployment:
            ports = deployment["ports"]
            if isinstance(ports, list) and all(isinstance(p, int) for p in ports):
                whanos_deploy.ports = ports
            else:
                print("Warning: Ports must be a list of integers. Skipping.")

        return whanos_deploy

    except FileNotFoundError:
        print(f"Error: File not found - {FILE_PATH}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error parsing whanos.yml: {e}")
        return None
