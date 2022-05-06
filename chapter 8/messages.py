def show_messages(messages):
    """Prints all the messages in a list of messages"""
    for message in messages:
        print(str(message))
def send_messages(messages, sent_messages):
    while messages:
        sent_message = messages.pop()
        sent_messages.append(sent_message)




short_msgs = ["Keep up the good work! ",
              "Now's the time to give it everything you've got! ",
              "You're doing great!",
              "Walk away with no regrets!",]
sent_messages = []
show_messages(short_msgs)
send_messages(short_msgs[:],sent_messages)
print(short_msgs)
print(sent_messages)