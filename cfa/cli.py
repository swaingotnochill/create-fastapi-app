import os
import click
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    autoescape=select_autoescape(),
    trim_blocks=True,
    lstrip_blocks=True
)

@click.command()
@click.argument("project_dir", default=".")
def main(project_dir):
    """Create a new FastAPI application"""
    project_dir = Path(project_dir).absolute()
    project_dir.mkdir(parents=True, exist_ok=True)

    # Get user options
    options = prompt_for_options()

    # Generate project structure
    generate_project(project_dir, options)

    click.echo(f"\n 🎉Successfully created FastAPI project at {project_dir}")
    click.echo("\nRun the following commands to get started:")
    click.echo(f"`cd {project_dir}`")
    click.echo("`pip install -r requirements.txt`")
    click.echo("`uvicorn app.main:app --reload`")


def prompt_for_options():
    pass

def generate_project(project_dir, options):
    pass