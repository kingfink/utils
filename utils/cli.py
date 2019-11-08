import click
import utils


@click.group()
def cli():
    """Utilities for working with SQL, dbt, and possibly other stuff in the future"""
    pass


@click.command()
@click.option('--schema', default='analytics_prod', type=str, help='Database schema to use')
def dbt(schema):
    """Replace model references (in dbt) from Jinja to a specific schema"""
    utils.replace_model_references(schema)
    click.echo('Replaced model references!')  # TODO: default prod, optional dev


@click.command()
@click.option('--data_type', default=None, type=click.Choice(['number', 'string', None]), help='Type of items in the list. If None guess')
@click.option('--header_rows', default=0, type=click.IntRange(min=0), help='Number of header rows, default to 0')
def lst(data_type, header_rows):
    """Format lists for easy insertion into a SQL query"""
    utils.format_list(data_type, header_rows)
    click.echo('Formatted list!')  # TODO: default look to see if is number, otherwise quote, or specify


cli.add_command(dbt)
cli.add_command(lst)
