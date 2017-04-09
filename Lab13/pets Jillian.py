
##
## Class PetError -- complete
##

class PetError( ValueError ):
    
    pass

##
## Class Pet -- not complete
##


class Pet( object ):
    
    def __init__( self, species=None, name="" ):
        species_list = ['dog', 'cat', 'horse', 'gerbil', 'hamster', 'ferret']
        if species.lower() in species_list:
            
            self.species_str = species.title()
            self.name_str = name.title()
            
        else:
            
            raise PetError()
            
    def __str__( self ):
        
        result_str = "Species of {:s}".format(self.species_str)
        
        if self.name_str != "":
            result_str += ", named {}".format(self.name_str)
        
        else:
            result_str += ", unnamed."
        
        return result_str

##
## Class Dog -- not complete
##

class Dog( Pet ):

    def __init__(self, name="", chases="Cats"):
        Pet.__init__(self, "dog", name)
        self.chases = chases
        
    def __str__( self ):
        return_str = Pet.__str__( self )
        
        return_str += ", chases {:s}".format(self.chases)
        
        return return_str

##
## Class Cat -- not complete
##

class Cat( Pet ):
    
    def __init__(self, name="", hates="Dogs"):
        Pet.__init__(self, "cat", name)
        self.hates = hates
        
    def __str__( self ):
        return_str = Pet.__str__( self )
        
        return_str += ", hates {:s}".format(self.hates)
        
        return return_str

