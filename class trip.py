
class trip:
        def __init__(self,target,length):
                self.target = target
                self.length = length
                print("go to ",target," for ",length," days")



def main():
    plan1 = trip("London", 5)
    plan2 = trip("Barcelona", 7)

if __name__ == '__main__':
    main()

