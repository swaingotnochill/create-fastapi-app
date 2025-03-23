from dataclasses import dataclass
from typing import List, Literal, Optional

DatabaseType = Literal["none", "postgresql", "mysql", "mongodb"]
ServerType = Literal["uvicorn", "hypercorn", "gunicorn"]
FeatureType = Literal["metrics", "docker", "logging", "deployment"]


@dataclass
class ProjectConfig:
    database: DatabaseType
    server: ServerType
    features: FeatureType