# class decorator

def add_id(cls):
    cls.id = 100
    return cls 


@add_id
class TestMe():
    pass

print(TestMe.id)