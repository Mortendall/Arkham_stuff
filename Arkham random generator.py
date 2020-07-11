import random,sys

def getCampaign(CampaignNumber):
    if CampaignNumber == 1:
        return "Night of the Zealot"
    elif CampaignNumber == 2:
        return "Dunwich Legacy"
    elif CampaignNumber == 3:
        return "The Path to Carcosa"
    elif CampaignNumber == 4:
        return "The Forgotten Age"
    elif CampaignNumber == 5:
        return "The Circle Undone"
    elif CampaignNumber == 6:
        return "The Dream-Eaters"

def getInvestigator(InvestigatorNumber):
    if InvestigatorNumber == 1:
        return "Agnes"
    elif InvestigatorNumber == 2:
        return "Akachi"
    elif InvestigatorNumber == 3:
        return "Amanda Sharp"
    elif InvestigatorNumber == 4:
        return "Duke"
    elif InvestigatorNumber == 5:
        return "Calvin"
    elif InvestigatorNumber == 6:
        return "Carolyn"
    elif InvestigatorNumber == 7:
        return "Daisy"
    elif InvestigatorNumber == 8:
        return "Dexter"
    elif InvestigatorNumber == 9:
        return "Diana"
    elif InvestigatorNumber == 10:
        return "Father Mateo"
    elif InvestigatorNumber == 11:
        return "Finn"
    elif InvestigatorNumber == 12:
        return "Harvey Walters"
    elif InvestigatorNumber == 13:
        return "Jacquelin Fine"
    elif InvestigatorNumber == 14:
        return "Jenny"
    elif InvestigatorNumber == 15:
        return "Jim Culver"
    elif InvestigatorNumber == 16:
        return "Joe Diamond"
    elif InvestigatorNumber == 17:
        return "Leo Anderson"
    elif InvestigatorNumber == 18:
        return "Lola"
    elif InvestigatorNumber == 19:
        return "Luke"
    elif InvestigatorNumber == 20:
        return "Mandy"
    elif InvestigatorNumber == 21:
        return "Marie Lambeau"
    elif InvestigatorNumber == 22:
        return "Mark Harrigan"
    elif InvestigatorNumber == 23:
        return "Minh"
    elif InvestigatorNumber == 24:
        return "Nathaniel Cho"
    elif InvestigatorNumber == 25:
        return "Norman Withers"
    elif InvestigatorNumber == 26:
        return "Patrice"
    elif InvestigatorNumber == 27:
        return "Preston"
    elif InvestigatorNumber == 28:
        return "Rex Murphy"
    elif InvestigatorNumber == 29:
        return "Rita Young"
    elif InvestigatorNumber == 30:
        return "Roland Banks"
    elif InvestigatorNumber == 31:
        return "Sefina"
    elif InvestigatorNumber == 32:
        return "Silas"
    elif InvestigatorNumber == 33:
        return "Sister Mary"
    elif InvestigatorNumber == 34:
        return "Skids"
    elif InvestigatorNumber == 35:
        return "Stella"
    elif InvestigatorNumber == 36:
        return "Tommy"
    elif InvestigatorNumber == 37:
        return "Tony"
    elif InvestigatorNumber == 38:
        return "Ursula"
    elif InvestigatorNumber == 39:
        return "Wendy"
    elif InvestigatorNumber == 40:
        return "Winnifred"
    elif InvestigatorNumber == 41:
        return "Yorick"
    elif InvestigatorNumber == 42:
        return "Zoey"


while True:
    print("Hello, would you like me to select a campaign for you? (y)es or (n)o?")
    campaign = input()
    if campaign == "y":
        CampaignNumber = random.randint(1,6)
        Campaign = getCampaign(CampaignNumber)
        print("You should play ",Campaign,". How many investigators do you want me to select, 1, 2, 3, or 4?")
        break
    elif campaign == "n":
        print("OK, how many investigators do you want me to select, 1, 2, 3, or 4?")
        break
while True:
    Investigators = input()
    if int(Investigators)== 1:
        InvestigatorNumber = random.randint(1,42)
        Investigator = getInvestigator(InvestigatorNumber)
        print("You should play ",Investigator)
    elif int(Investigators) == 2:
        InvestigatorNumber1 = random.randint(1,42)
        Investigator1 = getInvestigator(InvestigatorNumber1)
        InvestigatorNumber2 = random.randint(1,42)
        Investigator2 = getInvestigator(InvestigatorNumber2)
        print("You should play ",Investigator1," and ", Investigator2)
    elif int(Investigators) == 3:
        InvestigatorNumber1 = random.randint(1,42)
        Investigator1 = getInvestigator(InvestigatorNumber1)
        InvestigatorNumber2 = random.randint(1,42)
        Investigator2 = getInvestigator(InvestigatorNumber2)
        InvestigatorNumber3 = random.randint(1,42)
        Investigator3 = getInvestigator(InvestigatorNumber3)
        print("You should play ",Investigator1,", ", Investigator2," and ", Investigator3)
    elif int(Investigators) == 4:
        InvestigatorNumber1 = random.randint(1,42)
        Investigator1 = getInvestigator(InvestigatorNumber1)
        InvestigatorNumber2 = random.randint(1,42)
        Investigator2 = getInvestigator(InvestigatorNumber2)
        InvestigatorNumber3 = random.randint(1,42)
        Investigator3 = getInvestigator(InvestigatorNumber3)
        InvestigatorNumber4 = random.randint(1,42)
        Investigator4 = getInvestigator(InvestigatorNumber4)
        print("You should play ",Investigator1,", ", Investigator2,", ", Investigator3," and ", Investigator4)
