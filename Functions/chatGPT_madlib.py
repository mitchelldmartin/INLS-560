def get_input(prompt):
    return input(prompt + ": ")

def mad_libs():
    print("Welcome to Basketball Mad Libs!")

    # Collecting inputs from the user
    noun1 = get_input("Enter a noun (e.g., player, coach, team)")
    adjective1 = get_input("Enter an adjective (e.g., exciting, skilled)")
    verb1 = get_input("Enter a verb (past tense, e.g., scored, dribbled)")
    noun2 = get_input("Enter another noun (e.g., game, court, shot)")
    adverb1 = get_input("Enter an adverb (e.g., quickly, energetically)")
    noun3 = get_input("Enter a third noun (e.g., teammate, referee)")
    adjective2 = get_input("Enter another adjective (e.g., intense, thrilling)")
    verb2 = get_input("Enter another verb (present tense, e.g., pass, shoot)")
    noun4 = get_input("Enter another noun (e.g., basket, point)")

    # Creating the story
    story = (
        f"One day, a {adjective1} {noun1} was playing in an important basketball {noun2}. The game had {adverb1} "
        f"started, and the {noun1} {verb1} the ball with great precision. Fans cheered as the {adjective1} {noun1} "
        f"made incredible plays that left everyone in awe. The score was close, and the tension was high.\n\n"

        f"In the second quarter, the {noun1} and their {noun3} worked together to create an {adjective2} strategy. "
        f"With every {noun2}, they {verb2} the ball around, looking for the perfect opportunity to {verb1} towards "
        f"the {noun4}. The {adjective2} atmosphere of the game kept everyone on the edge of their seats.\n\n"

        f"As the final buzzer approached, the {noun1} made a last-ditch effort to win the game. With a {adjective2} "
        f"shot, they {verb1} the ball into the {noun4}, clinching the victory. The crowd erupted in cheers as the "
        f"{noun1} celebrated their hard-earned triumph. It was a game to remember, filled with excitement and {adjective2} "
        f"moments."
    )

    print("\nHere's your Basketball Mad Libs story:\n")
    print(story)

if __name__ == "__main__":
    mad_libs()
