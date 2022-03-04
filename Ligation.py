class Ligation:
    # First find if sticky or blunt ends.
    sticky_or_blunt = input("Are you ligating sticky or blunt ends?: ")
    if sticky_or_blunt == "sticky":
        backbone_to_insert_ratio = 0.3333 # 1:3 ratio
    if sticky_or_blunt == "blunt":
        backbone_to_insert_ratio = 0.2 #1:5 ratio
    kB_of_insert = float(input("How many kB of insert are there?: "))
    kB_of_backbone = float(input("How many kB of backbone are there?: "))

    insert_concentration = float(input("What's the nanodrop concentration for the insert in ng/uL?: "))
    backbone_concentration = float(input("What's the nanodrop concentration for the backbone in ng/uL?: "))

    x = 100 * kB_of_insert
    y = x / kB_of_backbone
    ng_insert = y / backbone_to_insert_ratio

    #Finding the volume of insert
    volume_of_insert = ng_insert / insert_concentration

    # Finding volume of backbone
    volume_of_backbone = 100 / backbone_concentration # 100 bc 100 ng always used

    volume_of_water = 10 - volume_of_insert + volume_of_backbone + 2
    print(" ")
    print("You are using " + str(ng_insert) + "ng of insert")
    print(" ")
    print("Volumes to use in the ligation: ")
    print(" ")
    print("Insert: " + ":\t\t" + str(volume_of_insert) + "uL")
    print("Backbone: " + ":\t\t" + str(volume_of_backbone) + "uL")
    print("Water: " + ":\t\t" + str(volume_of_water) + "uL")
    print("Ligase Buffer:" + ":\t\t" "1uL")
    print("Ligase: " + ":\t\t" + "1uL")
    print(" ")
    print("Total: " + ":\t\t" + "10uL")
    print(" ")
