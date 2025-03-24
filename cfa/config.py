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

    def to_dict(self) -> dict:
        return {
            "database": self.database,
            "server": self.server,
            "has_metrics": "metrics" in self.features
        }
