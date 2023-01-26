class User():
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if kwargs['test'].is_logged_in == False:
            function(kwargs["test"])

        for log in args:
            if log.is_logged_in:
                function(log)

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Caglayan")
new_user.is_logged_in = True

new_user2 = User("Yogi")
new_user2.is_logged_in = True

new_user3 = User("Test")
new_user3.is_logged_in = False


create_blog_post(new_user, new_user2, test=new_user3)
