import os
import click
import questionary
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from typing import Dict, Any
from cfa.config import ProjectConfig

env = Environment(
    loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    autoescape=select_autoescape(),
    trim_blocks=True,
    lstrip_blocks=True
)

"""Create a new FastAPI application."""
@click.command()
@click.argument("project_dir", default=".")
def main(project_dir):
    project_dir = Path(project_dir).absolute()
    project_dir.mkdir(parents=True, exist_ok=True)

    # Get user options
    options = prompt_for_options()

    # Generate project structure
    generate_project(project_dir, options)

    click.echo(f"\n🎉Successfully created FastAPI project at {project_dir}")
    click.echo("\nRun the following commands to get started:")
    click.echo(f"`cd {project_dir}`")
    click.echo("`pip install -r requirements.txt`")
    click.echo("`uvicorn app.main:app --reload`")

"""Prompt for user configurations."""
def prompt_for_options() -> ProjectConfig:
    click.echo("\n🚀Let's create your FastAPI application!\n")

    questions = [
        {
            "type": "select",
            "name": "database",
            "message": "Choose your database(default: None):",
            "choices": [
                {"name": "None", "value": "none"},
                {"name": "PostgreSQL", "value": "postgresql"},
                {"name": "MySQL", "value": "mysql"},
                {"name": "MongoDB", "value": "mongodb"}
            ],
            "default": {"name": "None", "value": "none"},
        },
       {
            "type": "select",
            "name": "server",
            "message": "Choose your server(default: Uvicorn):",
            "choices": [
                {"name": "Uvicorn", "value": "uvicorn"},
                {"name": "Hypercorn", "value": "hypercorn"},
                {"name": "Gunicorn", "value": "gunicorn"}
            ],
            "default": {"name": "Uvicorn", "value": "uvicorn"},

        },
        {
            "type": "select",
            "name": "features",
            "message": "Select metrics(default: none):",
            "choices": [
                {"name": "None", "value": "none"},
                {"name": "Prometheus metrics", "value": "metrics"},
            ],
            "default": {"name": "None", "value": "none"},
        },
    ]

    answers = questionary.prompt(questions = questions)
    return ProjectConfig(
        database=answers["database"],
        server = answers["server"],
        features=answers["features"]
    )

"""Generate actual files"""
def generate_project(project_dir, options: ProjectConfig):
    # Generate Common files.
    render_template("common/app/main.py.j2", project_dir / "app/main.py", options)


"""Render Jinja2 templates."""
def render_template(template_path: str, destination_path, context: Any):
    templates = env.get_template(template_path)
    content = templates.render()

    destination_path.parent.mkdir(parents=True, exist_ok=True)
    destination_path.write_text(content)
    click.echo(f"Created: {destination_path.relative_to(Path.cwd())}")

