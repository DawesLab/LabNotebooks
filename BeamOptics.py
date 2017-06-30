from numpy import sqrt, arctan, pi, exp, random, shape
I = 1.0j
# A package for beam optics in python


def spot_size(z, zR, w0):
    """Calculate spot size at z, given zR, and w0"""
    return w0 * sqrt(1 + (z/zR)*(z/zR))


def radius_curvature(z, zR):
    """calculate R(z)"""
    # This could be smarter, just adding epsilon to avoid nan's
    if (z == 0):
        z += 1e-31
    return z * (1 + (zR/z)*(zR/z))


def guoy_phase(z, zR):
    """really just atan(z/zR)"""
    return arctan(z/zR)


def rayleigh_range(w0, wavelambda):
    """Calculate rayleigh range"""
    return pi*w0*w0/wavelambda


def gaussian_beam(x, y, z, E0, zR, w0, k):
    """full gaussian beam at x, y, z given the beam parameters\n
    E0 is the electric field amplitude
    zR is the raleigh range
    w0 is the beam waist (1/e field radius and 1/e^2 intensity radius)
    k is a tuple of [kx,ky,kz]"""

    r = sqrt(x*x + y*y)
    w = spot_size(z, zR, w0)
    R = radius_curvature(z, zR)
    eta = guoy_phase(z, zR)
    return E0 * w0/w * exp(- r*r/(w*w)) *\
        exp(-I*k[2]*z - I*k[2]*r*r/(2*R) + I*eta)*exp(I*k[0]*x + I*k[1]*y) #\
        #+ sqrt(E0)*random.random([max(shape(x)), max(shape(y))])
    # The exp(ikz) term in this definition causes extra phase accumulation
    # compared to the BPM. I need to sort this out for sure.
    # The following agrees with BPM:
    # return w0/w * exp(- r*r/(w*w)) * exp(- 1j*k*r*r/(2*R) + 1j*eta)


def plane_wave_beam(x, y, z, A, k):
    """a simple plane wave mostly used for testing"""
    #dphase = 1/(2*A**2)
    #noiseamp = sqrt(A) * (random.random() - 0.5)
    #noisephase = exp(2*pi*1j*dphase*(random.random() - 0.5))
    # noise = random.normal(0, 0.5) * exp(1j*2*pi*random.random())
    # return (A + noise) * exp(I*k[0]*x + I*k[1]*y + I*k[2]*z)
    return (A) * exp(I*k[0]*x + I*k[1]*y + I*k[2]*z)
    #return A * exp(I*k[0]*x + I*k[1]*y + I*k[2]*z)
    # this is more accurate, the best way to model is to let
    # the amplitude have noise.
