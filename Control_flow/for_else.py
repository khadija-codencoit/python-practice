success = False

for i in range(3):
    print("Attempt")
    if success:
        print("success")
        break
else:
    print("Stop")