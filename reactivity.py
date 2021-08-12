from inputparam import InputParam as Param

class Reactivity:
    def __init__(self):
        pass
        
    def reactivity_func(self, temp, z1, z2, t):
        """Perhitungan perubahan reaktivitas akibat perubahan suhu reaktor, 
        ketinggian reflektor, burnup, poison, dan excess reactivity"""
        
        #Perubahan reaktivitas suhu reaktor
        temperature = (-2.18885E-05) * (temp - 973)
        
        #Perubahan reaktivitas akibat ketinggian reflektor             
        height =(-5.188078E-13 * z1**6) - (1.357260E-10 * z1**5) - (1.247909E-08 * z1**4) - (5.250613E-07 * z1**3) - \
                (1.588379E-05 * z1**2) - (1.299811E-04 * z1) + \
                (5.539788E-13 * z2**6) + (1.843489E-10 * z2**5) + (2.347309E-08 * z2**4) + (1.359879E-06 * z2**3) + \
                (3.059608E-05 * z2**2) + (3.374790E-04 * z2) + \
                ((-1.298881E-16 * z2**6) - (3.037237E-14 * z2**5) - (2.575903E-12 * z2**4) - (1.036916E-10 * z2**3) - \
                (1.172406E-09 * z2**2) + (8.584116E-08 * z2)) * z1**2 + \
                ((2.373176E-14 * z2**6) + (7.181094E-12 * z2**5) + (7.992216E-10 * z2**4) + (3.950583E-08 * z2**3) + \
                (9.243540E-07 * z2**2) + (1.756676E-05 * z2)) * z1
                
        #Perubahan reaktivitas akibat burnup    
        burnup = (-0.0005) * t
        
        #Reaktivitas excess
        excess = 0.00937134705684230
        
        return temperature+height+burnup+excess
    
