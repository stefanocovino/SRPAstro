""" Utility functions and classes for SRP

Context : SRP
Module  : Sky
Version : 1.0.0
Author  : Stefano Covino
Date    : 19/01/2023
E-mail  : stefano.covino@inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : to be imported

Remarks : Possible sites are:
    {'STANDARD': {'T': 288.15, 'p': 101325, 'RH': 0.0, 'xc': 450,
        'latitude': 0, 'altitude': 0, 'comment': 'Standard atmospheric conditions'},
    'CERRO_ARMAZONES': {'T': 279.65, 'p': 71200, 'RH': 0.22, 'xc': 450,
        'latitude': -24.5983, 'altitude': 3064, 'comment': 'Default conditions for Cerro Armazones, site of the ELT.\nValues are taken from the optical model of MICADO.'},
    'CERRO_PARANAL': {'T': 285.95, 'p': 74300, 'RH': 0.15, 'xc': 450,
        'latitude': -24.623, 'altitude': 2635, 'comment': 'Average conditions at Cerro Paranal, site of the VLT.\nValues are taken from https://www.eso.org/sci/facilities/paranal/astroclimate/site.html and https://academic.oup.com/mnras/article/399/2/783/1061377'},
    'LA_SILLA': {'T': 284.65, 'p': 77220, 'RH': 0.44, 'xc': 450,
        'latitude': -29.25, 'altitude': 2400, 'comment': 'Average conditions of the La Silla Observatory.\nValues based on https://www.eso.org/gen-fac/pubs/astclim/lasilla/diffrefr.html'},
    'LAS_CAMPANAS': {'T': 285.85, 'p': 76400, 'RH': 0.0, 'xc': 450,
        'latitude': -29.016, 'altitude': 2380, 'comment': 'Mean conditions at Las Campanas observatory, site of the GMT.\nValues based on https://www.gmto.org/Resources/GMT-ID-01466-Chapter_5_Site_Evaluation.pdf and http://weather.lco.cl/'},
    'LA_PALMA': {'T': 281.95, 'p': 77500, 'RH': 0.36, 'xc': 450,
        'latitude': 28.764, 'altitude': 2396, 'comment': 'Average conditions for Roque de los Muchachos Observatory on La Palma, Spain.\nValues taken from https://academic.oup.com/mnras/article/399/2/783/1061377'},
    'MAUNA_KEA': {'T': 274.45, 'p': 61400, 'RH': 0.48, 'xc': 450,
        'latitude': 19.826, 'altitude': 4205, 'comment': 'Average conditions at the Mauna Kea Observatory.\nValues taken from http://www.soest.hawaii.edu/MET/Faculty/businger/mauna_kea/daSilvaThesisFinal.pdf, Ch. 3. and https://www.eso.org/gen-fac/pubs/astclim/espas/espas_reports/ESPAS-MaunaKea.pdf'}}

    
History : (19/02/2023) First version.

"""

import AstroAtmosphere as AA

def AtmRefraction (l, z, site='CERRO_PARANAL'):
    return AA.quick_refraction(l, z, conditions=site)*3600
