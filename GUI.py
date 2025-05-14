import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class Pet:
    def __init__(self, name, hunger=5, age=0, boredom=3, sleepiness=3):
        self.dead = False
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.sleepiness = sleepiness
        self.age = age

    def feed(self):
        if self.dead: return
        self.hunger = max(0, self.hunger - 3)

    def wait(self):
        if self.dead: return
        self.age += 1
        self.sleepiness += 1
        self.hunger += 1
        self.boredom += 1

    def sleep(self):
        if self.dead: return
        self.sleepiness = max(0, self.sleepiness - 5)

    def play(self):
        if self.dead: return
        self.boredom = max(0, self.boredom - 3)

    def check_death(self):
        return self.sleepiness >= 10 or self.boredom >= 10 or self.hunger >= 10 or self.age >= 15

    def __str__(self):
        return f"{self.name} - Age: {self.age}, Hunger: {self.hunger}, Boredom: {self.boredom}, Sleepiness: {self.sleepiness}"


class VirtualPetApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Virtual Pet Game")
        self.geometry("800x600")

        self.pet = None

        self.name_label = ctk.CTkLabel(self, text="Enter your pet's name:")
        self.name_label.pack(pady=10)

        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.pack(pady=10)

        self.start_button = ctk.CTkButton(self, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.pack(pady=20)

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)

        self.feed_button = ctk.CTkButton(self.button_frame, text="Feed", command=self.feed)
        self.play_button = ctk.CTkButton(self.button_frame, text="Play", command=self.play)
        self.sleep_button = ctk.CTkButton(self.button_frame, text="Sleep", command=self.sleep)
        self.wait_button = ctk.CTkButton(self.button_frame, text="Wait", command=self.wait)

        self.toggle_action_buttons("disable")

    def start_game(self):
        name = self.name_entry.get()
        if name:
            self.pet = Pet(name)
            self.update_status()
            self.toggle_action_buttons("enable")

    def update_status(self):
        if self.pet.check_death():
            self.status_label.configure(text=f"{self.pet.name} has died.\n💀 R.I.P 💀")
            self.toggle_action_buttons("disable")
        else:
            self.status_label.configure(text=str(self.pet))

    def toggle_action_buttons(self, state):
        for button in [self.feed_button, self.play_button, self.sleep_button, self.wait_button]:
            if state == "disable":
                button.pack_forget()
            else:
                button.pack(pady=5, fill='x')

    def feed(self):
        self.pet.feed()
        self.update_status()

    def play(self):
        self.pet.play()
        self.update_status()

    def sleep(self):
        self.pet.sleep()
        self.update_status()

    def wait(self):
        self.pet.wait()
        self.update_status()


if __name__ == "__main__":
    app = VirtualPetApp()
    app.mainloop()
