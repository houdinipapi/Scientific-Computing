import random
import copy


class Hat:
    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    def draw(self, num_balls):
        num_balls = min(num_balls, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(num_balls)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls_drawn = new_hat.draw(num_balls_drawn)
        required_balls = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        success_count += 1 if required_balls == len(expected_balls) else 0

    probability = success_count / num_experiments
    return probability
