def dvizenye(vrast, vrema, prost, pves):
    sk = vrast // vrema
    dvizenye = 0.035 * pves + (sk ** 2 / prost) * 0.029 * pves
    dvizenye = dvizenye * vrema
    return dvizenye

def velosiped(vrema, puls, pves):
    vel = 0.014 * pves * vrema * (0.12 * puls - 7)
    return vel