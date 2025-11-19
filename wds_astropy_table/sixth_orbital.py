from .parser import parse_file
import numpy as np


sixth_orbital_columns = [
    (1,20,'s','j2000'),                     # 2000 Coordinates
    (20,29,'s','id'),                       # WDS Id
    (31,45,'s','discoverer'),               # Discover designation and components, or other catalog designation.
    (46,51,'i','ads_id'),                   # ADS (Aitken Double Star catalog) number.
    (52,58,'i','hd_id'),                    # HD catalog number.
    (59,65, 'i','hip_id'),                  # Hipparcos catalog number.
    (67,71, 'f', 'pri_mag'),                # Magnitude of the primary (usually V)
    (72,72, 's', 'pri_mag_flag'),           # primaty magnitude flag :
                                                # > = fainter than quoted magnitude
                                                # < = brighter than quoted magnitude 
                                                # v = variable magnitude
                                                # k = magnitude is in K-band or other infrared band
                                                # ? = magnitude is uncertain
    (74,78, 'f', 'sec_mag'),                # Magnitude of the primary (usually V)
    (79,79, 's', 'sec_mag_flag'),           # primaty magnitude flag :
                                                # > = fainter than quoted magnitude
                                                # < = brighter than quoted magnitude 
                                                # v = variable magnitude
                                                # k = magnitude is in K-band or other infrared band
                                                # ? = magnitude is uncertain
    (82,92, 'f', 'period'),                # Period (P)
    (93,93, 's', 'period_units'),            #  code for period units:
                                                # m = minutes (not yet used!)
                                                # h = hours (not yet used!)
                                                # d = days
                                                # y = years
                                                # c = centuries (rarely used)
    (95, 105, 'f', 'period_error'),         # Published formal error in P (in same units as for P). 
    (106, 115, 'f', 'semi_major'),           # Semi-major axis (a)
    (116,116, 's', 'semi_major_units'),           # code for semi-major axis units:
                                                # a = arcseconds
                                                # m = milliarcseconds (mas)
                                                # M = arcminutes (used only for alp Cen + Proxima Cen)
                                                # u = microarcseconds (uas - not yet used)
    (117, 125, 'f', 'semi_major_error'),     # Error in a. Units are the same as for a.
#   13    T126,F8.4        Inclination (i), in degrees.
#   14    T135,F8.4        Error in i.
#   15    T144,F8.4,A1     Node (Omega), in degrees. An identified ascending node 
#                          is indicated by an asterisk following the value. If 
#                          the ascending node is later determined to off by 
#                          180deg, it is flipped, and a "q" code added to 
#                          indicate the change. 
#   16    T154,F8.4        Error in Omega.
#   17    T163,F12.6,A1    The time of periastron passage (T0) and code for units:
#                            c = centuries (fractional year / 100; used only for 
#                                alp Cen + Proxima Cen) 
#                            d = truncated Julian date (JD-2,400,000 days)
#                            m = modified Julian date  (MJD = JD-2,400,000.5 days)
#                            y = fractional Besselian year
#   18    T177,F10.6       Error in T0. Units are the same as for T0.
#   19    T188,F8.6        Eccentricity (e).
#   20    T197,F8.6        Error in e.
#   21    T206,F8.4,A1     Longitude of periastron (omega), in degrees, reckoned 
#                          from the node as listed. If the published omega value 
#                          is later determined to fall in the wrong quadrant, the 
#                          value is flipped by 180deg; a letter "q" indicates the 
#                          quadrant has been corrected.
#   22    T215,F8.4        Error in omega.
#   23    T224,I4          Equinox, if any, to which the node refers.

    (229, 233, 'i', 'last_date'),           # Date of the last observation used in the orbit 
                                            # calculation, if published.
    (234, 235, 'i', 'grade'),               # Orbit grade, ranging from 1 ("definitive") to 5 
                                                #  ("indeterminate"). Additionally, a grade of 8 is used
                                                #  for interferometric orbits based on visibilities 
                                                #  rather than rho and theta measures (hence not gradable
                                                #  by the present scheme) and a grade of 9 indicates an
                                                #  astrometric binary (also lacking rho and theta data).

#   26    T236,A1          A flag "n" to any notes for this system. 
#   27    T238,A8          A code for the reference (usually based on the name of 
#                          the first author and the date of publication).

    (247, 265, 's', 'orbit_image'),          # Name of image file (png format) illustrating orbit and
                                                # all associated measures in the Washington Double Star 
                                                # database.
]
sixth_orbital_header_lines = 7

def parse_sixth_orbital(filename):
    table = parse_file(filename, sixth_orbital_columns, sixth_orbital_header_lines)
    table['discoverer_normalized'] = discoverer_orbital = np.strings.replace(table['discoverer'], ' ', '')
    return table
