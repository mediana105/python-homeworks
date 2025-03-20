from latex_images_and_tables_generator import generate_table
from latex_images_and_tables_generator import generate_image


def generate_code(input_array, input_img):
    table_code = generate_table(input_array)
    img_code = generate_image(input_img)
    img_code_with_width = generate_image(input_img, width="0.5\\textwidth")
    return f"""\\documentclass{{article}}
\\usepackage{{graphicx}}
\\begin{{document}}
{table_code}
{img_code}
{img_code_with_width}
\\end{{document}}"""


def generate_tex_file():
    input_array = [
        ["Col1", "Col2", "Col2", "Col3"],
        ["1", "6", "87837", "787"],
        ["2", "7", "78", "5415"],
        ["3", "545", "778", "7507"],
        ["4", "545", "18744", "7560"],
        ["5", "88", "788", "6344"]
    ]
    input_img = "artifacts/task_2/images/example_image.png"
    latex_code = generate_code(input_array, input_img)
    with open("artifacts/task_2/main.tex", "w") as f:
        f.write(latex_code)


if __name__ == '__main__':
    generate_tex_file()
