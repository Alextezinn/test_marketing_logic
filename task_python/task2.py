import random


class GroupDistribution:
    def __init__(self, num_people=20, num_groups=2, num_people1=19, num_people2=20):
        self.num_people = num_people
        self.num_groups = num_groups
        self.num_people1 = num_people1
        self.num_people2 = num_people2
        self.people = list(range(1, num_people + 1))
        self.groups = [[] for _ in range(num_groups)]
        self.simulations = 1000000  # Количество симуляций
        self.success_count = 0

    def divide_people_groups(self):
        random.shuffle(self.people)
        for i, person in enumerate(self.people):
            self.groups[i % self.num_groups].append(person)

    def _check_two_people_together(self):
        for group in self.groups:
            if self.num_people1 in group and self.num_people2 in group:
                return True
        return False

    def simulate(self):
        for _ in range(self.simulations):
            self.divide_people_groups()
            if self._check_two_people_together():
                self.success_count += 1
            self.groups = [[] for _ in range(self.num_groups)]

    def calculate_probability(self):
        self.simulate()
        probability = self.success_count / self.simulations
        return probability


if __name__ == "__main__":
    num_people1 = 19
    num_people2 = 20
    assignment = GroupDistribution(num_people1=num_people1, num_people2=num_people2)
    probability = assignment.calculate_probability()
    print(f"Вероятность того, что {num_people1} и {num_people2} находятся в одной группе, равна: {probability*100:.4f} %")
