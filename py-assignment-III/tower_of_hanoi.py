def TowerOfHanoi(n , source, destination, auxilliary): 
    if n==1: 
        print(f"Move disk 1 from source {source}to destination {destination}") 
        return
    TowerOfHanoi(n-1, source, auxilliary, destination) 
    print(f"Move disk{n} from source {source } to destination {destination}") 
    TowerOfHanoi(n-1, auxilliary, destination, source) 

n = 4
TowerOfHanoi(n,'A','B','C')  