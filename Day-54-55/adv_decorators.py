class User:

    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def check_authentication(function):
    def wrapper(*args, **kwargs):
        if (args[0].is_logged_in == True):
            function(args[0])
    
    return wrapper


@check_authentication
def show_home(user):
    print(f"Welcome {user.name}.")


meet = User("Meet Thummar")
meet.is_logged_in = True
show_home(meet)