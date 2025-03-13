import click


def print_lines(file):
    last_line = None
    for i, line in enumerate(file, start=1):
        click.echo(f"{i:6}  {line}", nl=False)
        last_line = line
    if last_line and not last_line.endswith('\n'):
        click.echo()


@click.command()
@click.argument('file_path', type=click.Path(), required=False)
def simple_nl(file_path):
    """
    A simplified version of the `nl` utility.

    Args:
        file_path (Path or None): The path to the file to process. If not provided, reads from `stdin`.

    Returns:
        None: The function outputs directly to `stdout`.

    Behavior:
        - If a file is provided:
            Reads the file and outputs each line with a line number.
        - If no file is provided:
            Reads from `stdin` and outputs each line with a line number starting from 1.
    """
    if file_path is not None:
        try:
            with open(file_path, mode='r') as f:
                print_lines(f)
        except OSError as e:
            click.echo(f"nl: {file_path}: {e.strerror}")
    else:
        stdin = click.get_text_stream("stdin")
        print_lines(stdin)


if __name__ == '__main__':
    simple_nl()
