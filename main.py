from pygame import * 
init()
size = width, height = 800, 500 #Establishing screen dimensions
screen = display.set_mode(size)
button = 0 #button is a variable that keeps track of it the user is pressing a button
BLACK = (0, 0, 0)
WHITE= (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0,255)
myFont = font.SysFont("Times New Roman",20) #creating font
myFont2 = font.SysFont("Times New Roman",10)
MAINPAGE = 0 #MAINPAGE, VIEW,MODIFY etc. are the states, which represent the different pages
VIEW = 1
MODIFY = 2
ADD = 3
REMOVE = 4
REPORTS = 5
REPORT1 = 6
REPORT2 = 7
REPORT3 = 8
QUITCOMMAND = 9
countTable = 0 #countTable is a variable that changes from 0 to 1 depending on how we want the table to be drawn. If countTable is 0 we will draw a white background that takes up the dimensions of the screen, otherwise if it is greater than 0, we will always draw the table white background with smaller dimensions, so that it does not go over the text that the user is entering. We will draw the full background once, when the user first moves to a new state and then as the table refreshes we will use the smaller dimensions of the background so the text is visible.
step = 1 #step decides what step of the modification/addition/removing the user is on
change = "" #change is the variable which stores what the user wants to change when they are modifying
removeID = "" #removeID is the variable which stores what the user wants to remove when they are removing
textAllowed = True #this variable is True if the user is allowed to enter text and false if they are not
addList = [] #this is a list with all the fields that the user adds, which then act as one record in this list. This list can then be added to the file
addVar = "" #this variable is a variable which stores what field the user wants to add
maximum = 6 #this variable is to control the maximum character length (stars off as 6 characters)
ID = "" #this variable stores the ID that the user wants to change
field = "" #this variable stores the field that the user wants to change
textDisplayList= [] #this variable holds the text that the user is entering
KEY_pressed = False #this variable is True if a key is being pressed and vice versa
KEY_backspace = False #this variable is True if a backspace has been pressed and vice versa
enter = 0 #if this variable is 0 than that means that the enter button has not been pressed, if it is 1, than that means that it has been pressed
def quitCommand(currentState,mx,my,button): #runs if the user presses the end button
  exit() #exits out of the program
def mainPage(currentState, mx, my, button): #drawing the main page
  draw.rect(screen,WHITE,(0,0,800,600)) #draws background
  drawBoxes(325,345,100,"View Data") #drawing buttons
  drawBoxes(325,340,175,"Modify Data")
  drawBoxes(325,350,250,"Add Data")
  drawBoxes(325,335,325,"Remove Data")
  drawBoxes(325,335,400, "See Reports")
  drawBoxes(625,665,25,"END")
  text = myFont.render("Data for FIFA teams", 1, (255, 0, 0)) 
  screen.blit(text,(295,25,25,10))	
  if button == 1: #if the user is pressing down
     #checking the mouse coordinates of the user when mouse is down
    if 325<mx<475 and 100<my<150: 
      button = 0
      currentState = VIEW
      #if the mouse is in the range of the view button than go to view page
    elif 325<mx<475 and 175<my<225:
      button = 0
      currentState = MODIFY
      #if the mouse is in the range of the modify button than go to modify page
    elif 325<mx<475 and 250<my<300:
      button = 0
      currentState = ADD
      #if the mouse is in the range of the add button than go to the add page 
    elif 325<mx<475 and 325<my<375:
      button = 0
      currentState = REMOVE
      #if the mouse is in the range of the remove button than go to the remove page
    elif 325<mx<475 and 400<my<500:
      button = 0
      currentState = REPORTS
      #if the mouse is in the range of the reports button than go to the reports page
    elif 625<mx<775 and 25<my<75:
      button = 0
      currentState = QUITCOMMAND
      #if the mouse is in the range of the quit button than go to the quit page
  return currentState #return the new state, if the user has not pressed any buttons, than it will stay at the main page 
def view(currentState,mx,my,button): #view state
  global textAllowed
  textAllowed = False #not allowing text to be inputted
  draw.rect(screen,WHITE,(0,0,800,100)) #drawing background
  draw.rect(screen,BLUE,(625,400,150,50)) #drawing text box
  drawTextSimple("BACK", 665,410) #drawing back button
  drawTable() #drawing table
  return currentState #returning state
def modify(currentState,mx,my,button): #modify state
  global enter
  global countTable
  draw.rect(screen,WHITE,(0,0,800,100)) 
  draw.rect(screen, BLACK,(100,300,400,100),10)
  draw.rect(screen,BLUE,(625,400,150,50)) #drawing text box
  drawTextSimple("BACK", 665,410) #drawing back button
  if step == 1: #if it is the first input than display enter ID, because that is the first input the user needs to do, regardless of if it is modify, add or remove
    drawTextSimple("Enter ID",80,255)
  drawTable()
  # keyCheck()
  if enter == 1: #if the the enter button has been pressed
    program("1") #run the main program and passing parameter "1", which means that the program will run the modify code 
    enter = 0 #change enter back to 0 because the enter button has already been pressed and registered
  return currentState 
def add(currentState,mx,my,button): #add state
  global enter
  draw.rect(screen,WHITE,(0,0,800,100))
  draw.rect(screen, BLACK,(100,300,400,100),10)
  draw.rect(screen,BLUE,(625,400,150,50)) #drawing text box
  drawTextSimple("BACK", 665,410) #drawing back button
  if step == 1:
    drawTextSimple("Enter ID",80,255)
  drawTable()
  if enter == 1:#if the enter button has been pressed
    program("2") #run the main program and passing parameter "2", which means that the program will run the add code
    enter = 0
  return currentState
def remove(currentState,mx,my,button): #remove state
  global enter
  draw.rect(screen,WHITE,(0,0,800,100))
  draw.rect(screen, BLACK,(100,300,400,100),10)
  draw.rect(screen,BLUE,(625,400,150,50)) #drawing text box
  drawTextSimple("BACK", 665,410) #drawing back button
  if step == 1:
    drawTextSimple("Enter ID",80,255)
  drawTable()
  if enter == 1:
    program("3")#run the main program and passing parameter "3", which means that the program will run the remove code
    enter = 0
  return currentState
def reports(currentState,mx,my,button): #reports state
  draw.rect(screen,WHITE,(0,0,800,500))
  draw.rect(screen,BLUE,(625,400,150,50)) #drawing text box
  drawTextSimple("BACK", 665,410) #drawing back button
  drawBoxes(325,345,100,"report1") #draw the buttons to see the specific reports
  drawBoxes(325,350,175,"report2")
  drawBoxes(325,335,250, "report3")
  if button == 1: #if the mouse is down
    #checking to see where the mouse coordinates are and going to the appropriate state (based on what button the mouse coordinates coincide with)
    if 325<mx<475 and 100<my<150:  
      currentState = REPORT1 #first report
    elif 325<mx<475 and 175<my<225:
      currentState = REPORT2 #seocond report
    elif 325<mx<475 and 250<my<300:
      currentState = REPORT3 #third report
  return currentState
def report1(currentState,mx,my,button): #first report
  global recordsList
  print("record1")
  draw.rect(screen,WHITE,(0,0,800,600))
  draw.rect(screen,BLUE,(625,400,150,50)) #drawing text box
  drawTextSimple("BACK", 665,410) #drawing back button
  reportY = 50 #making a variable for the y position
  drawText(myFont,"Teams who are in the round of 16",100,20,100,100) #show the first report
  for i in range(len(recordsList)): #going through all the records
    if (recordsList[i])[5] == "True":  #if the in round of 16? field is true
      #note: i represents each individual record and i[5] represents the 6th field of the record which is the in round of 16? field
      drawText(myFont,recordsList[i][1],100,reportY,100,100) #than print out that team specifically (print the record at 1, because index one is the team), because that team is in the round of 16 and that is what the report is generating. draw it at the reportY position
      reportY+=20 #change the y position so that the next team printed goes on a new line
def report2(currentState,mx,my,button): #second report
  global recordsList
  draw.rect(screen,WHITE,(0,0,800,600))
  draw.rect(screen,BLUE,(625,400,150,50)) #drawing text box
  drawTextSimple("BACK", 665,410) #drawing back button
  reportY = 50
  drawText(myFont,"Teams in the top 15 (ranking)",100,20,100,100) #show the second record
  for i in range(len(recordsList)): #going through the list of all records
    if int((recordsList[i])[2]) <= 15: #checking to see if a teams ranking is 15 or less
      drawText(myFont,recordsList[i][1],100,reportY,100,100) #if so print the team that has that ranking (field 2) 
      reportY+=20 #move to a new line
def report3(currentState,mx,my,button): #third record
  global recordsList
  draw.rect(screen,WHITE,(0,0,800,600))
  draw.rect(screen,BLUE,(625,400,150,50)) #drawing text box
  drawTextSimple("BACK", 665,410) #drawing back button
  reportY = 50
  drawText(myFont,"Teams with more than 100 total world cup goals",100,20,100,100) #show the second record
  for i in range(len(recordsList)):
    if int((recordsList[i])[4]) > 100: #if the 5th field, which is the world cup goals is greater than 100:
      drawText(myFont,recordsList[i][1],100,reportY,100,100) #than print the team that has more than 100 total World Cup Goals
      reportY+=20   #move to a new line
def drawTextSimple(text,rectX,rectY): #function to draw simple text with less parameters than "drawText()"
  text = myFont.render(text, 1, (255,0,0)) #the parameter text is the text that is going to be displayed
  screen.blit(text,(rectX,rectY,200,50))  #display the text 
def drawTable():#function to draw the table
  global textDisplayVar
  global countTable
  global recordsList
  if countTable == 0: #if countTable == 0. countTable is 0 when the page is first being opened
    draw.rect(screen, WHITE, (0,0,800,500)) #draw a white background that takes up the whole screen

    
    countTable+=1 #increase countTable by 1 because the page has already been opened and now we do not want to draw the whole white background because otherwise it will cover the text
  else:
    draw.rect(screen, WHITE, (0,0,800,200)) #if it is not the first time that the table is being drawn than we can draw a smaller rectangle so it does not cover the text. The first time we do want to draw it such that it covers the whole screen because we dont objects from other screens to still be there even when we are on a new screen.
  j = 0 #j is a variable 
  xPosText = 20 #this is the xPosition of the text
  yPosText = 20#this is the y position of the text
  #draw the titles
  drawText(myFont2,"ID            Team                                                             Ranking   Best Player                                                  World Cup Goals   in round of 16?",20,10,100,10) 
  for i in range(len(recordsList)): #going through recordsList
    for j in range(1):
      drawText(myFont2,recordsList[i][0],xPosText,yPosText,7,50) #draw the first field of the first record
      xPosText+=50 #increase xPosText by 50 so we can have enough spacing between the first field and the second field
      drawText(myFont2,recordsList[i][1],xPosText,yPosText,20,50)
      xPosText+=210
      #the amount we increase xPosText by depends on the maximum character length of each field
      drawText(myFont2,recordsList[i][2],xPosText,yPosText,4,50)
      xPosText+=50
      drawText(myFont2,recordsList[i][3],xPosText,yPosText,21,50)
      xPosText+=210
      drawText(myFont2,recordsList[i][4],xPosText,yPosText,4,50)
      xPosText+=90
      drawText(myFont2,recordsList[i][5],xPosText,yPosText,6,50)
    yPosText+=10 #move on to the next line (new record)
    xPosText = 20 #reset the x value
def drawBoxes(box_xPos,xPos,yPos,text): #function to draw the boxes
  #parameters (listed in order) are the x position of the box, the x position of the text, the y position of the text and the actual text 
  draw.rect(screen, BLUE, (box_xPos,yPos,150,50)) #draw the box with the parameters; customizable x position of box and y position of box
  drawText(myFont,text,xPos,yPos,150,50) #draw the text, at the same y position as the box but at a customizable x position
def drawText(font,text,xPos,yPos,rectX,rectY): #function to draw text (not simple)
  text = font.render(text, 1, (255,0,0))
  screen.blit(text,(xPos,yPos+10,150,50)) #display text
def keyInput(): #variable to display the key that the user has entered
    global xPos_textInput
    global KEY_backspace
    global textAllowed
    global textDisplayList

    global e
    global KEY_pressed
    if textAllowed == True: #if the user is allowed to enter text
      yPos = 335 #y position variable
      if KEY_backspace == True: #if backspace is pressed
        if xPos_textInput >= 135: #if the x position of the text is greater than 135 than backspace can happen, otherwise that means that you are already at the leftmost you can be at the box, because 135 is the leftmost position. Thus, you can not go back more and should not be allowed to.
          draw.rect(screen,WHITE,(xPos_textInput-15,yPos,40,50)) #draw a rectangle to cover up the text. Draw the rectangle at the y position of the text, and 15 to the left from the position of the character (because the character has a width)
          xPos_textInput-=15 #decrease the x position by 15, because the next character drawn will be be before the character that was deleted
          KEY_backspace = False #the backspace has just been pressed so it is not being pressed anymore
          del textDisplayList[-1] #delete the last element from the list of the characters that the user has inputted in the program because it has been deleted (that is the function of a backspace) 
        KEY_backspace = False #the user has already pressed the backspace so make it false now
      if KEY_pressed == True: #if a key is being pressed
        if e.unicode!= "\x08" and e.unicode!= "\r": #if the character entered is not enter or backspace than execute the following code. the user can not enter those because those are special keys that we have seperate code for
          drawTextSimple(e.unicode,xPos_textInput,yPos) #draw the character that the user has typed in at xPos_textInput 
          if e.key == K_LSHIFT or e.key == K_RSHIFT: #if shift is pressed
            xPos_textInput+=0 #do not change the x position because by default shift adds a space so we are making sure that does not happen
          else:
            xPos_textInput+=15 #otherwise, increase the x position becasue we are moving on to a new character
            textDisplayList.append(e.unicode) #add the key that they entered to a list of the current keys they have entered (the text that is displayed on the screen)
          KEY_pressed = False #make KEY_pressed false because they have just pressed it
def read(dataFile): #Reading the data file
  global textDisplayVar
  global fileInformation 
  global textDisplayVar
  file = open(dataFile, "r") #Opening the data file as a read only, the variable dataFile is a local variable which we will replace with the file name when we call the function.
  fileInformation = [] #creating a list to store data in
  textDisplayVar = ""
  while True:
      text = file.readline() #reads each line of data file
      text = text.rstrip("\n") #removes the backslash n
      if text=="": #if there is nothing on the line, than that means that there is no more data to be read, so break out of the loop. We are done reading the file
          break
      values = text.split(",") #make a list with the different fields of the records as seperate elements, by using the split method, which splits the data fields through the commas that are seperating them
      for i in range(len(values)):
        fileInformation.append(values[i]) #go through all of the individual fields of our data and append them to our list
      # print("%-6s  %-20s %-3s\t  %-20s  %-3s\t\t\t\t %-5s" %(values[0], values[1], values[2], values[3], values[4], values[5]))
      textDisplayVar+="%-6s  %-20s %-3s\t  %-20s  %-3s\t\t\t\t %-5s" %(values[0], values[1], values[2], values[3], values[4], values[5])
    #print all the fields in one record, with field spacing
  file.close() #closing the file; 
def formattedList(): #creating our formatted multidimensional lsit
  global recordsList
  recordsList = [] #the multidimensional list is called recordsList
  count = 6 #we have a variable count which is 6
  for i in range(len(fileInformation)//6): #going through the length of the unformattedList/2
    record = [] #1  #setting an empty list for record which represents the information in one record
    for j in range(count-6,count): #going through 6 elements in the unformatted list and putting them into one record
      record.append(fileInformation[j])
    count+=6 #increasing count so that we can go through the next 6
    recordsList.append(record) #adding that record to our multi dimensional list
  return recordsList #returning our final recordsList, which a list containing all the records
def userPrompt(message): #function to prompt the user to enter a command
  print(message) #print out the message they want the user to see
  inputVar = input("Enter command:") #inputVar = the users input
  return inputVar #return inputVar
def write(dataFile): #writing our final formatted list back to the file
  global recordsList
  file = open(dataFile, "w") #opening the file once again except as a write
  count = 0 #creating a variable
  for i in range(len(recordsList)): #going through each record in the table
    for j in range(len(recordsList[i])): #going through each field in each record
      if j > 0: #if the field number is any field besides the first than add a comma, becasue we want a comma before every field, except for the first one
        file.write(",") #writing a comma to the data file so that we have something that we can identify in order to split our information into individuals fields when reading the data
      file.write((recordsList[i])[j]) #writing each individual field to the file with the raw data until we have finished writing one record
    file.write("\n") #adding a back slash so that we move to a new line and start on the second record
  file.close() #closing the file, we are done writing
def displayInfo():
  global fileInformation
  global recordsList
  # print("ID\t\tTeam\t\t\t\t Ranking  Best Player\t\t\tWorld Cup Goals  in round of 16?") #printing the headings for the information
  read("info.dat") #calling the read function. storing the unformatted list
    #into a list called "fileInformation"
  recordsList = formattedList() #formatting file Information (by calling function) into a multidimensional list and storing the returned value (recordsList) into a list called recordsList.
def program(function): #the main program
  global ID
  global textDisplayList
  global enter
  global countEnter
  global field
  global change
  global step
  global recordsList
  global maximum
  global textAllowed
  global addList
  global addVar
  global recordsList
  global removeID
  while True: #putting everyting in a while loop so the program keeps on running after the user has executed it once
    if function == "0":
      print("") 
    elif function == "1": #if the user presses 1 then do the following code:
      if step == 1: #if the user is on the first step on the input
        maximum = 20 #set the maximum value
        ID = ""
        IDcount = 0 #set IDcount to 0. 
        # while True:
        for i in range(len(textDisplayList)):
          ID+=textDisplayList[i] #add all of what the user has entered into the variable ID
        print(ID)
        for i in range(len(recordsList)): #going through all ther records
          if str(recordsList[i][0]) == ID:#if the first field of a record (which is the ID) is the same as what the user entered 
            IDcount +=1 #increase IDcount by 1 
        if IDcount == 0: #if by the end of the loop IDcount == 0, that means that the ID that the user entered is not in the data      
          drawTextSimple("That ID does not exist", 210,275)
          #error message
          enter = 0 #set enter to 0, because the user has just inputted the enter button
          ID = ""
          break
        else: #If there is no invalid input
          #Invalid Input cover
          draw.rect(screen, WHITE, (210,275,400,20)) #draw a white box over the invalid input so that we can display another one in the future
          #Enter a heading cover
          draw.rect(screen, WHITE,(80,250,300,30)) #drawing a white box over the user prompt so that we can draw a new one
          drawTextSimple("Enter heading",80,255) 
          enter = 0
          step+=1 #increase step by 1 and break so that when they exit the loop, go through the rest of the program and then come back to this loop they now go through the second step
          break   #break from the loop
      elif step == 2: #if the user is on the second step
        if enter == 1: #if enter is pressed
          for i in range(len(textDisplayList)):
            field += textDisplayList[i] #adding the users key inputs to field
          #setting the maximum character length depending on what the field is
          if field.lower() == "id":
            maximum = 6 
          elif field.lower() == "team":
            maximum = 20
          elif field.lower() == "ranking":
            maximum = 3
          elif field.lower() == "best player":
            maximum = 20
          elif field.lower() == "world cup goals":
            maximum = 3
          elif field.lower() == "in round of 16?":
            maximum = 5
          if field.lower()!="team" and field.lower()!="id" and field.lower()!="ranking" and field.lower()!="best player" and field.lower()!="world cup goals" and field!= "in round of 16?": #if the field does not match one of the headings then give an error message
            drawTextSimple("Invalid Heading", 210,275)
            field = "" #reset the field and break because they are going to come back to the loop and have to re enter their input
            break
          else:
            #if there is no invalid input
            draw.rect(screen, WHITE, (210,275,400,20)) 
            draw.rect(screen, WHITE,(80,250,300,30))
            drawTextSimple("Enter your change",80,255)
            enter = 0
            step+=1
            break
        else:
          break   
      elif step == 3:
        if enter == 1:
          for i in range(len(textDisplayList)):
            change+=textDisplayList[i]
          print(change)
          if field.lower() == "id":  #if they want to change the ID:
            IDcount = 0 #setting ID count to 0 again
            for i in range(len(recordsList)):
              if recordsList[i][0] == change: #going through the list and increasing IDcount by 1 everytime there is an ID that matches the one that the user wants to add (because the user is changing one ID to another)
                IDcount +=1
            if change.isdigit() == False:
              print("The ID must be a number (positive integer).")
              drawTextSimple("The ID must be a number (positive integer).", 210,275)
              #if the ID they want to add is not a number than give an error. ID must be a number
            elif len(change) > 6:
              print("The ID length must be 6 characters or less.")
              #If the length is more than 6 characters than give an error
            elif IDcount > 0:
              print("That ID already exists.")
              drawTextSimple("ID already exists", 210,275)
              #if IDcount is greater than 0, than that meanst that the ID that they want to add already exists, thus we give an error.      
            else:
              draw.rect(screen, WHITE, (210,275,400,20))
          elif field.lower() == "team": #if they want to change the team
            if len(change) > 20: #ensuring that their input length is not more than 20 characters
              print("The Team name length must be 20 characters or less.")
              change = ""
              enter = 0
              break
            elif "," in change:
              print("A comma is an invalid character.")
              drawTextSimple("comma is an invalid character.", 210,275)
              change = ""
              enter = 0
              break
            else:
              draw.rect(screen, WHITE, (210,275,400,20))
          elif field.lower() == "ranking":
            if change.isdigit() == False: #making sure they add a number
              print("The team ranking must be a number (positive integer).")
              drawTextSimple("must be a number (positive integer)", 210,275)
              change = ""
              enter = 0
              break
            elif len(change) > 3: #making sure that the ranking length is 3 characters or less
              print("The ranking length must be 3 characters or less.")
              change = ""
              enter = 0
              break
            else:
              draw.rect(screen, WHITE, (210,275,400,20))
          elif field.lower() == "best player":
            if len(change) > 20:
              print("The Best Player must be 20 characters or less.")
              change = ""
              enter = 0
              break
            elif "," in change:
              print("A comma is an invalid character.")
              drawTextSimple("comma is an invalid character.", 210,275)
              change = ""
              enter = 0
              break
            else:
              draw.rect(screen, WHITE, (210,275,400,20))
          elif field.lower() == "world cup goals":
            if change.isdigit() == False:
              drawTextSimple("must be a number (positive integer)", 210,275)
              change = ""
              enter = 0
              break
            elif len(change) > 3:
              print("The World Cup Goals length must be 3 characters or less.")
              change = ""
              enter = 0
              break
            else:
              draw.rect(screen, WHITE, (210,275,400,20))
          elif field.lower() == "in round of 16?":
            if change.lower()!="true" and change.lower()!="false": #if the user is not entering a boolean than give them an error message
              print("Enter a boolean.")
              drawTextSimple("Enter a boolean", 210,275)
              change = ""
              enter = 0
              break
            else:
              draw.rect(screen, WHITE, (210,275,400,20))
              change = change.lower() #we want the boolean value that they entered to be capitalized so we make it lower case and then capitalize it
              change = change.capitalize()
        else:
          break
        for i in range(len(recordsList)):
          if (recordsList[i])[0] == ID:#accessing the record which the ID that they entered
            if field.lower() == "id":
              (recordsList[i])[0] = change #adding their wanted change to the appropriate place in the record depending on the field.        textAllowed = False
              textAllowed = False #they have finished their input so they are not allowed to enter text anymore
              enter = 0 #resetting enter so that we can perform a function once they press enter again
              step = 1 #set step back to 1, because the next time they want to perform something, we want them to start from the beginning of the input
              #reset the variables for the next time they modify
              #Also reset the characters that the user has inputted
              ID = "" 
              change = ""
              field = ""
              textDisplayList=[]
              draw.rect(screen, WHITE,(80,250,300,30))
              drawTextSimple("Completed.",80,255)
              write("info.dat") 
              break #break becuase we are done
            elif field.lower() == "team":
              (recordsList[i])[1] = change
              textAllowed = False
              enter = 0
              ID = ""
              change = ""
              field = ""
              textDisplayList= []
              draw.rect(screen, WHITE,(80,250,300,30))
              drawTextSimple("Completed.",80,255)
              write("info.dat")
              break
            elif field.lower() == "ranking":
              (recordsList[i])[2] = change
              textAllowed = False
              enter = 0
              ID = ""
              change = ""
              field = ""
              textDisplayList= []
              draw.rect(screen, WHITE,(80,250,300,30))
              drawTextSimple("Completed.",80,255)
              write("info.dat") 
              break
            elif field.lower() == "best player":
              (recordsList[i])[3] = change
              textAllowed = False
              enter = 0
              ID = ""
              change = ""
              field = ""
              textDisplayList= []
              draw.rect(screen, WHITE,(80,250,300,30))
              drawTextSimple("Completed.",80,255)
              write("info.dat") 
              break
            elif field.lower() == "world cup goals":
              (recordsList[i])[4] = change
              textAllowed = False
              enter = 0
              ID = ""
              change = ""
              field = ""
              textDisplayList= []
              draw.rect(screen, WHITE,(80,250,300,30))
              drawTextSimple("Completed.",80,255)
              write("info.dat") #added
              break
            elif field.lower() == "in round of 16?":
              (recordsList[i])[5] = change
              textAllowed = False
              enter = 0
              ID = ""
              change = ""
              field = ""
              textDisplayList = []
              draw.rect(screen, WHITE,(80,250,300,30))
              drawTextSimple("Completed",80,255)
              write("info.dat")  #writing to the file because we want to add the new changes to the file
              break
    elif function == "2": #if the user enters 2
      if step == 1: #if the user is on the first step
        maximum = 6 #set the maximum character length
        IDcount = 0 
        for i in range(len(textDisplayList)):
          addVar+=textDisplayList[i] #addVar is the variable that stores what the user has entered for a field. We will later reset addVar so that it can be used for the next field that the user is adding.
        for i in range(len(recordsList)):
          if recordsList[i][0] == addVar:
            IDcount +=1 #similar method to modifying data
        print(addVar)
        if addVar.isdigit() == False:
          drawTextSimple("The ID must be a number (positive integer).", 210,275)
          print("The ID must be a number (positive integer).")
          addVar = ""
          break
        elif len(addVar) > 6:
          print("The ID length must be 6 characters or less.")
          addVar = ""
          break
        elif IDcount > 0:
          drawTextSimple("That ID already exists.", 210,275)
          print("That ID already exists.") #if the ID that they want to a dd is already in the data then that means it already exists    
          addVar = ""
          break
        else:
          print("success")
          draw.rect(screen, WHITE,(80,250,300,30))
          drawTextSimple("Enter the team",80,255)
          draw.rect(screen, WHITE, (210,275,700,25))
          addList.append(addVar) #if there are no errors than add their input to addList (we are forming a record)
          addVar = "" #Resetting the variable
          step +=1
          maximum = 20
          break
      elif step == 2:
        for i in range(len(textDisplayList)):
          addVar+=textDisplayList[i]
        if len(addVar) > 20:
          print("The name of the team must be 20 characters or less.")
          addVar = ""
          break
        elif "," in addVar:
          print("A comma is an invalid character.")
          drawTextSimple("comma is an invalid character.", 210,275)
          addVar = ""
          break
        else:
          draw.rect(screen, WHITE,(80,250,300,30))
          drawTextSimple("Enter the ranking",80,255)
          draw.rect(screen, WHITE, (210,275,700,25))
          addList.append(addVar) #adding team to add list
          addVar = ""
          step+=1
          maximum = 3
          break
      elif step == 3:
        for i in range(len(textDisplayList)):
          addVar+=textDisplayList[i]
        if addVar.isdigit() == False:
          print("You must enter a positive number (positive integer).")
          drawTextSimple("You must enter a number (positive integer).", 210,275)
          addVar = ""
          break
        elif len(addVar) > 3:
          print("The Ranking must be 3 characters or less.")
          addVar = ""
          break
        else:  
          draw.rect(screen, WHITE,(80,250,300,30))
          drawTextSimple("Enter the best player",80,255)
          draw.rect(screen, WHITE, (210,275,700,25))
          addList.append(addVar) #adding ranking to addlist
          addVar = ""
          step +=1
          maximum = 20
          break
      elif step == 4: 
        for i in range (len(textDisplayList)):
          addVar+=textDisplayList[i]
        if len(addVar) > 20:
          print("The Best Player must be 20 characters or less.")
          addVar = ""
          break
        elif "," in addVar:
            print("A comma is an invalid character.")
            drawTextSimple("comma is an invalid character.", 210,275)
            addVar = ""
            break
        else:
          draw.rect(screen, WHITE,(80,250,300,30))
          drawTextSimple("Enter world cup goals",80,255)
          draw.rect(screen, WHITE, (210,275,700,25))
          addList.append(addVar) #adding best player to addList
          addVar = ""
          step +=1
          maximum = 3
          break
      elif step == 5:
        for i in range(len(textDisplayList)):
          addVar+=textDisplayList[i]
        if addVar.isdigit() == False:
          print("You must enter a number (positive integer).")
          drawTextSimple("You must enter a number (positive integer).", 210,275)
          addVar = ""
          break
        elif len(addVar) > 3:
          print("The number of World Cup Goals must be 3 characters or less.")
          addVar = ""
          break
        else:
          draw.rect(screen, WHITE,(80,250,300,30))
          drawTextSimple("Enter if in round of 16",80,255)
          draw.rect(screen, WHITE, (210,275,700,25))
          addList.append(addVar) #adding World Cup Goals to addList
          addVar = ""
          step+=1
          maximum = 5
          break
      elif step == 6:
        for i in range(len(textDisplayList)):
          addVar+=textDisplayList[i]
        if addVar.lower()!="true" and addVar.lower()!="false":
          drawTextSimple("Enter a boolean value", 210,275)
          print("Enter a boolean value")
          addVar = "" #resetting addVar because the user has entered input incorrectly and we are going to get them to re enter it
          break #break because there is an error. We will return to the loop and then the user will re enter their input
        else:
          draw.rect(screen, WHITE, (210,275,700,25))
          addVar = addVar.lower()
          addVar = addVar.capitalize()
          addList.append(addVar) #adding boolean value to addList
          addVar = "" #resetting addVar
          recordsList.append(addList) #adding the new record to the list of records
          #resetting variables for the next time they want to add a record
          enter = 0
          addList = [] 
          textDisplayList= []
          textAllowed = False
          draw.rect(screen, WHITE,(80,250,300,30))
          drawTextSimple("Completed.",80,255)
          write("info.dat")  #write to the file so that the file can be updated with the new information
          break
    elif function == "3": #if the user enters 3
      step = 2
      if step == 2:
        IDcount = 0
        for i in range(len(textDisplayList)):
          removeID += (textDisplayList[i])
        for i in range(len(recordsList)):
          if ((recordsList[i])[0]) == removeID: #go through all the ID's of every record in the table and if they match the ID  
            del recordsList[i] 
            #than delete the whole record from recordsList
            IDcount +=1 #increase the IDcount by 1 everytime an ID is deleted
            break
        if IDcount == 1: #if an ID was deleted than it is successful
          #reset variables
          draw.rect(screen, WHITE, (210,275,700,25))
          enter = 0
          textAllowed = False
          textDisplayList = []
          removeID = ""
          draw.rect(screen, WHITE,(80,250,300,30))
          drawTextSimple("Completed",80,255)
          write("info.dat")#write the changes to the file
          break
        else:
          #error
          drawTextSimple("That ID does not exist.", 210,275)
          #resetting removeID because we are going to re prompt the user because they inputted something invalid
          removeID = ""
          break
    else: 
      print("Invalid Input.") #if the user does not type any of the numbers that correspond to the menu items then give an error
    write("info.dat") #call the write function to write all the data to the file.
    if function!="4": #if the function is anything but 4 than show the info because for 4 we do not wat to display anything
      displayInfo()
    print("\n\n")
    break
  if function!="4": #if the function is anything but 4 than draw the table because for 4 (reports) we do not need to draw the table
    drawTable()
def keyCheck(): #checking for key input
  global enter
  global xPos_textInput
  global KEY_backspace
  global e
  global KEYDOWN
  global KEYUP
  global K_BACKSPACE
  global K_RETURN
  global KEY_pressed
  if textAllowed == True: #if the user is allowed to press text
    if e.type == KEYDOWN: #if the user is pressing a key 
      if e.key == K_BACKSPACE: #if the key is back space
        if xPos_textInput >= 135: #if the x position is greater than the left most point of the box
          KEY_backspace = True #backspace is true
      if e.key == K_RETURN: #if the enter/return key is pressed
        enter = 1 #set enter to 1, because that signifies that enter has been pressed
        time.wait(100) #some delay
      if xPos_textInput<(120 + (15*maximum)): #if the text is less than a certain amount (depending on maximum) than it will draw the character. Otherwise, it meanst that the character length has been exceeded so the program should not draw any text
        KEY_pressed = True #the key has been pressed and it is valid
    if e.type == KEYUP: #if the key is not being pressed
      if e.key == K_RETURN and enter == 0: #if the key is enter yet enter = 0
        enter = 0 #than keep enter as -
      if e.key == K_BACKSPACE: #if the key is backspace
        KEY_backspace = False #make it false because key is up
      KEY_pressed = False #make KEY_pressed false because key is up and therefore nothing is being pressed
    keyInput() #run the keyInput() function to display characters on s creen
running = True #the program is running
mx = my = 0 #the mouse values are 0
button = 0 # a button is not being pressed
currentState = MAINPAGE #the state is mainPage
displayInfo()  #display the information
xPos_textInput = 120 #the x position of the text is 120
def trafficCop():
  global KEY_pressed
  global xPos_textInput
  global KEY_backspace
  global running
  global e
  global button
  global mx
  global my
  global KEYDOWN
  global KEYUP
  global K_BACKSPACE
  global MAINPAGE
  global VIEW
  global MODIFY
  global ADD
  global REMOVE
  global REPORTS
  global REPORT1
  global REPORT2
  global REPORT3
  global QUITCOMMAND
  global currentState
  global enter
  global textAllowed
  global countTable
  global textDisplayList
  global step
  while running:
      if xPos_textInput<= 0:
        xPos_textInput = 0
      if xPos_textInput>=(120 + (15*maximum)):
        drawTextSimple("Maximum Length reached",100,400) 
      else:
        draw.rect(screen, WHITE,(100,400,400,100))
      for e in event.get():             # checks all events that happen
          if e.type == QUIT:
              running = False
              button = 0
          if e.type == MOUSEBUTTONDOWN:
              button = 1
              mx, my = e.pos 
              if 625<mx<775 and 400<my<450 and button==1:
                textAllowed = True
                addVar = ""
                step = 1
                program("0")
                addList = []
                ID = ""
                field = ""
                change = ""
                removeID = ""
                textDisplayList= []
                countTable = 0
                currentState = MAINPAGE
                xPos_textInput = 120 #setting our variable for the x position of the text that the user is going to enter
          if e.type == KEYDOWN: #if a key is being pressed
            keyCheck() #run the key check function
      #BACKBUTTON
      if currentState!=MAINPAGE: #if the current state is not already main page
        
        if button == 1: #if the user is pressing
          if 625<mx<775 and 80<my<130: #if the mouse is in a certain range
            countTable = 0  #set countTablet 0, because the user is pressing the back button and we will have to redraw the table for the first time
            step = 1
            textDisplayList = []
            xPos_textString = 120
            currentState = MAINPAGE #set the current state to main page because the back button brings us back home
      #looking at the current state and calling the function accordingly
      if currentState == MAINPAGE:
        currentState = mainPage(currentState, mx, my, button)
      elif currentState == VIEW:
        currentState = view(currentState,mx,my,button)
      elif currentState == MODIFY:
        currentState = modify(currentState,mx,my,button)
      elif currentState == ADD:
        currentState = add(currentState,mx,my,button)
      elif currentState == REMOVE:
        currentState = remove(currentState,mx,my,button)
      elif currentState == REPORTS:
        currentState = reports(currentState,mx,my,button)
      elif currentState == REPORT1:
        currentState = report1(currentState,mx,my,button)
      elif currentState == REPORT2:
        currentState = report2(currentState,mx,my,button)
      elif currentState == REPORT3:
        currentState = report3(currentState,mx,my,button)
      elif currentState == QUITCOMMAND:
        currentState = quitCommand(currentState,mx,my,button)
      display.flip()  #displaying everything 
trafficCop() #calling traffic cop function
quit() #quitting the program