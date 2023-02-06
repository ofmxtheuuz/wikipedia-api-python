import wikipediaapi

def get_wikipedia_summary(keyword):
    wiki_wiki = wikipediaapi.Wikipedia(
        language='pt',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    page = wiki_wiki.page(keyword)

    if page.exists():
        return page.summary[0:1024] + "..."
    else:
        return "Não foi possível encontrar informações sobre '{}' na Wikipedia.".format(keyword)


keyword = input("Digite o que você quer pesquisar na Wikipedia: ")
print(get_wikipedia_summary(keyword))
