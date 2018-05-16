import click

class Config(object):

    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--verbose',is_flag=True)
@click.option('--home-directory', type=click.Path())
@pass_config
def cli(config, verbose, home_directory):

    config.verbose = verbose
    config.home_directory = home_directory


@cli.command()
@click.option('--string',default='World',help="Input Your Name")
@click.option('--repeat',default=1, help="Repat greeting times")
@click.argument('out', type=click.File('w'), default='-', required=False)
@pass_config
def say(config, string,repeat,out):
    """
        This script greeting for you
    """
    if config.verbose:
        click.echo("In Verbose mode")
    click.echo('Home Directory is {}'.format(config.home_directory))
    for x in range(repeat):
        click.echo(click.style('Hello {}'.format(string), fg='black',bg='white'),file=out)


    