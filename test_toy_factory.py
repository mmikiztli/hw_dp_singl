import unittest
import toy_factory


class ToyFactoryTests(unittest.TestCase):

    def testIsBoat(self):
        toy = toy_factory.ToyFactory.make_toy('boat')
        result = toy.name
        self.assertEqual(result, 'boat')

    def testIsRaceCar(self):
        toy = toy_factory.ToyFactory.make_toy('racecar')
        result = toy.name
        self.assertEqual(result, 'racecar')

    def testIsSpaceShip(self):
        toy = toy_factory.ToyFactory.make_toy('space ship')
        result = toy.name
        self.assertEqual(result, 'space ship')

    def testNameError(self):
        toy = toy_factory.ToyFactory.make_toy(123)
        self.assertEqual(toy, None)

    def testStrip(self):
        toy = toy_factory.ToyFactory.make_toy(' race car ')
        result = toy.name
        self.assertEqual(result, 'racecar')

    def testLower(self):
        toy = toy_factory.ToyFactory.make_toy('BOaT')
        result = toy.name
        self.assertEqual(result, 'boat')

    def testToyFactoryAttribute(self):
        toy = toy_factory.ToyFactory()
        result = hasattr(toy, 'prepare')
        self.assertEqual(result, False)

    def testToyLogOrder(self):
        toy_name = 'space ship'
        toy = toy_factory.ToyFactory.make_toy(toy_name)
        methods_in_order = [toy.prepare(), toy.make(), toy.package()]
        with open("%s.txt" % toy.log.file_name) as f:
            rows = f.readlines()
        lines = [line.strip("\n") for line in rows]
        result = "preparing %s" % toy_name == lines[0] and "making %s" % toy_name == lines[
            1] and "packaging %s" % toy_name == lines[2]
        self.assertEqual(result, True)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
