class Rock:
    def __init__(self):
        self.name = "the rock"

        self.hunger = 10
        self.max_hunger = 100

        self.health = 100
        self.max_health = 100

        self.food_choices = {"Apple", "Burger", "Instant noodles"}
        self.choices = ["Feed the rock", "Play with the rock", "Throw the rock away", "Name the rock"]

    def show_stats(self):
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Hunger: {self.hunger}/{self.max_hunger}")

    def parse_choice(self, choice):
        if choice == "Feed the rock":
            food_choice = show_choices(self.food_choices, "What would you like to feed the rock?")
            if food_choice in ["Apple", "Instant noodles"]:
                print(f"You set the {food_choice.lower()} beside the rock, unsure of how to feed it. After a few seconds, you feel a sharp pain in your head",
                      "as the rock speaks:",
                      '\t"What is this? This isn\'t food! Bring me something I can eat, like flesh or a sacrafice"',
                      "The pain in your head subsides as quickly as it appeared, and you are left standing, confused.", sep="\n")
                self.food_choices.difference_update({"Apple", "Instant noodles"})
                self.food_choices.update({"Raw beef", "Finger", "Goat"})
            elif food_choice == "Burger":
                print("You put the burger next to the rock, and it speaks:",
                      '\t"Hmmmm... this is edible, but I perfer raw or still-living foods"'
                      "You walk away as the burger disappears, concerned for what you will have to do to fulfill the rock's hunger", sep="\n")
                print("+10 hunger")
                self.hunger += 10
                self.food_choices.update({"Raw beef", "Finger", "Goat"})


def show_choices(choices, intro=""):
    while True:
        try:
            if intro:
                print(intro)

            for i, choice in enumerate(choices):
                print(f"\t{i + 1}. {choice}")

            player_choice = int(input("Choose an option: "))

            if player_choice > len(choices):
                print(f"Pick a value less than {len(choices)}")
                continue

            return choices[player_choice - 1]
        except ValueError:
            continue


def main():
    day_count = 0
    rock = Rock()

    print("One fateful day, while walking on the side of the road, you are all of a sudden blinded.",
          "When your vision clears, you see a rock. It looks like an ordinary rock, but you can tell something is different about it.",
          "Curious, you pick it up and decide to take it home. You leave it on your kitchen table, and every time you",
          "walk by it, you get a strange foreboding feeling. After about a week, just when you are considering whether to",
          "throw it away, it begins to speak:",
          '\t"I grow hungry. I demand sacrifices"',
          "Freaked out, you attempt to pick up the rock to destroy it. As you make contact with the rock, a shock runs up",
          "your arm and you jerk your hand away quickly. The rock speaks again:",
          '\t"I wouldn\'t do that if I were you. You don\'t want to end up like them"',
          "As you wonder what a rock even eats, you wonder what you have gotten yourself into...\n", sep="\n")

    try:
        while True:
            day_count += 1
            print(f"Day {day_count}:\n")
            rock.show_stats()
            player_choice = show_choices(rock.choices, "What would you like to do?")

            rock.parse_choice(player_choice)

    except KeyboardInterrupt:
        print(f"\n{rock.name} is dissapointed in you for abandoning it. Please do better next time")


if __name__ == "__main__":
    main()
