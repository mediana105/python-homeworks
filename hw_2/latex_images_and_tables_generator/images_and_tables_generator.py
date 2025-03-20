def generate_table(input_array):
    columns_number = len(input_array[0])
    table_rows = ''.join(
        " & ".join(map(str, row)) + "\\\\\n\\hline\n"
        for row in input_array
    )
    return f"""
\\begin{{tabular}}{{|{"c|" * columns_number}}}
\\hline
{table_rows}
\\end{{tabular}}"""


def generate_image(path, width=None):
    set_width = f"[width={width}]" if width else ""
    return f"""
\\begin{{figure}}[h]
\\begin{{center}}
\\includegraphics{set_width}{{{path}}}
\\end{{center}}
\\end{{figure}}"""
