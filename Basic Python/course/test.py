import sys
from unittest import TestCase
import importlib

class Evaluate(TestCase):

    def test_output(self):
        import main
        output = sys.stdout.getvalue()
        expected_output = "1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes.\n"
        self.assertEqual(expected_output, output, "Output does not match expected output, check you havn't changed the original punctuation or letter casing at all.")


print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
