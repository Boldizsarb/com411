def cross_bridge (steps):
    #display each step
    for step in range (steps):
        print ("Crossed step.")

    if steps > 5:
        print("the bridge is collapsing!")
    else:
        print("We must keep going!")

cross_bridge(3)
cross_bridge(7)
