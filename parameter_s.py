from inputparam import InputParam as Param
import math

class parameter_s:
    def __init__(self):
        pass
    def fs(self,zs):
        if zs>Param.zsref:
            r1=(Param.Rc/(Param.Rc+Param.delta_Rr)) * (((Param.zsmax-zs)**2) + ((Param.Rc+Param.delta_Rr)**2))**0.5
            r2=(Param.delta_Rr/(Param.Rc+Param.delta_Rr)) * (((Param.zsmax-zs)**2) + ((Param.Rc+Param.delta_Rr)**2))**0.5
        else:
            r1=((Param.zsmax-Param.zsref)/(Param.zsmax-zs)) * (((Param.zsmax-zs)**2) + ((Param.Rc+Param.delta_Rr)**2))**0.5
            r2=((Param.zsref-zs)/(Param.zsmax-zs)) * (((Param.zsmax-zs)**2) + ((Param.Rc+Param.delta_Rr)**2))**0.5

        atas=math.exp(-(Param.C1*r1*((Param.Sigma_A1/Param.D1)**0.5) + Param.C2*r2*((Param.Sigma_A2/Param.D2)**0.5)))
        bawah=(Param.C1*r1*((Param.Sigma_A1/Param.D1)**0.5) + Param.C2*r2*((Param.Sigma_A2/Param.D2)**0.5))

        s=Param.sn*(atas/bawah)
        return s