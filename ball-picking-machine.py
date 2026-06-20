import random

def pick_ball_experiment():
    # Defining the balls
    balls = ['Blue', 'Red', 'Green']

    # Theoretical Probability
    probability_red = balls.count('Red') / len(balls)
    print("Theoretical Probability of Picking a Red Ball: ", probability_red)

    # Counters
    red_count = 0
    total_trials = 10

    print("\nResults of 10 Picks: ")
    for i in range(total_trials):
        result = random.choice(balls)
        print(f"Pick {i+1}: {result}")

        if result == 'Red':
            red_count += 1

    # Experimental Probability
    experimental_probability = red_count / total_trials

    print("\nNumber of Red Balls Picked: ", red_count)
    print("Experimental Probability of Red Ball: ", experimental_probability)

# Run the experiment
pick_ball_experiment()
