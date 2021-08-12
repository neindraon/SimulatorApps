import numpy as np
class Constants:
    """"Konstanta beta dan lambda yang digunakan dalam perhitungan"""
    
    beta_groups = [0.000215,  # Nilai Beta U-235
                   0.001424,
                   0.001274,
                   0.002568,
                   0.000748,
                   0.000273]
    
    lambda_groups = [0.01244,  # Nilai Lambda U-235
                     0.03051,
                     0.11144,
                     0.30137,
                     1.13631,
                     3.01368]
    
    precursor_groups = [6.48041E+15, # Nilai C1 - C6
                        1.75013E+16,
                        4.28660E+15,
                        3.19504E+15,
                        2.46822E+14,
                        3.39659E+13]
    beta_groups = np.array(beta_groups)    
    lambda_groups = np.array(lambda_groups)        
    precursor_groups = np.array(precursor_groups)    
    
    lp = 0.001  # Prompt neutron generation time (lp) (s)
                          # (sementara mengikuti nilai PWR)
                            
    t_interval = 0.00001 # Time interval untuk perhitungan (h) (s)
    
    n = 1000000 # Banyak iterasi
    
    def __init__(self, beta_groups, lambda_groups, prompt_n_gen, t_interval):
        self.beta_groups = beta_groups
        self.beta = sum(beta_groups)
        self.lambda_groups = lambda_groups
        self.prompt_n_gen = prompt_n_gen
        self.t_interval = t_interval