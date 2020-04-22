import json
from tools import inputs


def save_roles(passwords_mapping, passwords, permissions):
    users = {"passwords": passwords, "passwords_mapping": passwords_mapping, "permissions": permissions}
    with open("users.json", "w") as f:
        users = json.dumps(users)
        f.write(users)


def create_admin():
    admin_password = input("Enter password for new admin: ")
    passwords_mapping = {"admin": "admin"}
    passwords = {admin_password: "admin"}
    permissions = {"create": ["admin"], "delete": ["admin"], "read": ["admin"], "list": ["admin"], "manage": ["admin"]}
    save_roles(passwords_mapping, passwords, permissions)
    return passwords_mapping, passwords, permissions


def load_roles():
    try:
        with open("users.json", "r") as f:
            try:
                users = json.load(f)
                passwords_mapping = users["passwords_mapping"]
                passwords = users["passwords"]
                permissions = users["permissions"]
            except json.JSONDecodeError:
                print("Blog file corrupted")
                passwords_mapping, passwords, permissions = create_admin()
    except FileNotFoundError:
        print("No users found")
        passwords_mapping, passwords, permissions = create_admin()
    return passwords_mapping, passwords, permissions


passwords_mapping, passwords, permissions = load_roles()


def user_has_access(allowed_roles):
    def wrapped(f):
        def wrapper(articles, password):
            role = passwords_mapping.get(passwords[password])
            if role in allowed_roles:
                return f(articles)
            else:
                print("\nYou can't do that\n")
                return articles
        return wrapper
    return wrapped


def user_can_manage(allowed_roles):
    def wrapped(f):
        def wrapper(password):
            role = passwords_mapping.get(passwords[password])
            if role in allowed_roles:
                return f()
            else:
                print("\nYou can't do that\n")
                return passwords_mapping, passwords, permissions
        return wrapper
    return wrapped


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


@user_has_access(permissions["create"])
def create_article(articles):
    article_title = inputs.get_text("\nEnter article title: ", 0, False)
    article_body = inputs.get_text("Enter article body: ", 0, False)
    articles[article_title] = article_body
    write_to_file(articles)
    print(f"\nArticle '{article_title}' created\n")
    return articles


@user_has_access(permissions["delete"])
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


@user_has_access(permissions["read"])
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


@user_has_access(permissions["list"])
def list_articles(articles):
    if len(articles) == 0:
        print("\nThere are no articles yet\n")
    else:
        print("\nArticles in our blog:")
        for key in articles:
            print(key)
        print()


@user_can_manage(permissions["manage"])
def create_change_role():
    global passwords_mapping, passwords, permissions
    role_name = inputs.get_text("Enter role name to change password or create new: ", 0, False).lower()
    passwords_mapping[role_name] = role_name
    role_pass = inputs.get_text(f"Enter password for role '{role_name}': ", 3, False)
    if role_pass in passwords.values():
        passwords[role_pass] = role_name
    can_create = inputs.confirm("Can this user create articles? ")
    if can_create and role_name not in permissions["create"]:
        permissions["create"].append(role_name)
    elif not can_create and role_name in permissions["create"]:
        permissions["create"].pop(role_name)
    can_delete = inputs.confirm("Can this user delete articles? ")
    if can_delete and role_name not in permissions["delete"]:
        permissions["delete"].append(role_name)
    elif not can_delete and role_name in permissions["delete"]:
        permissions["delete"].pop(role_name)
    can_read = inputs.confirm("Can this user read articles? ")
    if can_read and role_name not in permissions["read"]:
        permissions["read"].append(role_name)
    elif not can_read and role_name in permissions["read"]:
        permissions["read"].pop(role_name)
    can_list = inputs.confirm("Can this user view list of articles? ")
    if can_list and role_name not in permissions["list"]:
        permissions["list"].append(role_name)
    elif not can_list and role_name in permissions["list"]:
        permissions["list"].pop(role_name)
    can_manage = inputs.confirm("Can this user manage users? ")
    if can_manage and role_name not in permissions["manage"]:
        permissions["manage"].append(role_name)
    elif not can_manage and role_name in permissions["manage"]:
        permissions["manage"].pop(role_name)
    save_roles(passwords_mapping, passwords, permissions)
    print(f"\nRole {role_name} created\n")
    return passwords_mapping, passwords, permissions
