class InputParam:
    """Input-input nilai parameter yang bersangkutan dengan perhitungan 
    dinamika reaktor MRHP."""
    
    # Parameter operasi
   
    power = 1E-6  # Daya operasi reaktor (W)
   
    e = 200 # MeV/fusi
   
    k = 1.6021E-13 # J/MeV
       
    nu = 2.487710 # Nilai Nu
   
    eta = 2.02725434 #Nilai Eta

    eps = 2.55 #Nilai Epsilon
      
    rho = 0.000 # Nilai reaktivitas sementara 0.0074903077
        
    # Parameter termal
    
    v_fuel = 0.430279033 # Volume bahan bakar UO2 dan Thorium (m3)
    
    v_reactor = 9.236832416 # Volume reaktor (m3)
    
    m_reactor = 21181.62582 # Massa reaktor (kg)
    
    cpr = 720.9506722 # Kalor jenis rerata reaktor (J/(kg.K))
    
    u_reactor = 22015.75002 # Koefisien transfer kalor menuju heat pipe
                           # (W/(m2.K))
 
    t_reactor = 973 # Suhu inisial reaktor (K)
    
    t_msp = 817 # Suhu inisial Molten Salt Pool (K)
    
    #Parameter s
    
    sn = 1E+10 #laju pancaran neutron dari sumber (neutron/s)

    C1 = 0.5    #faktor koreksi geometri reaktor (cm)

    C2 = 0.5    #faktor koreksi geometri reflektor (cm)

    Sigma_A1 = 0.00741131    #tampang lintang serapan makros reaktor (1/cm)

    Sigma_A2 = 0.00000464    #tampang lintang serapan makros reflektor (1/cm)

    D1 = 0.22032810  #koef. difusi neutron pd reaktor (cm)

    D2 = 1.96361548  #koef. difusi neutron pd reflektor (cm)

    Rc = 55 #radius teras reaktor (cm)

    delta_Rr = 111  #radius reflektor samping (cm)

    zsmax=150

    zsref=100
    
    
    
    