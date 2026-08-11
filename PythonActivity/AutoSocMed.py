action_state = ["CRITICAL DISPATCH", "MONITORING", "SYSTEM IGNORE"]

post_text = input("Social Media Post: ")
post_text = post_text.lower()

if "system check" in post_text or "luis" not in post_text:
    print(action_state[2])
elif ("baha" in post_text or "rescue" in post_text) and "test" not in post_text and "fake" not in post_text:
    print(action_state[0])
elif "luis" in post_text:
    print(action_state[1])

