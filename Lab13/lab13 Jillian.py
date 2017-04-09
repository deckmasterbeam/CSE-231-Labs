
##
## Demonstrate some of the operations of the Pet classes
##

import pets

def main():
    
    try:

        # Hamster
        A = pets.Pet( "Hamster" )
        print( A )       
        
        # Dog named Fido who chases Cats
        B = pets.Dog( "Fido" )
        print( B )

        # Cat named Fluffy who hates everything
        C = pets.Cat( "Fluffy", "everything" )
        print( C )
        
        D = pets.Pet("Ferret", "Aang")
        print( D )
        
        E = pets.Cat("Pepper", "plastic bags")
        print( E )
        
        G = pets.Dog("Woof", "other dogs")
        print( G ) 
        
        F = pets.Pet("parrot", "brazil")
        print( F )

    except pets.PetError:
        
        print( "Got a pet error." )

main()

