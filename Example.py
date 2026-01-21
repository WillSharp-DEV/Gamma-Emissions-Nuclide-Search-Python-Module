from GammaEmmisionsLibrary import CreateSearch

def main():
    NewSearch = CreateSearch().Search.InRange(400, 30)
    print("Closest Nuclides to energy 600 keV and width of 30 keV:")
    for i in NewSearch:
        print(f"{i.Name} @ {i.Energy} keV")

if __name__ == "__main__":
    main()