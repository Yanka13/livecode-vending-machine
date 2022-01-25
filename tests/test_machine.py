# tests/test_machine.py
import unittest
from machine import Rack, Machine, Coin


class MachineTest(unittest.TestCase):
    #Tester feature 1 - Un agent peut remplir les stocks
    def test_agent_can_refill_A(self):

        # Je dois instancier des stocks - 0 quantité par défaut
        racks = [Rack("A", "", 100)]

        # Je dois instancier une machine qui doit avoir des stocks A
        machine = Machine(racks)

        # L'agent remplit la machine avec 10 produits "A"
        machine.refill("A", 10)

        # Assertions : Je vérifie qu'à la fin j'ai bien
        # rajouté les produits que l'agent a mis
        self.assertEqual(machine.racks["A"].quantity, 10)

    #Tester feature 2 - Un utilisateur puisse commander un produit A
    def test_agent_can_order_A(self):
        # Je dois instancier des stocks - 0 par défault
        racks = [Rack("A", "", 100)]

        # Je dois instancier une machine qui doit avoir des stocks "A" SANS monnaie
        machine = Machine(racks, 0)

        # Je remplis la machine avec 10 produits "A"
        machine.refill("A", 10)

        # Un utilisateur  insère un dollar
        machine.insert(Coin.DOLLAR)

        # Un utilisateur press  le bouton A pour commander un produit
        outcome = machine.press("A")


        # On  vérifie que :
        # - Il a le droit de commander
        self.assertEqual(outcome, True)

        # - Il y a 9 produits en stock dans la machine
        self.assertEqual(machine.racks["A"].quantity, 9)

        # - Dans la machine, il y a bien une pièce de 1 dollar en plus
        self.assertEqual(machine.coins[Coin.DOLLAR], 1)



    #Tester feature 3 - Un utilisateur qui commande en mettant
    # un surplus d'argent va recevoir le reste de sa monnaie
    def test_machine_gives_money_back_C(self):
        # J'instancie des stocks de C, par défaut 0 quantité
        racks = [Rack("C", "", 85)]

        # Je dois instancier une machine qui accepte des stocks de C et avec
        # 10 pièces de chaque
        machine = Machine(racks, 10)

        # L'agent met un produit de C dans la machine (quantité = 1)
        machine.refill("C", 1)

        # Un utilisateur insère une pièce de 1 dollar
        machine.insert(Coin.DOLLAR)

        # Un utilisateur presse le bouton C pour commander
        machine.press("C")


        # vérifier qu'on lui a rendu 15 cents, soit une pièce de NICKEL et une pièce de DIME
        self.assertEqual(machine.coins[Coin.NICKEL], 9)
        self.assertEqual(machine.coins[Coin.DIME], 9)


if __name__ == "__main__":
    racks = [Rack("A", "", 100), Rack("C", "", 85)]
    racks = dict((rack.code, rack) for rack in racks)
    print(racks)

    for coin in Coin:
        print(coin, coin.value)

