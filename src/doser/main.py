from doser.cli.parser import create_parser, parse_args
from loguru import logger
import sys

def main():
    logger.info("Starting doser...")

    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Ohjataan komennot oikeisiin moduuleihin
    if args.command == "add":
        from doser.cli.commands.add import handle_add
        handle_add(args)
    if args.command == "list":
        logger.info("Listing...")


if __name__ == "__main__":
    main()
