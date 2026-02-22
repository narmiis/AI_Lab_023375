class BlockWorld:
    def __init__(self, initial_state):
        self.state = initial_state
        self.holding = None

    def is_clear(self, block):
        for b in self.state:
            if self.state[b] == block:
                return False
        return True

    def pick_up(self, block):
        if self.state[block] == "table" and self.is_clear(block):
            self.holding = block
            self.state[block] = None
            print(f"Pick up {block}")
            return True
        return False

    def put_down(self, block):
        if self.holding == block:
            self.state[block] = "table"
            self.holding = None
            print(f"Put down {block}")
            return True
        return False

    def unstack(self, block, below):
        if self.state[block] == below and self.is_clear(block):
            self.holding = block
            self.state[block] = None
            print(f"Unstack {block} from {below}")
            return True
        return False

    def stack(self, block, below):
        if self.holding == block and self.is_clear(below):
            self.state[block] = below
            self.holding = None
            print(f"Stack {block} on {below}")
            return True
        return False

    def show_state(self):
        print("Current State:")
        for block in self.state:
            print(f"{block} on {self.state[block]}")
        print("Holding:", self.holding)
        print("-" * 20)


# Example Usage
initial_state = {
    "A": "table",
    "B": "table",
    "C": "table"
}

bw = BlockWorld(initial_state)

bw.show_state()

# Goal: A on B, B on C, C on table

bw.pick_up("B")
bw.stack("B", "C")

bw.pick_up("A")
bw.stack("A", "B")

bw.show_state()
