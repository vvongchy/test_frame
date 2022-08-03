import pathlib
from string import Template


# TEMPLATE_PATH = pathlib.Path(__file__).parent.joinpath("template.txt")
# RESULT_PATH = pathlib.Path(__file__).parent.joinpath("a.py")
TEMPLATE_PATH = r"/TestCase\template\test_case.txt"
RESULT_PATH = r"/TestCase\template\ab.py"

def generate_txt():
    with open(r"../TestCase/template/a.py", mode="r", encoding="utf-8") as r_f:
        template_content = r_f.read()
        print(f"template_content:{template_content}")
        template = Template(template_content)
        data = template.substitute(NAME="TOM", GENDER="man", AGE=19)
    with open(RESULT_PATH, mode="w", encoding="utf8") as w_f:
        w_f.write(data)


if __name__ == "__main__":
    generate_txt()