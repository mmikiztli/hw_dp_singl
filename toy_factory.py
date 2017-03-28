import logger


class Toy:

    def __init__(self, name):
        self.name = name.lower().strip()
        self.log = logger.Logger()

    def prepare(self):
        self.log.log("preparing %s" % self.name)

    def make(self):
        self.log.log("making %s" % self.name)

    def package(self):
        self.log.log("packaging %s" % self.name)


class ToyFactory:

    @staticmethod
    def make_toy(toy_name):
        try:
            toy_name = str(toy_name).lower().replace(" ", "")
            if toy_name == 'boat':
                return Toy('boat')
            elif toy_name == 'racecar':
                return Toy('racecar')
            elif toy_name == 'spaceship':
                return Toy('space ship')
        except NameError:
            return ('Factory can\'t create the given type')


def main():
    toy_type = input(
        'What type of toy you want to make? (boat, racecar, space ship): ')
    toy = ToyFactory.make_toy(toy_type)
    toy.prepare()
    toy.make()
    toy.package()


if __name__ == '__main__':
    main()
