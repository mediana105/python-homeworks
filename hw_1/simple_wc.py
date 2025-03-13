import click


def get_one_file_stat(file):
    file_content = file.read()
    lines_count = len(file_content.splitlines('\n'))
    words_count = len(file_content.split())
    bytes_count = len(file_content)
    return lines_count, words_count, bytes_count


def process_file(file_path):
    try:
        with open(file_path, mode='rb') as f:
            lines_count, words_count, bytes_count = get_one_file_stat(f)
            click.echo(f"{lines_count} {words_count} {bytes_count} {file_path}")
            return lines_count, words_count, bytes_count
    except (IsADirectoryError, OSError) as e:
        click.echo(f"wc: {file_path}: {e.strerror}")
        if isinstance(e, IsADirectoryError):
            click.echo(f"0 0 0 {file_path}")  # original wc util returns 0, 0, 0 for paths
        return 0, 0, 0


def process_stdin():
    stdin = click.get_text_stream("stdin")
    lines, words, bytes_count = get_one_file_stat(stdin)
    click.echo(f"{lines} {words} {bytes_count}")


@click.command()
@click.argument('file_paths', type=click.Path(), required=False, nargs=-1)
def simple_wc(file_paths=None):
    """
        A simplified version of the `wc` utility.

        Args:
            file_paths (list of Path or None): A list of file paths to process. If empty, reads from `stdin`.

        Returns:
            None: The function outputs directly to `stdout`.

        Behavior:
            - For each file:
                1. Counts the number of lines, words, and bytes in the file.
                2. Outputs the statistics (three numbers) with the file name.
            - If multiple files are provided:
                After processing all files, outputs the total statistics (three numbers) with the label "total".
            - If no files are provided:
                Reads from `stdin` and outputs the statistics (three numbers).
    """
    if file_paths:
        total_lines, total_words, total_bytes = 0, 0, 0
        total_stat_flag = len(file_paths) > 1
        for file_path in file_paths:
            lines_count, words_count, bytes_count = process_file(file_path)
            total_lines += lines_count
            total_words += words_count
            total_bytes += bytes_count
        if total_stat_flag:
            click.echo(f"{total_lines} {total_words} {total_bytes} total")
    else:
        process_stdin()


if __name__ == '__main__':
    simple_wc()
