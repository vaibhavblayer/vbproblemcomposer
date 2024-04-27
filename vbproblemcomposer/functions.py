import os
import subprocess


def extract_integer_from_filename(filename):
    base = os.path.basename(filename)
    name, ext = os.path.splitext(base)
    integer_part = name.split("_")[-1]
    try:
        return int(integer_part)
    except ValueError:
        return None


def make_folder_with_basename(filename):
    base = os.path.basename(filename)
    name, ext = os.path.splitext(base)
    folder_name = os.path.dirname(filename) + r"./" + r"problems" + r"/" + name
    print(folder_name)
    os.makedirs(folder_name, exist_ok=True)
    return folder_name


def make_file_in_folder(folder_name, exam, year, paper, n):
    file_name = folder_name + "/main.tex"
    with open(file_name, "w") as file:
        file.write(r"\documentclass{article}" + "\n")
        file.write(r"\usepackage{v-test-paper}" + "\n")
        file.write(
            r"\newenvironment{solution}{\par\noindent\color{red!85!black}$\Rightarrow$\vspace{0em}}{}" + "\n")
        if exam == "JEE Advanced":
            file.write(r"\title{\large\textsc{" + f"{exam} " + f"{year} " +
                       r"Paper-" + f"{paper}" + r"\\Physics}}" + "\n")
        else:
            file.write(r"\title{\large\textsc{" + f"{exam} " +
                       f"{year} " + r"\\Physics}}" + "\n")
        file.write(r"\begin{document}" + "\n")
        file.write(r"\maketitle" + "\n")
        file.write(
            r"\begin{enumerate}\setcounter{enumi}{" + f"{n-1}" + r"}" + "\n")
        file.write(r"\input{../../" + f"problem_{n}.tex" + r"}" + "\n")
        file.write(r"\end{enumerate}" + "\n")
        file.write(r"\end{document}")


def run_subprocess_with_verbose(folder_name):
    subprocess.call(["pdflatex", "-interaction=nonstopmode",
                    "-file-line-error", "-halt-on-error", "main.tex"], cwd=folder_name)
