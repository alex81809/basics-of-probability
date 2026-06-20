import random

def dice_roll_experiment():
    # Roll a dice 10 times
    total_rolls = 10
    six_count = 0

    print("Rolling the dice 10 times:\n")

    for i in range(total_rolls):
        roll = random.randint(1, 6)
        print(f"Roll {i + 1}: {roll}")

        if roll == 6:
            six_count += 1

    # Theoretical Probability
    theoretical_probability = 1/6

    # Experimental Probability
    experimental_probability = six_count / total_rolls

    print("\nTheoretical Probability of getting 6:", theoretical_probability)
    print("Number of times 6 appeared:", six_count)
    print("Experimental Probability of getting 6:", experimental_probability)

# Run the experiment
dice_roll_experiment()
