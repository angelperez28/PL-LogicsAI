#  LogicsAI Parser
#
#  By Angel Perez, Carlos Donato, Gilberto Jimenez, Luis Sala

#Import Yacc library from PLY
import ply.yacc as yacc

#Import the LogicsAi Definitions
import Definitions

#Import OS containing Python Scripts
#import os

# Get the map of tokens from the lexer.
from Lex import tokens


defined_SC = []

consoleCode = []

#General statement rule
def p_statement(p):
    '''
    statement : inquiry
    '''
    pass

#Groups
#Rules for identifying the structure and components of the line of code
def p_statement_1(p):
    'statement : THE SUBJECT IS OBJECT'
    global defined_SC

    for element in defined_SC:
      if(element.SUBJECT == p[2]):
        element.Objects.append(p[4])
        break
    else :
            defined_SC.append(Definitions.SElement(p[2], p[4],None))
    
def p_statement_2(p):
    'statement : THE SUBJECT IS NOT COMPOBJ'
    global defined_SC
    
    for element in defined_SC:
      if(element.SUBJECT == p[2]):
        element.Complements.append(p[5])
        break
    else :
            defined_SC.append(Definitions.SElement(p[2],None,p[5]))

def p_statement_3(p):
    'statement : THE SUBJECT AND SUBJECT ARE OBJECT'
    global defined_SC
    
    for element in defined_SC:
      if(element.SUBJECT == p[2]):
        element.Objects.append(p[6])
        break
    else :
            defined_SC.append(Definitions.SElement(p[2], p[6], None))
            
    for element in defined_SC:
      if(element.SUBJECT == p[4]):
        element.Objects.append(p[6])
        break
    else :
            defined_SC.append(Definitions.SElement(p[4],p[6], None))

def p_statement_4(p):
    'statement : THE SUBJECT AND SUBJECT ARE NOT COMPOBJ'
    global defined_SC
    
    for element in defined_SC:
      if(element.SUBJECT == p[2]):
        element.Complements.append(p[7])
        break
    else :
            defined_SC.append(Definitions.SElement(p[2],None, p[7]))
            
    for element in defined_SC:
      if(element.SUBJECT == p[4]):
        element.Complements.append(p[7])
        break
    else :
            defined_SC.append(Definitions.SElement(p[4], None, p[7]))

def p_statement_5(p):
    'statement : THE SUBJECT IS OBJECT AND NOT COMPOBJ'
    global defined_SC
    
    for element in defined_SC:
      if(element.SUBJECT == p[2]):
        element.Objects.append(p[4])
        elements.Complements.append(p[7])
        break
    else :
            defined_SC.append(Definitions.SElement(p[2],p[4],p[7]))

def p_hypothesis_6(p):
    'statement : IF THE SUBJECT IS OBJECT THEN SUBJECT IS OBJECT'
    global defined_SC
    
    for element in defined_SC:
      if((element.SUBJECT == p[3])& (p[5] in element.Objects)):
          for element2 in defined_SC:
            if(element2.SUBJECT == p[7]):
                element2.Objects.append(p[9])
                break
            else :
                defined_SC.append(Definitions.SElement(p[7],p[9], None))
                break
                 
def p_element_inquiry(p):
    'inquiry : IS THE SUBJECT OBJECT'
    global defined_SC
    
    for element in defined_SC:
      if((element.SUBJECT == p[3])&(element.OBJECT in element.Objects)):
        print ("True")
        break
    else :
            print("False")

def p_element_inquiry2(p):
    'inquiry : WHAT IS OBJECT'
    global defined_SC
    SubjectsRecovered = []
    for element in defined_SC:
      if((p[3] in element.Objects)):
        SubjectsRecovered.append(element.SUBJECT)

    print(SubjectsRecovered)

def p_element_inquiry3(p):
    'inquiry : WHAT IS NOT COMPOBJ'
    global defined_SC
    SubjectsRecovered = []
    for element in defined_SC:
      if((p[4] in element.Complements)):
        SubjectsRecovered.append(element.SUBJECT)

    print(SubjectsRecovered)
            
# Error rule for detecting syntax errors
def p_error(p):
    print("Syntax error in input at: '%s'" % repr(p))

#Auxiliary Functionalities

#Finds an element based on the subject
def getElem(SUBJECT):
  global defined_SC

  for element in defined_SC:
    if(element.SUBJECT == SUBJECT):
      return element

    print("Not Found")
  return None #Returns null if element is not found

def getAll():
  global defined_SC
  for element in defined_SC:
    print(element.SUBJECT)

def getComplements(SUBJECT):
  global defined_SC
  for element in defined_SC:
      if(element.SUBJECT == SUBJECT):
        print(element.Complements)
        break

def get5(SUBJECT):
  global defined_SC
  for element in defined_SC:
      if(element.SUBJECT == SUBJECT):
        print(element.Complements)
        print(element.Objects)
        break

def getComplementsNot(SUBJECT, SUBJECT2):
  global defined_SC
  for element in defined_SC:
      if(element.SUBJECT == SUBJECT):
        print(element.Complements)
        break
  for element in defined_SC:
      if(element.SUBJECT == SUBJECT2):
        print(element.Complements)
        break

def getObjects(SUBJECT, SUBJECT2):
  global defined_SC
  for element in defined_SC:
      if(element.SUBJECT == SUBJECT):
        print(element.Objects)
        break
  for element in defined_SC:
      if(element.SUBJECT == SUBJECT2):
        print(element.Objects)
        break

def clear():
  global consoleCode
  consoleCode = []
  global defined_SC
  defined_SC = []

# Parser Builder
parser = yacc.yacc()

#Main Program

print("\n")

while True:
  try:
    s = input('logicsAI >> ')
    
  except EOFError:
    break

  if not s: 
    continue
#Commands listing
  elif s == 'clear':
    #Reset variables
    clear()
    continue

  elif s == 'getall':
    #Gets all subjects
    getAll()
    continue

  elif s == 'getcomplements':
    #Gets all complements
    getComplements("sky")
    continue

  elif s == 'getcomplementsnot':
    #Gets all !complements
    getComplementsNot("sky", "sea")
    continue

  elif s == 'get5':
    get5("sky")
    continue

  elif s == 'getobjects':
    #Gets all objects
    getObjects("sky", "sea")
    continue

  elif s == 'run':
    #Runs the parser with the given code
    print("Debug: Code to be evaluated by parser:")
    print(consoleCode)
    
    #Parse code, line by line
    for code in consoleCode:
      result = parser.parse(code)
  else:
    #Stores the line of code
    global consoleCode
    consoleCode.append(s)
