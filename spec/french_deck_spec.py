from mamba import describe, context, it, before
from expects import expect, equal
from pascal.french_deck import FrenchDeck

with describe("Given a french deck of cards") as self:
    with before.each:
        self.deck = FrenchDeck()

    with context("when counting all cards"):
        with it("should have 52 cards"):
            expect(len(self.deck)).to(equal(52))

    with context("when taking the first card"):
        with it("should have a rank 2"):
            expect(self.deck[0].rank).to(equal("2"))

        with it("should have a suit spades"):
            expect(self.deck[0].suit).to(equal("spades"))

    with context("when taking the 15th card"):
        with it("should have a rank 3"):
            expect(self.deck[14].rank).to(equal("3"))

        with it("should have a suit diamonds"):
            expect(self.deck[14].suit).to(equal("diamonds"))
