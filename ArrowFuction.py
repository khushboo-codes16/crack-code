D = int(input())  
Oc, Of, Od = map(int, input().split())  
Cs, Cb, Cm, Cd = map(int, input().split())  

online_cost = Oc if D <= Of else Oc + (D - Of) * Od  
classic_cost = Cb + (D // Cs) * Cm + D * Cd  

print("Online Taxi" if online_cost <= classic_cost else "Classic Taxi")
