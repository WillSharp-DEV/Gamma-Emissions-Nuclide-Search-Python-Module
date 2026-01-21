# Gamma-Emissions-Nuclide-Search-Python-Module
This simple python script helps in the aid of determining Nuclide's based off their gamma emission energy. The datasource this python module uses comes directly from https://atom.kaeri.re.kr.
Below is an example of its execution...

```
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
```

This exact script can be found in example.py
