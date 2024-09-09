# this is a mad lib example for functions
def madlib(adjective1, noun1, verb1, verb2, verb3, adjective2, adjective3, noun2, noun3):
    """Mad Lib Function"""
    story =f'''
Once upon a time, in a land of {adjective1} {noun1}s, there was a {adjective2} {noun2}. Every day, this {noun2} would {verb1} through the {adjective3} {noun3}, looking for adventure. One day, it decided to {verb2} to the nearby forest to {verb3} with the creatures there.
In the forest, the {noun2} met a {adjective3} creature that loved to {verb3} and tell stories. They became fast friends and spent the day {verb1} and sharing tales of their {adjective2} adventures. The {noun2} felt {adjective1} and grateful for the new friend it had made.
As the sun set, the {noun2} and the creature returned home, happy and {adjective2} from their day of {verb2} and laughter. They promised to meet again soon for more {adjective3} adventures.
'''
    return story
 # Collecting inputs from the user
    noun1 = get_input()
    verb1 = get_input()
    noun2 = get_input()
    adjective1 = get_input()
    noun3 = get_input()
    adjective2 = get_input()
    verb2 = get_input()
    adjective3 = get_input()
   

output_story = madlib('adjective1', 'adjective2', 'adjective3', 'noun1', 'noun2', 'noun3', 'verb1', 'verb2', 'verb3')
print(output_story)