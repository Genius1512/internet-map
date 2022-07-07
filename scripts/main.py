from argparse import ArgumentParser, Namespace as Args

from app import App


def parse_args(argv) -> Args:
    parser = ArgumentParser()

    parser.add_argument(
            "start_url",
            help="The URL to start from"
            )

    args = parser.parse_args(argv)
    return args


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    app = App(args=args)

    return 0


if __name__ == "__main__":
    from sys import exit, argv
    exit(main(argv[1:]))

