import click
import utils


@click.group()
def cli():
    pass


@click.command()
@click.option('--schema', default='analytics_prod', help='Database schema to use')
def dbt(schema):
    utils.replace_model_references(schema)
    click.echo('Replaced model references!')  # TODO: default prod, optional dev


@click.command()
@click.option('--data_type', default=None, help='Type of items in the list, number or string. If None guess')
@click.option('--header_rows', default=0, help='Number of header rows, default to 0')
def lst(data_type, header_rows):
    utils.format_list(data_type, header_rows)
    click.echo('Formatted list!')  # TODO: default look to see if is number, otherwise quote, or specify


cli.add_command(dbt)
cli.add_command(lst)
