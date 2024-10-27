# Task 3

class Message:

    # Constructor with recipient and sender
    def __init__(self, recipient, sender):
        self.recipient = recipient
        self.sender = sender
        self.messagetext = ""  # Empty message text

    # Returns senders name
    def get_sender(self):
        return self.sender

    # Returns the recipient
    def get_recipient(self):
        return self.recipient

    # Places the message to the letter, when written
    def append(self, message):
        self.messagetext = message

    # Return the formatted string, with sender, recipient and message
    def __str__(self):
        return f"From: {self.sender} \nTo: {self.recipient} \n{self.messagetext}"


# The letter, from Java to Python, with the message underneath the object
letter1 = Message("Python", "Java")
letter1.append("Hello! I've been studying your language for decades,\nand I have yet to be able to speak to "
                       "any ACTUAL pythons! What's up with that?\nAnyways, text me back, so we can go out for some "
                       "JAVA coffee.")

# Printing of the letter, with the recipient, sender and message
print(letter1)