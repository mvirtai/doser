"""Handler for 'doser add' command"""

import argparse
from ast import arg
from typing import Optional
from loguru import logger
from rich.console import Console
from rich.prompt import Prompt


def handle_add(args: argparse.Namespace) -> None:
    console = Console()
    drug_name = args.drug

    if drug_name:
        logger.info(f"Adding: {drug_name}")
        



if __name__ == "__main__":
    # Testing 
    import argparse
    args = argparse.Namespace(drug="Melatonin")
    handle_add(args)