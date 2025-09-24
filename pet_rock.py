class Rock:
    def __init__(self):
        self.name = "the rock"

        self.hunger = 30
        self.max_hunger = 100

        self.satisfaction = 100
        self.max_satisfaction = 100

        self.finger_count = 10

        self.food_choices = {"Apple", "Burger", "Instant noodles"}
        self.choices = [f"Feed {self.name}", f"Play with {self.name}", f"Throw {self.name} away", f"Name {self.name}", "Do nothing"]

    def show_stats(self):
        print(f"Satisfaction: {self.satisfaction}/{self.max_satisfaction}")
        print(f"Hunger: {self.hunger}/{self.max_hunger}")

    def add_hunger(self, amount):
        print(f"{amount:+} hunger")
        self.hunger += amount
        self.hunger = min(self.hunger, self.max_hunger)

    def add_satisfaction(self, amount):
        print(f"{amount:+} satisfaction")
        self.satisfaction += amount
        self.satisfaction = min(self.satisfaction, self.max_satisfaction)

    def parse_choice(self, choice):
        if choice == f"Feed {self.name}":
            food_choice = show_choices(list(self.food_choices), f"What would you like to feed {self.name}?")

            if food_choice in ["Apple", "Instant noodles"]:
                print(f"You set the {food_choice.lower()} beside {self.name}, unsure of how to feed it. After a few seconds, you feel a sharp pain in your head",
                      f"as {self.name} speaks:",
                      '\t"What is this? This isn\'t food! Bring me something I can eat, like flesh or a sacrafice"',
                      "The pain in your head subsides as quickly as it appeared, and you are left standing, confused.", sep="\n")
                self.food_choices.difference_update({"Apple", "Instant noodles"})
                self.food_choices.update({"Raw beef", "Finger", "Goat"})

            elif food_choice == "Burger":
                print(f"You put the burger next to {self.name}, and it speaks:",
                      '\t"Hmmmm... this is edible, but I perfer raw or still-living foods"',
                      f"You walk away as the burger disappears, concerned for what you will have to do to fulfill {self.name}'s hunger", sep="\n")
                self.add_hunger(10)
                self.food_choices.update({"Raw beef", "Your Finger", "Goat"})

            elif food_choice == "Raw beef":
                print(f"You go to the store to buy some raw beef. When you get home, you place it next to {self.name} and wait to see how it",
                      f"reacts. After a moment {self.name} speaks:",
                      '"I am pleased. My hunger has been partially fulfilled. You have done satisfactory"',
                      f"You can't help but feel a sense of pride at {self.name}'s words", sep="\n")
                self.add_hunger(30)

            elif food_choice == "Your Finger":
                if self.finger_count > 0:
                    print("You take a deep breath, grab a knife, and lay your hand out on the table. Without stopping to think, you swing the",
                          "knife down, and your finger comes off in with a rush of blood. Before you even have time to process what",
                          f"you have just done, your disconnected finger disappears and {self.name} speaks:",
                          '\t"Yes... this is acceptable. You show true devotion."',
                          "The pain in your hand dulls slightly, replaced by a strange warmth in your chest", sep="\n")
                    self.add_hunger(50)
                    self.add_satisfaction(10)
                    self.finger_count -= 1
                else:
                    print(f"You have no fingers left. {self.name} is not amused")
                    self.add_satisfaction(-10)

            elif food_choice == "Goat":
                print(f"You find a goat and bring it before {self.name}. The creature struggles against you, bleating in fear.",
                      f"As you lay the goat down beside {self.name}, a dark presence fills the air.",
                      f"{self.name} speaks, its voice echoing inside your skull:",
                      '\t"A sacrifice... yes. This pleases me greatly."',
                      "The goat goes silent in an instant, vanishing without a trace.",
                      f"You stumble backward, your heart racing, but you are glad to see {self.name} pleased", sep="\n")
                self.add_hunger(70)
                self.add_satisfaction(20)

        elif choice == f"Play with {self.name}":
            play_choice = show_choices(["Pet", "Tell a joke", "Sing a song"], f"How will you play with {self.name}?")
            if play_choice == "Pet":
                print(f"You gently place your hand on {self.name}. The stone is cold and unfeeling.",
                      f"After a long silence, {self.name} speaks:",
                      '\t"Strange... but not unpleasant."',
                      "You feel as if you’ve formed a small bond.", sep="\n")
                self.add_satisfaction(10)

            elif play_choice == "Tell a joke":
                print("You tell the best joke you can think of.",
                      f"For a moment, silence fills the air. Then {self.name} vibrates ever so slightly.",
                      '\t"Amusing. You may continue to entertain me."',
                      "A sense of relief washes over you.", sep="\n")
                self.add_satisfaction(15)

            elif play_choice == "Sing a song":
                print("You sing a tune to the best of your ability.",
                      f"{self.name} is silent, but you swear you hear a faint hum in the air around it.",
                      '\t"I remember... long ago, others sang too. You please me."',
                      "You are left with a strange melancholy, but {self.name} seems satisfied.", sep="\n")
                self.add_satisfaction(20)

        elif choice == f"Throw {self.name} away":
            confirm = show_choices(["Yes", "No"], f"Are you sure you want to throw {self.name} away?")
            if confirm == "Yes":
                print("You take {self.name} far from your home and cast it into a river.",
                      "For a brief moment, you feel free.",
                      "Then, a crushing pain fills your skull, and a voice thunders in your head:",
                      '\t"YOU THINK YOU CAN DISPOSE OF ME?"',
                      "You collapse to the ground, realizing you can never truly be rid of it.", sep="\n")
                self.add_satisfaction(-50)
            else:
                print(f"You decide against throwing {self.name} away. It seems pleased you reconsidered.")
                self.add_satisfaction(5)

        elif choice == f"Name {self.name}":
            new_name = input("What will you name the rock? ")
            print(f"You whisper the name '{new_name}' to the stone.",
                  f"After a pause, {self.name} responds:",
                  f'\t"Very well. From now on, I shall be known as {new_name}."',
                  "You feel an odd sense of ceremony in the act.", sep="\n")
            self.name = new_name
            self.choices = [f"Feed {self.name}", f"Play with {self.name}", f"Throw {self.name} away", "Do nothing"]
            self.add_satisfaction(10)

        elif choice == "Do nothing":
            print(f"{self.name} grows weary at your inaction")
            self.add_satisfaction(-10)


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
          "your arm and you jerk your hand away quickly. the rock speaks again:",
          '\t"I wouldn\'t do that if I were you. You don\'t want to end up like them"',
          "As you wonder what a rock even eats, you wonder what you have gotten yourself into...\n", sep="\n")

    try:
        while True:
            day_count += 1
            print(f"Day {day_count}:\n")
            rock.show_stats()
            player_choice = show_choices(rock.choices, "What would you like to do?")

            rock.parse_choice(player_choice)

            print(f"{rock.name} grows hungier")
            rock.add_hunger(-10)
            print(f"{rock.name} grows bored")
            rock.add_satisfaction(-10)

            if rock.hunger <= 0:
                print(f"You have failed to properly care for {rock.name}. It has grown hungry, and you are its closest",
                      f"source of food. You have no time to react as you are instantly consumed by {rock.name},",
                      "who you once cared for", sep="\n")
                break

            if rock.satisfaction <= 0:
                print(f"{rock.satisfaction} has grown bored of your presence. Desperate for any enjoyment, it turns on you.",
                      "It begins laughing, and you begin to run away, but a sharp pain rings in your head.",
                      "You double over in pain, before it stops instantly as {rock.name} becomes tired of you",
                      "and consumes you, ending your suffering", sep="\n")
                break

    except KeyboardInterrupt:
        print(f"\n{rock.name} is dissapointed in you for abandoning it. Please do better next time")
    finally:
        print("Maybe you will take better care of your rock next time")


if __name__ == "__main__":
    main()
