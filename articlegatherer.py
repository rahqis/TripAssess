from newsapi.newsapi_client import NewsApiClient

newsapi1 = NewsApiClient(api_key="2175ec159de245a187f73f5f2bad6de5")

# Finds top articles of destination alone
def collectTopArticles(destination):
    topArticles = newsapi1.get_top_headlines(q=destination, language="en")
    topArts = topArticles["articles"]
    return topArts


# Finds articles on source and destination countries and their relations
def collectNationsRelationships(source, destination):
    Relations = source + " " + destination + " relations"
    relationsArticles = newsapi1.get_top_headlines(q=Relations, language="en")
    relArts = relationsArticles["articles"]
    return relArts


# Finds all articles on destination
def collectAllArticles(destination):
    allArticles = newsapi1.get_everything(
        q=destination, sort_by="relevancy", language="en"
    )
    allArts = allArticles["articles"]
    return allArts


# Collects all string contents of every title, content, and description of all articles found
def gatherAllArticleDescriptions(allArticles):
    allDescriptions = ""
    for source in allArticles:
        if type(source["title"]) == str:
            allDescriptions += source["title"]
        if type(source["content"]) == str:
            allDescriptions += source["content"]
        if type(source["description"]) == str:
            allDescriptions += source["description"]
    return allDescriptions


# Collects all string contents of every title, content, and description of all country relation articles found
def gatherRelationArticleDescriptions(relationsArticles):
    relationsDescriptions = ""
    for source in relationsArticles:
        if type(source["title"]) == str:
            relationsDescriptions += source["title"]
        if type(source["content"]) == str:
            relationsDescriptions += source["content"]
        if type(source["description"]) == str:
            relationsDescriptions += source["description"]
    return relationsDescriptions


def gatherTopArticleDescriptions(topArticles):
    topDescriptions = ""
    for source in topArticles:
        if type(source["title"]) == str:
            topDescriptions += source["title"]
        if type(source["content"]) == str:
            topDescriptions += source["content"]
        if type(source["description"]) == str:
            topDescriptions += source["description"]
    return topDescriptions
