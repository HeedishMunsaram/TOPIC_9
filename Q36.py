message = "This is a list of cities."

message_list = message.split()

for word in message_list:
    print(word)

new_message = " ".join(message_list)
print(new_message)