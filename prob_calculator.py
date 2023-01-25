import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = list()
        for color, amount in kwargs.items():
            self.color = color
            self.amount = amount
            for i in range(self.amount):
                self.contents.append(self.color)
        # print(self.contents)

    def draw(self, num_balls):
        self.num_balls = num_balls
        self.removed_balls = list()
        if self.num_balls > self.amount:
            return self.contents
        else:
            for k in range(self.num_balls):
                self.select = random.randint(0, len(self.contents)-1)
                # print(self.select)
                self.removed_balls.append(self.contents[self.select])
                self.contents.pop(self.select)
            return self.removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  
    expected_balls_list = list()
    for color, amount in expected_balls.items():
        for i in range(amount):
            expected_balls_list.append(color)

    # print(expected_balls_list)
    probability = 0
    N = 0
    while N < num_experiments:

        new_contents = copy.copy(hat.contents)
        # print(new_contents)
        removed_balls = list()
        if num_balls_drawn > len(new_contents):
            num_balls_drawn = len(new_contents)

        for i in range(num_balls_drawn):
            # print(len(new_contents))
            select_e = random.randint(0,len(new_contents)-1)
            # print(select_e)
            removed_balls.append(new_contents[select_e])
            new_contents.pop(select_e)
            # print(new_contents)
        # print(removed_balls)


        count = 0
        for ball_e in expected_balls_list:
            for ball_r in removed_balls:
                if ball_e == ball_r:
                    count += 1
                    removed_balls.remove(ball_e)
                    break
            if count == len(expected_balls_list):
                probability += 1

        N += 1

    probability = (probability/num_experiments)

    return probability
