from tools import inputs
from tools import actions


def main():
    actions_list = [
        "Create article",
        "Delete article",
        "Read article",
        "List articles",
        "Change role",
        "Add new user"
    ]
    articles = actions.load_articles()
    password = inputs.get_text("Enter password to log in", 3)
    while True:
        action = inputs.selector(actions_list, "Select your next action")
        if action[0] == 0:
            articles = actions.create_article(articles, password)
        elif action[0] == 1:
            articles = actions.delete_article(articles, password)
        elif action[0] == 2:
            actions.read_article(articles, password=password)
        elif action[0] == 3:
            actions.list_articles(articles, password=password)
        elif action[0] == 4:
            password = inputs.get_text("Enter password", 3)
        elif action[0] == 5:
            # passwords_mapping, passwords, permissions = actions.load_roles()
            actions.create_change_role(password=password)
        else:
            print("\nWrong choice")


if __name__ == '__main__':
    main()
