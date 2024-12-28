import random
import json

# Load verbs from a JSON file
def load_verbs():
    try:
        with open('verbs.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save verbs to a JSON file
def save_verbs(verbs):
    with open('verbs.json', 'w', encoding='utf-8') as file:
        json.dump(verbs, file, ensure_ascii=False, indent=4)

verbs = load_verbs()

# Function to add a new verb and its conjugations
def add_verb():
    print("Add a new verb and its conjugations.")
    verb = input("Enter the infinitive form of the verb: ").strip().lower()
    if verb in verbs:
        print("This verb already exists in the database.")
        return

    conjugations = {}
    subjects = ["yo", "tú", "él/ella/usted", "nosotros/nosotras", "ellos/ellas/ustedes"]
    for subject in subjects:
        conjugation = input(f"Enter the conjugation for '{subject}': ").strip().lower()
        conjugations[subject] = conjugation

    verbs[verb] = conjugations
    save_verbs(verbs)
    print(f"Verb '{verb}' has been added successfully!")

# CLI for practicing conjugation
def practice_conjugation():
    if not verbs:
        print("No verbs available. Please add some verbs first.")
        return

    correct_count = 0
    incorrect_count = 0

    print("Welcome to the Spanish Verb Conjugation Practice App!")
    print("Type 'quit' at any time to exit.")

    while True:
        try:
            verb = random.choice(list(verbs.keys()))
            subject = random.choice(list(verbs[verb].keys()))

            print("\n===========================")
            print(f"Conjugate the verb '{verb}' for the subject '{subject}':")
            print("===========================")
            user_answer = input("Your answer: ").strip().lower()

            if user_answer == "quit":
                print("\nThanks for practicing! Adiós!")
                print(f"You got {correct_count} correct and {incorrect_count} incorrect answers.")
                break

            correct_answer = verbs[verb][subject]
            if user_answer == correct_answer:
                print("Correct! ✓")
                correct_count += 1
            else:
                print(f"Incorrect. The correct answer is '{correct_answer}'.")
                incorrect_count += 1
        except KeyboardInterrupt:
            print("\nSession interrupted. Exiting practice mode.")
            print(f"You got {correct_count} correct and {incorrect_count} incorrect answers.")
            break

if __name__ == "__main__":
    while True:
        print("1. Practice conjugation")
        print("2. Add a new verb")
        print("3. Quit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            practice_conjugation()
        elif choice == "2":
            add_verb()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")