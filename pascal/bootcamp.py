from typing import List
from abc import ABC, abstractmethod
import random
import string


class Idea:
    pass


class User:
    def __init__(self, name: str):
        self._voted_ideas: List[Idea] = []
        self._name: str = name

    def rename(self, new_name: str) -> None:
        self._name = new_name

    def voted_for(self, idea: Idea) -> None:
        self._voted_ideas.append(idea)


class Idea:
    def __init__(self, creator: User, description: str):
        self._likes: int = 1
        self._description: str = description
        self._creator: User = creator

    def likes_count(self):
        return self._likes

    def __str__(self):
        return self._description


class IdeaCollection:
    def __init__(self):
        self._ideas = []

    def propose_idea(self, creator: User, idea: str) -> Idea:
        new_idea = Idea(creator, idea)
        self._ideas.append(new_idea)
        creator.voted_for(new_idea)
        return new_idea


class IdeaGenerator(ABC):
    def generate(self):
        while True:
            yield Idea(self._get_creator(), self.random_value())

    @abstractmethod
    def random_value(self):
        pass

    @abstractmethod
    def _get_creator(self):
        pass


class NumberIdeaGenerator(IdeaGenerator):
    _creator: User = User("Number")

    def _get_creator(self):
        return self._creator

    def random_value(self):
        return str(random.randrange(0, 999))


class TextIdeaGenerator(IdeaGenerator):
    _creator: User = User("Text")

    def _get_creator(self):
        return self._creator

    def random_value(self):
        return "".join(random.choice(string.ascii_letters) for _ in range(6))


if __name__ == "__main__":
    number_gen = NumberIdeaGenerator().generate()
    print(next(number_gen))
    print(next(number_gen))
    print(next(number_gen))
    print(next(number_gen))
    print(next(number_gen))
    text_gen = TextIdeaGenerator().generate()
    print(next(text_gen))
    print(next(text_gen))
    print(next(text_gen))
    print(next(text_gen))
    print(next(text_gen))
