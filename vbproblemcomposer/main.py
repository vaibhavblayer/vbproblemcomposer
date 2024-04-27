import click
from .compose import compose

CONTEXT_SETTINGS = dict(
    help_option_names=[
        '-h',
        '--help'
    ]
)


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass


main.add_command(compose)
