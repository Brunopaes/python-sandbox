import random


class Planet:
    def __init__(self):
        self.population = random.randint(100, 800)

    def remove_population(self):
        self.population -= 1


class InfiniteGaunlet:
    def __init__(self):
        self.planets_ = []
        self.sum_population = 0
        self.new_sum_population = 0

    def instancing_planets(self):
        for inst in range(10):
            self.planets_.append(Planet())
            self.sum_population += self.planets_[inst].population
            print('Original population: {}'.format(self.planets_[inst].population))

        print('Original Population Average: {}'.format(self.sum_population / len(self.planets_)))
        print('Desired Population Average: {}'.format(self.sum_population / 2 / len(self.planets_)))

    def thanos(self):
        for i in range(int(self.sum_population / 2)):
            chosen = random.choice(self.planets_)
            if chosen.population == 0:
                self.sum_population += 1
                continue
            else:
                chosen.remove_population()

        for i in self.planets_:
            print('Remaining Population: {}'.format(i.population))
            self.new_sum_population += i.population

        print('After Thanos-Effect Population Average: {}'.format(self.new_sum_population / len(self.planets_)))

    def main(self):
        self.instancing_planets()
        self.thanos()


if __name__ == '__main__':
    InfiniteGaunlet().main()
