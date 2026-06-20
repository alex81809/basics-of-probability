import random

def card_draw_experiment():
    deck = ['Heart', 'Diamond', 'Club', 'Spade']

    total_draws = 12
    heart_count = 0

    print("Drawing cards 12 times:\n")

    for i in range(total_draws):
        card = random.choice(deck)
        print(f"Draw {i + 1}: {card}")

        if card == 'Heart':
            heart_count += 1


    # Theoretical Probability
    theoretical_probability = 1 / 4

    # Experimental Probability
    experimental_probability = heart_count / total_draws

    print("\nTheoretical Probability of Heart:", theoretical_probability)
    print("Number of Hearts Drawn:", heart_count)
    print("Experimental Probability of Heart:", experimental_probability)

# Run the experiment
card_draw_experiment()
