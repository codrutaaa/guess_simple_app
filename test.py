import unittest
import main

#ideea unui test unitar este aceea de a testa fiecare unit din cod
# putem ssparge ce este in main in mai multe functii mici pt testat

class TestGame(unittest.TestCase):

    def setUp(self):
        print("about to test a function")

    def test_input(self): #cati param sunt la functie atatia punem in testare
        answer=5
        guess=5
        result = main.run_guess(answer,guess)
        self.assertTrue(result)

    def test_input_wrong_guess(self): #cati param sunt la functie atatia punem in testare
        answer=0
        guess=5
        result = main.run_guess(answer,guess)
        self.assertFalse(result)

    def test_input_big_guess(self): #cati param sunt la functie atatia punem in testare
        answer=5
        guess=12
        result = main.run_guess(answer,guess)
        self.assertFalse(result)

    # def test_input_big_guess2(self): #cati param sunt la functie atatia punem in testare
    #     answer=5
    #     guess=12
    #     result = main.run_guess(answer,guess)
    #     self.assertEqual(result, 'hey bozo, I said 1~10')

    def test_input_wrong_guess2(self):  # cati param sunt la functie atatia punem in testare
        answer = 5
        guess = '12'
        result = main.run_guess(answer, guess)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()