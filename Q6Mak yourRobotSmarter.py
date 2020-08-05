"""   AI has provided bots to learn human skills but still
they are very much limited as everything needs to be taught.
You as a developer needs to write a robust framework using
OOPs concepts that allows the users to add new skills to the Bot.

    Provided below is the Interface of the Skill
    and Robot class that serves as an instance to
    the final bot. And add the following skills

    WhatIsMyName
    WhoCreatedYou
    WhatSkillsYouHave

"""

from abc import abstractmethod

class Robot:
    """
        Robot class 
    """
    def __init__(self,names,creator):
      self.name = names
      self.creator = creator
  

    def ask(self, query):
      print("Hello my name is" self.name)
      


class Skill: 
    """
        Skill Class
    """
    
    def WhatIsMyName(self):
      self.ask(self.name)
      
      
    def WhoCreatedYou(self):
      print("my creator is",self.creator)
      
    def WhatSkillYouHave(self):
      print("i can talk")
      
    @abstractmethod
    def execute(self):
        pass
      
