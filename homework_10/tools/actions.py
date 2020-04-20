import json
from tools import inputs


def create_article(articles):
    article_title = inputs.get_text("\nEnter article title: ", 0, False)
    article_body = inputs.get_text("Enter article body: ", 0, False)
    articles[article_title] = article_body
    write_to_file(articles)
    print(f"\nArticle '{article_title}' created\n")
    return articles


def delete_article(articles):
    article_title = inputs.get_text("\nEnter article title to delete: ", 0, False)
    try:
        articles.pop(article_title)
    except KeyError:
        print(f"Article '{article_title}' not found")
        return
    write_to_file(articles)
    print(f"\nArticle '{article_title}' deleted\n")
    return articles


def read_article(articles):
    article_title = inputs.get_text("\nEnter article title: ", 0, False)
    if article_title in articles.keys():
        print("\n=====")
        print(f"{article_title}")
        print("-----")
        print(articles[article_title])
        print("=====\n")
    else:
        print(f"\nArticle '{article_title}' not found\n")


def list_articles(articles):
    if len(articles) == 0:
        print("\nThere are no articles yet\n")
    else:
        print("\nArticles in our blog:")
        for key in articles:
            print(key)
        print()


def write_to_file(articles):
    with open("articles.json", "w") as f:
        articles = json.dumps(articles)
        f.write(articles)


def load_articles():
    try:
        with open("articles.json", "r") as f:
            try:
                articles = json.load(f)
            except json.JSONDecodeError:
                print("Blog file corrupted")
    except FileNotFoundError:
        articles = dict()
    return articles
