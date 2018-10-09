import bibtexparser

def testparse(bibtex_file):
    with open(bibtex_file) as bibfile:
        database = bibtexparser.load(bibfile)
        
    return database.entries_dict

def main():
    d = testparse("surveys.bib")
    a = list(d.keys())
    article =d[a[0]]
    names = article['author']
    print(bibtexparser.customization.homogenize_latex_encoding(d[a[0]]))
    print(bibtexparser.customization.splitname(names))

    print(a[0])
    print(article['author'])

if __name__ == '__main__':
    main()