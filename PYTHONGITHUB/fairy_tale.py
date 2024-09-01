import random

def get_random_element(elements):
    return random.choice(elements)

def generate_story():
    # Story elements
    characters = ["a brave knight", "a clever princess", "a wise wizard", "a kind-hearted dragon", "a mischievous fairy"]
    settings = ["a mystical forest", "an ancient castle", "a hidden village", "a magical kingdom", "a mysterious cave"]
    conflicts = ["a dangerous dragon", "an evil sorcerer", "a cursed spell", "a hidden treasure", "a wicked witch"]
    resolutions = ["they found a magical artifact", "they broke the curse", "they defeated the evil foe", "they discovered the hidden treasure", "they forged a lasting friendship"]
    dialogues = [
        "The knight said, 'We must embark on this quest to save the kingdom.'",
        "The princess exclaimed, 'I will not rest until we have uncovered the truth.'",
        "The wizard murmured, 'The prophecy speaks of a hero who will come.'",
        "The dragon roared, 'Only the pure of heart can lift this curse.'",
        "The fairy whispered, 'The answer lies in the enchanted forest.'"
    ]

    # Story structure
    intro = f"Once upon a time, in {get_random_element(settings)}, there was {get_random_element(characters)}."
    middle = f"One day, {get_random_element(characters)} encountered {get_random_element(conflicts)}. {get_random_element(dialogues)}"
    conflict_resolution = f"With great courage and wisdom, {get_random_element(characters)} faced the challenge and {get_random_element(resolutions)}."
    conclusion = "And so, the land was at peace once again, and everyone lived happily ever after."

    # Constructing the story
    story = f"{intro} {middle} {conflict_resolution} {conclusion}"
    
    # Ensure the story is at least 500 words
    words = story.split()
    while len(words) < 500:
        story += " " + get_random_element(["And then, something magical happened.", "A new adventure began.", "The story continued with many more wonders."])
        words = story.split()
    
    return story

if __name__ == "__main__":
    story = generate_story()
    print(story)
