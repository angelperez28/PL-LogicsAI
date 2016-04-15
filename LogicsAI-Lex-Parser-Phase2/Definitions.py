class SElement(object):

  def __init__(self,SUBJECT, OBJECT,COMPOBJ):
    #Initializing properties of any circuit element
    self.Objects = []
    self.Complements = []
    self.SUBJECT = SUBJECT
    self.OBJECT = OBJECT
    self.COMPOBJ = COMPOBJ
    if COMPOBJ is not None:
      self.Complements.append(COMPOBJ)
    if OBJECT is not None:
      self.Objects.append(OBJECT)

##sky = SElement("blue", "cloudy")
##room = SElement("big","dark")
