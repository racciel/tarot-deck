import random

major_arcana = [
            # Major Arcana
            "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant",
            "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man",
            "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]
minor_arcana = [
            # Minor Arcana - Wands
            "Ace of Wands", "Two of Wands", "Three of Wands", "Four of Wands", "Five of Wands", "Six of Wands", 
            "Seven of Wands", "Eight of Wands", "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands", 
            "Queen of Wands", "King of Wands",
            # Minor Arcana - Cups
            "Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups", "Five of Cups", "Six of Cups", 
            "Seven of Cups", "Eight of Cups", "Nine of Cups", "Ten of Cups", "Page of Cups", "Knight of Cups", 
            "Queen of Cups", "King of Cups",
            # Minor Arcana - Swords
            "Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords", "Five of Swords", "Six of Swords", 
            "Seven of Swords", "Eight of Swords", "Nine of Swords", "Ten of Swords", "Page of Swords", "Knight of Swords", 
            "Queen of Swords", "King of Swords",
            # Minor Arcana - Pentacles
            "Ace of Pentacles", "Two of Pentacles", "Three of Pentacles", "Four of Pentacles", "Five of Pentacles", 
            "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles", "Nine of Pentacles", "Ten of Pentacles", 
            "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles"
        ]

# Tarot deck (Major Arcana and Minor Arcana)
class Deck:
    def collect_deck(self, major_only=False):
        if major_only:
            self.tarot_deck = major_arcana
            return
        self.tarot_deck = major_arcana + minor_arcana
        
    def shuffle(self):
        random.shuffle(self.tarot_deck)
        
    def clean(self, major=False):
        self.collect_deck(major)
        self.shuffle()
        
    def __init__(self, major=False):
        self.collect_deck(major)
        self.shuffle()
    
    def draw_cards(self, number=1):
        drawn = None
        try:
            drawn = random.sample(self.tarot_deck, number)
            for card in drawn:
                self.tarot_deck.remove(card)
        except ValueError:
            print("No more cards to draw!")
            if(len(self.tarot_deck) > 0):
                drawn = random.sample(self.tarot_deck, len(self.tarot_deck))
                for card in drawn:
                    self.tarot_deck.remove(card)
                print("The rest of the deck:")
        if drawn:
            return drawn
        else:
            return
        
    def celtic_cross(self):
        self.clean()
        return self.draw_cards(10)
    
    def three_spread(self, major=False):
        self.clean(major)
        return self.draw_cards(3)
    
    def five_spread(self, major=False):
        self.clean(major)
        return self.draw_cards(5)
           
deck = Deck()

deck.celtic_cross()

deck.draw_cards(2)

deck.three_spread(major=True)

deck.draw_cards()

deck.five_spread()