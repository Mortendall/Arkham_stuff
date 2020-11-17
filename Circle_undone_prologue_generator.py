import random, sys, numpy

def selectInvestigator(InvestigatorNumber):
    if InvestigatorNumber == 1:
        return("Gavrielle Mizrah")
    elif InvestigatorNumber ==2:
        return("Jerome Davids")
    elif InvestigatorNumber ==3:
        return("Penny White")
    elif InvestigatorNumber ==4:
        return("Valentino Rivas")

def selectResolution(ResolutionNumber):
    if ResolutionNumber ==1:
        return("was taken by the Watcher")
    elif ResolutionNumber ==2:
        return("was claimed by Specters")
    elif ResolutionNumber ==3:
        return("disappeared into the Mist")
    elif ResolutionNumber ==4:
        return("was pulled into the spectral realm")

def clueDiscoverer(InvestigatorCount):
    return(numpy.random.normal(loc = 3.0, scale = 1.0, size = None)*InvestigatorCount)

while True:
    print("Hello, I will generate a prologue resolution for you for the Circle Undone. Do you want to select investigators (a) or do you want me to select them for you (b)?")
    select_investigators = input()
    if select_investigators == "a":
        InvestigatorList = []
        print("OK, add one investigator at a time and finish with \"Done\"")
        while True:
            print("Enter (a) for Gavriella Mirzah, (b) for Jerome Davis, (c) for Penny White and (c) for Valentino Rivas")
            InvestigatorNumber = input()
            if InvestigatorNumber == "a":
                InvestigatorList.append("Gavriella Mizrah")
            elif InvestigatorNumber == "b":
                InvestigatorList.append("Jerome Davis")
            elif InvestigatorNumber == "c":
                InvestigatorList.append("Penny White")
            elif InvestigatorNumber == "d":
                InvestigatorList.append("Valentino Rivas")
            elif InvestigatorNumber == "Done":
                break
        break
    elif select_investigators == "b":
        print("OK, how many investigators do you want me to select?")
        PlayerCount = input()
        if int(PlayerCount) ==4:
            InvestigatorList = ["Gavriella Mizrah", "Jerome Davis", "Penny White", "Valentino Rivas"]
        else:
            Investigators = random.sample(range(1,4),int(PlayerCount))
            InvestigatorList = []
            for i in range(0,int(PlayerCount)):
                InvestigatorList.append(selectInvestigator(Investigators[i]))
        break
CluesDiscovered = round(clueDiscoverer(int(len(InvestigatorList))))
InvestigatorFates = []
for i in range(0,int(len(InvestigatorList))):
    InvestigatorFate = random.randint(1,4)
    InvestigatorFates.append(selectResolution(InvestigatorFate))
print("OK, here's your resolution")
for i in range(0,int(len(InvestigatorList))):
    print(InvestigatorList[i],InvestigatorFates[i])
print(CluesDiscovered,"pieces of evidence were left behind")
