# This is how we import the module
from  GammaEmmisionsLibrary  import  CreateSearch

def  main():
	#This creates our new search instance and searches all nuclides around 400 keV at a max of plusminus 30
	NewSearch  =  CreateSearch().Search.InRange(400, 30)
	print("Closest Nuclides to energy 600 keV and width of 30 keV:")
	#A simple iterable loop that prints each found Nuclides name and energy!
	for  i  in  NewSearch:
		print(f"{i.Name} @ {i.Energy} keV")
		
if  __name__  ==  "__main__":
	main()