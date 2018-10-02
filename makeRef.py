import sys
import re
import subprocess

def makecite(filename):
    get_cite_key = r'@[a-z]+{.*?,'
    to_cite_command = r'@[a-z]+'
    with open(filename) as f:
        database = f.read()
        raw_citelist = re.findall(get_cite_key,database)
        get_ref = lambda s: re.sub(to_cite_command,"\cite",s).replace(',','}')
        data = list(map(get_ref,raw_citelist))

    return data

def make_tex(filename):
    style = "alpha"
    header = [r"\documentclass [a4,11pt] {article}", r"\usepackage [top=1.5cm,right=2cm,bottom=1.5cm, left=2cm,] {geometry}", r"\pagestyle {empty}",r"\title {References from Bibtex}", r"\begin {document}", r"\maketitle"]
    fooder = [r"\bibliographystyle {"+ style +r"}", r"\bibliography {"+ filename + r"}", r"\end{document}"]

    with open("tmp.tex",mode="w") as f:
        cites = makecite(filename)
        f.write('\n'.join(header))
        f.write("\n")
        f.writelines(cites)
        f.write("\n")
        f.write('\n'.join(fooder))
        f.write("\n")

make_tex(sys.argv[1])

