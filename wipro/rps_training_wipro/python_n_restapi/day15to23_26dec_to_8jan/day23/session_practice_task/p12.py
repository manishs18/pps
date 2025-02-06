def requires_auth(func):
    def wrapper(*args, **kwargs):
        if not kwargs.get("is_auth"):
            print("Authentication Required!")
            return
        return func(*args, **kwargs)

    return wrapper

@requires_auth
def view_dashboard(is_auth=False):
    print("Welcome to your dashboard")

view_dashboard(is_auth=False)
