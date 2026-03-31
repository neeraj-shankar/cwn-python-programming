import pickle

class DoSomething:
    # A complex dictionary we want to save
    data = {"user_id": 42, "roles": ["admin", "editor", "wizard"], "active": True}

    def say_hello():
        print(f"Hey there I am picled")


if __name__ == "__main__":

    obj = DoSomething()

    with open("pickled.pkb", "wb") as f:
        pickle.dump(obj, f)
