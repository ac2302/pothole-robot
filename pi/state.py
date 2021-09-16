class State:
    manual, speed, curve = [False, 0, 0]

    def __str__(self):
        return f"manual: {self.manual}\nspeed: {self.speed}\ncurve: {self.curve}\n\n"
