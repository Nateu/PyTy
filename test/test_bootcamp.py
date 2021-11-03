from pascal import User, Idea


def test_create_a_user():
    user = User("default")
    assert user._name == "default"


def test_rename_user():
    user = User("default")
    user.rename("Pascal")
    assert user._name == "Pascal"


def test_idea_by_pascal():
    user = User("Pascal")
    idea = Idea(user, "Best idea ever!")
    assert idea.likes_count() == 1
