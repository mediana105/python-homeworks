import click


def print_last_lines(file, lines):
    last_line = None
    last_lines = file.readlines()[-lines:]
    for line in last_lines:
        click.echo(line, nl=False)
        last_line = line
    if last_line and not last_line.endswith('\n'):
        click.echo()


def process_file(file_path, print_name_flag):
    try:
        with open(file_path, mode='r') as f:
            if print_name_flag:
                click.echo(f"==> {file_path} <==")
            print_last_lines(f, 10)
    except OSError as e:
        click.echo(f"tail: {file_path}: {e.strerror}")


def process_stdin():
    stdin = click.get_text_stream("stdin")
    print_last_lines(stdin, 17)


@click.command()
@click.argument('file_paths', type=click.Path(), required=False, nargs=-1)
def simple_tail(file_paths):
    """
    A simplified version of the `tail` utility.

    Args:
        file_paths (list of Path or None): A list of file paths to process. If empty, reads from `stdin`.

    Returns:
        None: The function outputs directly to `stdout`.

    Behavior:
        - For each file:
            1. If multiple files are provided, prints the file name before its content.
            2. Outputs the last 10 lines of the file.
        - If no files are provided:
            Reads from `stdin` and outputs the last 17 lines.
    """
    if file_paths:
        print_name_flag = len(file_paths) > 1
        for file_path in file_paths:
            process_file(file_path, print_name_flag)
    else:
        process_stdin()


if __name__ == '__main__':
    simple_tail()
