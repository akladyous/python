import numpy as np



class Card:
    __counter = 0

        
    values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    suit   =  ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    list((v,s) for v in values for s in suit)
    

value_dct = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'J': 11,'Q': 12,'K': 13,'A': 14}
value_dct.get('S','Missing Key')

