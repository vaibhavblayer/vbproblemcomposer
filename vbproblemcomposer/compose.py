import click
from .choice_option import ChoiceOption
from .functions import extract_integer_from_filename, make_folder_with_basename, make_file_in_folder, run_subprocess_with_verbose


@click.command()
@click.option(
    '--filename',
    '-f',
    type=click.Path(exists=True),
    required=True,
    multiple=False,
    help='The filename of the problem'
)
@click.option(
    '--exam',
    '-e',
    cls=ChoiceOption,
    type=click.Choice(['JEE Advanced', 'JEE Main', 'NEET', 'Olympiad']),
    prompt=True,
    default=1,
    show_default=True,
    help='The exam of the problem',
)
@click.option(
    '--paper',
    '-p',
    cls=ChoiceOption,
    type=click.Choice(['I', 'II']),
    prompt=True,
    default=1,
    show_default=True,
    help='The paper of the problem',
)
@click.option(
    '--year',
    '-y',
    type=click.INT,
    prompt=True,
    help='The year of the problem',
)
def compose(filename, exam, paper, year):
    integer_part = extract_integer_from_filename(filename)
    folder_name = make_folder_with_basename(filename)
    make_file_in_folder(folder_name, exam, year, paper, integer_part)
    run_subprocess_with_verbose(folder_name)
