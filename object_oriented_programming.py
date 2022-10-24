from symbol import parameters


class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        if self.condition == "perfect" or "repaired":
            return print(f"Podracer is already {self.condition}")
        else:
            self.condition = "repaired"
            return print("Podracer is repaired")


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

        def boost(self):
            max_speed = max_speed * 2
            return print(max_speed)


class SebulasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

        def flame_jet(self):
            condition = "thrashed"
            return print("thrashed")


# Questions

# HOW DOES THIS SOLUTION DEMONSTRATE THE FOUR PILLARS OF OOP?

#     Encapsulation: data is stored in each of the Podracer classes.
#     Inheritance: two different classes inherit a base class and its parameters


# WOULD IT HAVE BEEN EASIER TO IMPLEMENT A SOLUTION TO THIS PROBLEM USING A DIFFERENT CODING STYLE? WHY OR WHY NOT?

#     This was the best way to solve this type of problem. One piece of code was used to create infinite amounts of Podraces with individual sets of data.


# HOW IN PARTICULAR DID OBJECT ORIENTED PPROGRAMMING ASSIST IN THE SOLVING OF THIS PROBLEM?

#     Refer to second part of answer above.
