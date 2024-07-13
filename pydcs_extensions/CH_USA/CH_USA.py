# Requires Currenthill US Forces
# https://www.currenthill.com/usa
#
from typing import Set

from dcs import unittype
from game.modsupport import vehiclemod, shipmod

@vehiclemod
class FMTV_M1083(unittype.VehicleType):
    id = "CH_FMTV_M1083"
	name = "[CH] Oshkosh FMTV M1083"
	detection_range = 0
	threat_range = 0
	air_weapon_distance = 0
	

@vehiclemod
class CH_HEMTT_M977(unittype.VehicleType):
    id = "CH_HEMTT_M977"
	name = "[CH] Oshkosh HEMTT M977"
	detection_range = 0
	threat_range = 0
	air_weapon_distance = 0
	

@vehiclemod
class CH_HEMTT_M983(unittype.VehicleType):
    id = "CH_HEMTT_M983"
    name = "[CH] Oshkosh HEMTT M983"
    detection_range = 0
    threat_range = 0
    air_weapon_distance = 0	
	
	
@vehiclemod
class CH_M1A2SEPV3(unittype.VehicleType):
    id = "CH_M1A2SEPV3"
    name = "[CH] M1A2 SEPv3 MBT"
    detection_range = 0
    threat_range = 5000
    air_weapon_distance = 1800 
    eplrs =	True
	
	
@vehiclemod
class CH_M2A3(unittype.VehicleType):
    id = "CH_M2A3"
    name = "[CH] M2A3 IFV"
    detection_range = 0
    threat_range = 3800
    air_weapon_distance = 2500
    eplrs = True


@vehiclemod
class CH_M10(unittype.VehicleType):
    id = "CH_M10"
    name = "[CH] M10 LT"
    detection_range = 0
    threat_range = 4000
    air_weapon_distance = 1800
    eplrs = True


@vehiclemod
class CH_OshkoshLATV_M2(unittype.VehicleType):
    id = "CH_OshkoshLATV_M2"
    name = "[CH] Oshkosh L-ATV (M2)"
    detection_range = 0
    threat_range = 1800
	air_weapon_distance = 0
    eplrs = True


@vehiclemod
class CH_OshkoshLATV_MK19(unittype.VehicleType):
    id = "CH_OshkoshLATV_MK19"
    name = "[CH] Oshkosh L-ATV (Mk19)"
    detection_range = 0
    threat_range = 2000
    air_weapon_distance = 0
	eplrs = True


@vehiclemod
class CH_OshkoshMATV_M2(unittype.VehicleType):
    id = "CH_OshkoshMATV_M2"
    name = "[CH] Oshkosh M-ATV MRAP (M2)"
    detection_range = 0
    threat_range = 1800
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class CH_OshkoshMATV_MK19(unittype.VehicleType):
    id = "CH_OshkoshMATV_MK19"
    name = "[CH] Oshkosh M-ATV MRAP (Mk19)"
    detection_range = 0
    threat_range = 2000
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class CH_M551(unittype.VehicleType):
    id = "CH_M551"
	name = "[CH] M551 LT"
	detection_range = 0
	threat_range = 3000
	air_weapon_range = 1800
	eplrs = True
	
	
## ARTILLERY


@vehiclemod
class M142_HIMARS_ATACMS(unittype.VehicleType):
    id = "M142_HIMARS_ATACMS"
	name = "[CH] M142 HIMARS (ATACMS)"
	detection_range = 0
	threat_range = 296000
	air_weapon_range = 0
	eplrs = True


@vehiclemod
class M142_HIMARS_GLSDB(unittype.VehicleType):
    id = "M142_HIMARS_GLSDB"
    name = "[CH] M142 HIMARS (GLSDB)"
    detection_range = 0
    threat_range - 150000
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class M142_HIMARS_GMLRS(unittype.VehicleType):
    id = "M142_HIMARS_GMLRS"
    name = "[CH] M142 HIMARS (GMLRS)"
    detection_range = 0
    threat_range = 92000
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class M142_HIMARS_PRSM(unittype.VehicleType):
    id = "M142_HIMARS_PRSM"
    name = "[CH] M142 HIMARS (PrSM)"
    detection_range = 0
    threat_range = 500000
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class M142_HIMARS_PRSM_ASHM(unittype.VehicleType):
    id = "M142_HIMARS_PRSM_ASHM"
    name = "[CH] M142 HIMARS (PrSM AShM)"
    detection_range = 0
    threat_range = 500000
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class CH_M270A1_ATACMS(unittype.VehicleType):
    id = "CH_M270A1_ATACMS"
    name = "[CH] M270A1 MLRS (ATACMS)"
    detection_range = 0
    threat_range = 296000
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class CH_M270A1_GLSDB(unittype.VehicleType):
    id = "CH_M270A1_GLSDB"
    name = "[CH] M270A1 MLRS (GLSDB)"
    detection_range = 0
    threat_range = 150000
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class CH_M270A1_GMLRS(unittype.VehicleType):
    id = "CH_M270A1_GMLRS"
    name = "[CH] M270A1 MLRS (GMLRS)"
    detection_range = 0
    threat_range = 92000
    air_weapon_range = 0
    eplrs = True  


## Air Defense


@vehiclemod
class CH_LAVAD(unittype.VehicleType):
    id = "CH_LAVAD"
    name = "[CH] LAV-AD SPAAGM"
    detection_range = 10000
    threat_range = 8000
    air_weapon_range = 8000
    eplrs = True


@vehiclemod	
class MIM104_ANMPQ65(unittype.VehicleType):
    id = "MIM104_ANMPQ65"
	name = "[CH] MIM-104 AN/MPQ-65 STR (stationary)"
	detection_range = 200000
	threat_range = 0
	air_weapon_range = 0
	eplrs = True
	
	
@vehiclemod
class MIM104_ANMPQ65A(unittype.VehicleType):
    id = "MIM104_ANMPQ65A"
    name = [CH] MIM-104 AN/MPQ-65A STR (stationary)
    detection_range = 260000
    threat_range = 0
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class MIM104_ECS(unittype.VehicleType):
    id = "MIM104_ECS"
    name = "[CH] MIM-104 ECS"
    detection_range = 0
    threat_range = 0
    air_weapon_range = 400000	
    eplrs = True


@vehiclemod
class MIM104_EPP(unittype.VehicleType):
    id = "MIM104_EPP"
    name = "[CH] MIM-104 EPP"
    detection_range = 0
    threat_range = 0 
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class MIM104_LTAMDS(unittype.VehicleType):
    id = "MIM104_LTAMDS"
    name = "[CH] MIM-104 LTAMDS STR (stationary)"
    detection_range = 400000
    threat_range = 0
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class MIM104_M903_PAC2(unittype.VehicleType):
    id = "MIM104_M903_PAC2"
    name = "[CH] MIM-104 M903 PAC-2 GEM/T LN (stationary)"
    detection_range = 0
    threat_range = 150000
    air_weapon_range = 150000
    eplrs = True


@vehiclemod
class MIM104_M903_PAC3(unittype.VehicleType):
    id = "MIM104_M903_PAC3"
    name = "[CH] MIM-104 M903 PAC-3 MSE LN (stationary)"
    detection_range = 0
    threat_range = 120000
    air_weapon_range = 120000
    eplrs = True


@vehiclemod
class CH_NASAMS3_LN_AMRAAM_ER(unittype.VehicleType):
    id = "CH_NASAMS3_LN_AMRAAM_ER"
    name = "[CH] NASAMS 3 LCHR LN (AMRAAM-ER)"
    detection_range = 0 
    threat_range = 50000
    air_weapon_range = 50000
    eplrs = True


@vehiclemod
class CH_NASAMS3_SR(unittype.VehicleType):
    id = "CH_NASAMS3_SR"
    name = "[CH] NASAMS 3 SR"
    detection_range = 120000
    threat_range = 0
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class CH_THAAD_TFCC(unittype.VehicleType):
    id = "CH_THAAD_TFCC"
    name = "[CH] THAAD TFCC"
    detection_range = 1000000
    threat_range = 0
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class CH_THAAD_M1120(unittype.VehicleType):
    id = "CH_THAAD_M1120"
    name = "[CH] THAAD M1120 LN"
    detection_range = 0
    threat_range = 200000
    air_weapon_threat = 200000
    eplrs = True


@vehiclemod
class CH_THAAD_ANTPY2(unittype.VehicleType):
    id = "CH_THAAD_ANTPY2"
    name = "[CH] THAAD AN/TPY-2 STR"
    detection_range = 1000000
    threat_range = 0
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class CH_NASAMS3_LN_AIM9X2(unittype.VehicleType):
    id = "CH_NASAMS3_LN_AIM9X2"
    name = "[CH] NASAMS 3 LCHR LN (AIM-9X-2)"
    detection_range = 0
    threat_range = 20000
    air_weapon_range = 20000
    eplrs = True


@vehiclemod
class CH_NASAMS3_CP(unittype.VehicleType):
    id = "CH_NASAMS3_CP"
    name = "[CH] NASAMS 3 CP"
    detection_range = 120000
    threat_range = 0
    air_weapon_range = 0
    eplrs = True


## Infantry


@vehiclemod
class CH_USInfantry_MK19(unittype.VehicleType):
    id = "CH_USInfantry_MK19"
    name = "[CH] Mk19 AGL Soldier"
    detection_range = 0
    threat_range = 1500
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class CH_USInfantry_M249(unittype.VehicleType):
    id = "CH_USInfantry_M249"
    name = "[CH] M249 LMG Soldier"
    detection_range = 0
    threat_range = 700
    air_weapon_range = 700
    eplrs = True


@vehiclemod
class CH_USInfantry_M240(unittype.VehicleType):
    id = "CH_USInfantry_M240"
    name = "[CH] M240 GPMG Soldier"
    detection_range = 0
    threat_range = 1200
    air_weapon_range = 700
    eplrs = True


@vehiclemod
class CH_USInfantry_M136(unittype.VehicleType):
    id = "CH_USInfantry_M136"
    name = "[CH] M136 AT Soldier"
    detection_range = 0
    threat_range = 400
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class CH_USInfantry_M120(unittype.VehicleType):
    id = "CH_USInfantry_M120"
    name = "[CH] M120 120 mm Mortar"
    detection_range = 0
    threat_range = 7200
    air_weapon_range = 0
    eplrs = True


@vehiclemod
class CH_USInfantry_M82(unittype.VehicleType):
    id = "CH_USInfantry_M82"
    name = "[CH] M82 AMR Soldier"
    detection_range = 0
    threat_range = 1800
    air_weapon_range = 1800
    eplrs = True


@vehiclemod
class CH_USInfantry_M4M203(unittype.VehicleType):
    id = "CH_USInfantry_M4M203"
    name = "[CH] M4/M203 AR/GL Soldier"
    detection_range = 0
    threat_range = 500
    air_weapon_range = 500
    eplrs = True


@vehiclemod
class CH_USInfantry_M4(unittype.VehicleType):
    id = "CH_USInfantry_M4"
    name = "[CH] M4 AR Soldier"
    detection_range = 0
    threat_range = 500
    air_weapon_range = 500
    eplrs = True


@vehiclemod
class CH_USInfantry_M2(unittype.VehicleType):
    id = "CH_USInfantry_M2"
    name = "[CH] M2 HMG Soldier"
    detection_range = 0
    threat_range = 1800
    air_weapon_range = 1800
    eplrs = True


@vehiclemod
class CH_USInfantry_FIM92(unittype.VehicleType):
    id = "CH_USInfantry_FIM92"
    name = "[CH] FIM-92K Stinger Soldier"
    detection_range = 0
    threat_range = 8000
    air_weapon_range = 8000


@vehiclemod
class CH_USInfantry_FGM148(unittype.VehicleType):
    id = "CH_USInfantry_FGM148"
    name = "[CH] FGM-148 ATGM Soldier"
    detection_range = 0
    threat_range = 5000
    air_weapon_range = 5000
    eplrs = True


## Navy
	
	
@shipmod
class CH_Arleigh_Burke_III(unittype.VehicleType):
    id = "CH_Arleigh_Burke_III"
    name = "[CH] Arleigh Burke Flight III Destroyer"
    helicopter_num = 2
	parking = 1
	detection_range = 650000
	threat_range = 650000
	air_weapon_range = 650000
	
	
@shipmod
class CH_Arleigh_Burke_IIA(unittype.VehicleType):
    id = "CH_Arleigh_Burke_IIA"
    name = "[CH] Arleigh Burke Flight IIA Destroyer"
    helicopter_num = 2
    parking = 1
    detection_range = 325000
	threat_range = 160000
	air_weapon_range = 160000


@shipmod
class CH_Constellation(unittype.VehicleType):
    id = "CH_Constellation"
    name = "[CH] Constellation Class Frigate"
    helicopter_num = 1
    parking = 1
    detection_range = 450000
    threat_range = 160000
    air_weapon_range = 160000
	
	
@shipmod
class CH_Ticonderoga(unittype.VehicleType):
    id = "CH_Ticonderoga"
    name = "[CH] Ticonderoga Cruiser"
    helicopter_num = 2
    parking = 1
    detection_range = 325000
    threat_range = 160000
    air_weapon_range = 160000


@shipmod
class CH_Ticonderoga_CMP(unittype.VehicleType):
    id = "CH_Ticonderoga_CMP"
    name = "[CH] Ticonderoga CMP Cruiser"
    helicopter_num = 2
    parking = 1
    detection_range = 325000
    threat_range = 32500
    air_weapon_range = 325000
	

 	
     	
     	
	
       	
