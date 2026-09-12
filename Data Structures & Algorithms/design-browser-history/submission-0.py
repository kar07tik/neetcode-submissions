class BrowserHistory:

    def __init__(self, homepage: str):
        # Store history in a dynamic array
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        # Truncate forward history and append the new url
        self.curr += 1
        self.history = self.history[:self.curr]
        self.history.append(url)

    def back(self, steps: int) -> str:
        # Move back at most to index 0
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        # Move forward at most to the end of the history list
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]