# Conver text-based emotion into emoji

msg = input("Enter Your Message: ")

msg = msg.replace(":)", "🙂")
msg = msg.replace(":(", "😔")
msg = msg.replace(":D", "😀")
msg = msg.replace(";)", "😉")
msg = msg.replace(":}", "😍")

print(msg)
