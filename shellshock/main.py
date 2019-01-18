import argparse
from shellshock.convert import convert_source


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file",
        help="The Python script to convert to a shell script",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        help="The filename to write the output to. Writes to stdout if omitted",  # noqa: E501
    )
    parser.add_argument(
        "-s",
        "--include_source",
        help="Include the original Python source alongside the resulting shell code as a comment. Helpful for debugging",  # noqa: E501
        action="store_true",
    )
    parser.add_argument(
        "-e",
        "--allow_errors",
        help="Allow parse errors and output the errors as comments in the shell script",  # noqa: E501
        action="store_true",
    )
    args = parser.parse_args()
    result = convert_source(
        args.input_file,
        include_source=args.include_source,
        allow_errors=args.allow_errors,
    )

    if args.output_file:
        with open(args.output_file, 'w') as out:
            out.write(result)
    else:
        print(result)


if __name__ == '__main__':
    main()
