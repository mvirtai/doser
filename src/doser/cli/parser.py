"""CLI parser for doser application."""

import argparse
from typing import Optional


def create_parser() -> argparse.ArgumentParser:
    """Create and return argparse parser"""


    # Parser definition
    parser = argparse.ArgumentParser(
        prog="doser",
        description="Doser - App for managing drug intake",
        epilog="Use 'doser <command> --help to see more precise instructions on each command"
    )

    # Subparsers definition
    subparsers = parser.add_subparsers(
        dest="command",
        help="Commands in use",
        metavar="<command>"
    )


    # Add-command
    add_parser = subparsers.add_parser(
        "add",
        description="Add a new drug into your druglist. Application will store it into its database.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        help="Add a new drug into your druglist. Application will store it into its database."
    )
    add_parser.add_argument(
        "drug",
        help="The name of the drug to add."
    )


    # List-command
    list_parser = subparsers.add_parser(
        "list",
        help="List all drugs in your druglist.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="List all drugs in your druglist."
    )

    return parser


def parse_args(args: Optional[list] = None) -> argparse.Namespace:
    """Does parse the given arguments."""

    parser = create_parser()
    return parser.parse_args(args)

