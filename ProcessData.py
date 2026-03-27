#ProcessData.py
#Name: Kansas Nygaard
#Date: 03/27/26
#Assignment: Lab 8

import random
def makeID(first, last, idNum):
  firstInitial = first[0]
  lastThree = idNum[8:11]
  userID = firstInitial + last + lastThree
  return userID

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  #header for csv file
  outFile.write("FirstName,LastName,UserID,Major-Year\n")

  #read each line in the input file
  for line in inFile:
    parts = line.split() #split lines into pieces
    #store important info
    firstName = parts[0]
    lastName = parts[1]
    idNum = parts[3]
    year = parts[5]
    major = " ".join(parts[6:])
    #create userid with function
    userID = makeID(firstName, lastName, idNum)
    #combine major and year
    majorYear = major + "-" + year
    #write to csv file
    outFile.write(firstName + "," + lastName + "," + userID + "," + majorYear + "\n")
  
  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
