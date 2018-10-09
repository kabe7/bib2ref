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

def make_tex(filename,style="alpha"):
    style = "harvard" # plain / unsrt / alpha / abbrv
    header = [
        r"\documentclass{article}",
        r"\usepackage [top=1.5cm,right=2cm,bottom=1.5cm, left=2cm,] {geometry}",
        r"\usepackage{doi}", 
        r"\pagestyle {empty}",
        r"\title {References from Bibtex}", 
        r"\begin {document}", 
        r"\maketitle"]
    fooder = [
        r"\bibliographystyle {"+ style +r"}", 
        r"\bibliography {"+ filename + r"}", 
        r"\end{document}"]

    with open("tmp.tex",mode="w") as f:
        cites = makecite(filename)
        f.write('\n'.join(header))
        f.write("\n")
        f.write(r"\nocite {*}")
        #f.writelines(cites)
        f.write("\n")
        f.write('\n'.join(fooder))
        f.write("\n")

make_tex(sys.argv[1])

styles = ['chembst',
 'aastex',
 'opcit',
 'ieeepes',
 'pnas2009',
 'datatool',
 'texsis',
 'urlbst',
 'IEEEtran',
 'seuthesis',
 'sapthesis',
 'thuthesis',
 'lion-msc',
 'resphilosophica',
 'przechlewski-book',
 'din1505',
 'confproc',
 'fcavtex',
 'jneurosci',
 'adrconv',
 'context',
 'stellenbosch',
 'aiaa',
 'elsarticle',
 'bibexport',
 'ametsoc',
 'hc',
 'inlinebib',
 'mciteplus',
 'langsci',
 'imac',
 'finbib',
 'revtex',
 'germbib',
 'amsrefs',
 'chet',
 'nar',
 'chicago',
 'lni',
 'multibibliography',
 'gost',
 'udesoftec',
 'frankenstein',
 'iopart-num',
 'cmpj',
 'economic',
 'mnras',
 'dinat',
 'persian-bib',
 'biblatex',
 'babelbib',
 'bath-bst',
 'nmbib',
 'aichej',
 'mslapa',
 'dk-bib',
 'tugboat',
 'bgteubner',
 'psu-thesis',
 'sort-by-letters',
 'bibhtml',
 'aguplus',
 'apacite',
 'nature',
 'shipunov',
 'cje',
 'aomart',
 'chscite',
 'ascelike',
 'directory',
 'bib-fr',
 'gbt7714',
 'tufte-latex',
 'dlfltxb',
 'swebib',
 'phfnote',
 'hithesis',
 'amscls',
 'acmart',
 'cell',
 'seuthesix',
 'gloss',
 'bookdb',
 'nddiss',
 'figbib',
 'abntex2',
 'sageep',
 'multibib',
 'besjournals',
 'vancouver',
 'natbib',
 'cascadilla',
 'francais-bst',
 'chicago-annote',
 'uestcthesis',
 'beebe',
 'ijqc',
 'abstyles',
 'unamthesis',
 'jurarsp',
 'savetrees',
 'kluwer',
 'index',
 'chem-journal',
 'asaetr',
 'afthesis',
 'apalike-german',
 'gustlib',
 'notex-bst',
 'ijmart',
 'jurabib',
 'revtex4',
 'rsc',
 'fbs',
 'gatech-thesis',
 'perception',
 'cnbwp',
 'dvdcoll',
 'munich',
 'achemso',
 'bestpapers',
 'cquthesis',
 'apalike2',
 'computational-complexity',
 'adfathesis',
 'ksfh_nat',
 'listbib',
 'spie',
 'ajl',
 'base',
 'upmethodology',
 'beilstein',
 'harvard',
 'hustthesis',
 'biolett-bst',
 'vak']
