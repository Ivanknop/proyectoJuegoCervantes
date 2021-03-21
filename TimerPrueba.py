import time
run = input("Start? > ")
seg = 0
# Only run if the user types in "start"
if run == "ok":
    # Loop until we reach 20 minutes running
    while seg != 10:
        print (">>>>>>>>>>>>>>>>>>>>>" + str(seg))
        # Sleep for a minute
        time.sleep(1)
        # Increment the minute total
        seg += 1
    # Bring up the dialog box here