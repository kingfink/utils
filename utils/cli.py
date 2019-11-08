import click


@click.group()
def cli():
    pass


@click.command()
@click.option('--schema', default='analytics_prod', help='Database schema to use')
def dr():
    click.echo('Replaced dbt references!')  # TODO: default prod, optional dev


@click.command()
@click.option('--type', default=None, help='Type of items in the list, number or string. If None guess')
def fl():
    click.echo('Formatted list!')  # TODO: default look to see if is number, otherwise quote, or specify


cli.add_command(dr)
cli.add_command(fl)
