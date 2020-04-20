from tools import inputs
from tools import actions

actions_list = [
    "Create article",
    "Delete article",
    "Read article",
    "List articles",
    "Change role"
]

admin = "123"
editor = "456"
reader = "789"

passwords_mapping = {
    admin: "admin",
    editor: "editor",
    reader: "reader"
}


def user_has_access(allowed_roles):
    def wrapped(f):
        def wrapper(articles, password):
            role = passwords_mapping.get(password)
            if role in allowed_roles:
                return f(articles)
            else:
                print("\nYou can't do that\n")
                return articles
        return wrapper
    return wrapped


@user_has_access(("reader", "admin", "editor"))
def list_articles(articles):
    actions.list_articles(articles)


@user_has_access(("admin", "editor"))
def create_article(articles):
    articles = actions.create_article(articles)
    return articles


@user_has_access("admin")
def delete_article(articles):
    articles = actions.delete_article(articles)
    return articles


@user_has_access(("admin", "editor", "reader"))
def read_article(articles):
    actions.read_article(articles)


def main():
    articles = actions.load_articles()
    password = inputs.get_text("Enter password", 3)
    while True:
        action = inputs.selector(actions_list, "Select your next action")
        if action[0] == 0:
            articles = create_article(articles, password)
        elif action[0] == 1:
            articles = delete_article(articles, password)
        elif action[0] == 2:
            read_article(articles, password=password)
        elif action[0] == 3:
            list_articles(articles, password=password)
        elif action[0] == 4:
            password = inputs.get_text("Enter password", 3)


if __name__ == '__main__':
    main()
