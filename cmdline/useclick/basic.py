import click

@click.command()
@click.option('--string',default='World',help="Input Your Name")
@click.option('--repeat',default=1, help="Repat greeting times")
@click.argument('out', type=click.File('w'), default='-', required=False)
def cli(string,repeat,out):
    """
        This script greeting for you
    """
    for x in range(repeat):
        click.echo(click.style('Hello {}'.format(string), fg='black',bg='white'),file=out)

if __name__ == '__main__':
    cli()