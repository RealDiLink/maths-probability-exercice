def lievre_tortue():
    import random

    moyenne_lievre = 0
    moyenne_tortue = 0

    for loop in range(100):

        lievre = 0
        tortue = 0

        for loop in range(100000):
            tortue_case = 0
            print("tortue_case est à zéro " + str(tortue_case))
            for i in range(4):
                de = random.randint(1, 6)

                print("le dé donne : " + str(de))

                if (de == 6):
                    lievre += 1
                    print("break + lievre + 1 ")
                    break
                else:
                    tortue_case += 1
                    print("tortue case + 1 ")

                if (tortue_case == 4):
                    tortue += 1
                    print("break + tortue + 1 ")
                    break

        print("le lievre a gagné : " + str(lievre) + " fois")
        print("la tortue a gagné: " + str(tortue) + " fois")

        moyenne_lievre = moyenne_lievre + lievre
        moyenne_tortue = moyenne_tortue + tortue

    moyenne_lievre = moyenne_lievre / 100
    moyenne_tortue = moyenne_tortue / 100
    print("moyenne lievre : " + str(moyenne_lievre))
    print("moyenne tortue : " + str(moyenne_tortue))

lievre_tortue()
