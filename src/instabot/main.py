import instabot.persistence as persistence
from instabot.bot import InstaBot

if __name__ == '__main__':
    try:
        username = '8750000375'  # username goes here
        password = 'Insta@007'  # type your password here

        followed_accounts = persistence.read_followed_users()
        unfollowed_accounts = persistence.read_unfollowed_users()
        insta_bot = InstaBot(followed_accounts, unfollowed_accounts, username, password)
        insta_bot.follow_people()


    finally:
        persistence.persist_followed_users(insta_bot.followed_accounts)
        # persistence.persist_unfollowed_users(insta_bot.unfollowed_accounts)
        insta_bot.shutdown()
