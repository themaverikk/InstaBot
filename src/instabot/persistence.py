from pathlib import Path

from ordered_set import OrderedSet


def persist_followed_users(followed_accounts):
    print("persisting {0} usernames to file...".format(len(followed_accounts)))

    with open('followed_users.txt', 'w') as file:
        for insta_username in followed_accounts:
            file.write(insta_username + '\n')

    print("successfully persisted {0} usernames to file".format(len(followed_accounts)))


def persist_unfollowed_users(unfollowed_accounts):
    print("persisting {0} unfollowed usernames to file...".format(len(unfollowed_accounts)))

    with open('unfollowed_users.txt', 'w') as file:
        for insta_username in unfollowed_accounts:
            file.write(insta_username + '\n')

    print("successfully persisted {0} unfollowed usernames to file".format(len(unfollowed_accounts)))


def read_followed_users():
    followed_accounts_file = Path('followed_users.txt')

    if followed_accounts_file.is_file():
        print("retrieving already followed usernames from file...")

        followed_accounts = OrderedSet(open(followed_accounts_file, 'r').readlines())
        followed_accounts = OrderedSet(insta_username.strip() for insta_username in followed_accounts)

        print("successfully retrieved already followed usernames from file")

        return followed_accounts


def read_unfollowed_users():
    unfollowed_accounts_file = Path('unfollowed_users.txt')

    if unfollowed_accounts_file.is_file():
        print("retrieving already unfollowed usernames from file...")

        unfollowed_accounts = set(open(unfollowed_accounts_file, 'r').readlines())
        unfollowed_accounts = set(insta_username.strip() for insta_username in unfollowed_accounts)

        print("successfully retrieved already unfollowed usernames from file")

        return unfollowed_accounts
