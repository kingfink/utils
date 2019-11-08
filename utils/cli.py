import click


@click.group()
def cli():
    pass


@click.command()
def dr():
    click.echo('Replacing dbt references...')  # TODO: default prod, optional dev


@click.command()
def fl():
    click.echo('Formatting list')  # TODO: default look to see if is number, otherwise quote, or specify


cli.add_command(dr)
cli.add_command(fl)
