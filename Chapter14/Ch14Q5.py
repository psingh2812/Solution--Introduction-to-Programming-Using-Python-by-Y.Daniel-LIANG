import random
def main():
    state_cap={"Washington":"Olympia","Oregon":"Salem",\
                    "California":"Sacramento","Ohio":"Columbus",\
                    "Nebraska":"Lincoln","Colorado":"Denver",\
                    "Michigan":"Lansing","Massachusetts":"Boston",\
                    "Florida":"Tallahassee","Texas":"Austin",\
                    "Oklahoma":"Oklahoma City","Hawaii":"Honolulu",\
                    "Alaska":"Juneau","Utah":"Salt Lake City",\
                    "New Mexico":"Santa Fe","North Dakota":"Bismarck",\
                    "South Dakota":"Pierre","West Virginia":"Charleston",\
                    "Virginia":"Richmond","New Jersey":"Trenton",\
                    "Minnesota":"Saint Paul","Illinois":"Springfield",\
                    "Indiana":"Indianapolis","Kentucky":"Frankfort",\
                    "Tennessee":"Nashville","Georgia":"Atlanta",\
                    "Alabama":"Montgomery","Mississippi":"Jackson",\
                    "North Carolina":"Raleigh","South Carolina":"Columbia",\
                    "Maine":"Augusta","Vermont":"Montpelier",\
                    "New Hampshire":"Concord","Connecticut":"Hartford",\
                    "Rhode Island":"Providence","Wyoming":"Cheyenne",\
                    "Montana":"Helena","Kansas":"Topeka",\
                    "Iowa":"Des Moines","Pennsylvania":"Harrisburg",\
                    "Maryland":"Annapolis","Missouri":"Jefferson City",\
                    "Arizona":"Phoenix","Nevada":"Carson City",\
                    "New York":"Albany","Wisconsin":"Madison",\
                    "Delaware":"Dover","Idaho":"Boise",\
                    "Arkansas":"Little Rock","Louisiana":"Baton Rouge"}

    incrrct_ans=[]

    print('Answer state capitals!\n\n')
  

    while len(state_cap)>0:
        choice=random.choice(list(state_cap.keys()))
        corrct_ans=state_cap.get(choice)
        
        answer = input(('What is the capital city of',choice,'?'))
        
        if answer.lower()==corrct_ans.lower():
            print("That's Correct!\n")
            del state_cap[choice]
        else:
            print("That's Incorrect.")
            print("The correct answer is",corrct_ans)
            incrrct_ans.append(choice)

    print("You missed",len(incrrct_ans),"states.\n")
    

    if incrrct_ans:
        print("here's the ones that you may want to brush up on:\n")
        for each in incrrct_ans:
            print(each)
    else:
        print("Perfect!")

        

main()
    