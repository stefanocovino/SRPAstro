""" Utility functions and classes for SRP

Context : SRP
Module  : Spectroscopy.py
Version : 1.0.0
Author  : Stefano Covino
Date    : 03/09/2011
E-mail  : stefano.covino@brera.inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : to be imported

History : (03/09/2011) First version.

"""


from SRP.SRPSpectroscopy.DLACrossSection import DLACrossSection
import SRP.SRPSpectroscopy as SS


def TauDLA (lambd,NHI,zDLA):
    return NHI * DLACrossSection((SS.SpeedofLight/lambd) * (1.0+zDLA))
