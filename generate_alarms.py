from utils import *
import zipfile
# delta type use setpoint raddr
# room, mid, alarm_type, tag_type, raddr, logic, target, msg, sp=None

DT_HI = 5
DT_LO = -5
OOST_HI = 30
OOST_LO = 18

DH_HI = 10
DH_LO = -10
OOSH_HI = 70
OOSH_LO = 40

DCO2_HI = 2000
DCO2_LO = -300
OOSCO2_HI = 2000
OOSCO2_LO = 300

DDP_HI = 0.3
DDP_LO = -0.3
OOSDP_HI = 0.3
OOSDP_LO = -0.3
O2L = 9
CO2L = 3500

i = 1
TagAlarm("GR{}".format(i), i*2-1, "Temp", "delta", 2, ">", DT_HI, "Grow Room {} Temperature	deviation High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "Temp", "delta", 2, "<", DT_LO, "Grow Room {} Temperature deviation Low Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "Temp", "value", 2, ">", OOST_HI, "Grow Room {} Temperature Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "Temp", "value", 2, "<", OOST_LO, "Grow Room {} Temperature Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i*2-1, "RH", "delta", 12, ">", DH_HI, "Grow Room {} Relative Humidity deviation High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "RH", "delta", 12, "<", DH_LO, "Grow Room {} Relative Humidity deviation Low Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "RH", "value", 12, ">", OOSH_HI, "Grow Room {} Relative Humidity Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "RH", "value", 12, "<", OOSH_LO,"Grow Room {} Relative Humidity Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i*2-1, "CO2", "delta", 22, ">", DCO2_HI, "Grow Room {} CO2 deviation High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "CO2", "delta", 22, "<", DCO2_LO, "Grow Room {} CO2 deviation Low Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "CO2", "value", 22, ">", OOSCO2_HI, "Grow Room {} CO2 Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "CO2", "value", 22, "<", OOSCO2_LO, "Grow Room {} CO2 Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i*2-1, "DP", "delta", 37, ">", DDP_HI, "Grow Room {} Difference Pressure deviation High Alarm".format(i), sp=0)
TagAlarm("GR{}".format(i), i*2-1, "DP", "delta", 37, "<", DDP_LO, "Grow Room {} Difference Pressure deviation Low Alarm".format(i), sp=0)
TagAlarm("GR{}".format(i), i*2-1, "DP", "value", 37, ">", OOSDP_HI, "Grow Room {} Difference Pressure Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "DP", "value", 37, "<", OOSDP_LO, "Grow Room {} Difference Pressure Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i*2, "Max-Valve", "value", 33, "==", 1, "Grow Room {} Max number of Valves in failure Alarm".format(i)) # digital
TagAlarm("GR{}".format(i), i, "O2-Life", "value", 38, "<", O2L, "Grow Room {} O2 life safety Low Alarm".format(i))
TagAlarm("GR{}".format(i), i, "CO2-Life", "value", 39, ">", CO2L, "Grow Room {} CO2 life safety High Alarm".format(i))

TagAlarm("GR{}".format(i), i*2, "AHU 1", "value", 44, "==", 1, "Grow Room {} AHU 1 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "AHU 2", "value", 45, "==", 1, "Grow Room {} AHU 2 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "AHU 3", "value", 46, "==", 1, "Grow Room {} AHU 3 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "AHU 4", "value", 47, "==", 1, "Grow Room {} AHU 4 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "FFU 1", "value", 48, "==", 1, "Grow Room {} FFU 1 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "FFU 2", "value", 49, "==", 1, "Grow Room {} FFU 2 Equipemnt Failure".format(i))


i = 2
TagAlarm("GR{}".format(i), i*2-1, "Temp", "delta", 2, ">", DT_HI, "Grow Room {} Temperature	deviation High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "Temp", "delta", 2, "<", DT_LO, "Grow Room {} Temperature deviation Low Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "Temp", "value", 2, ">", OOST_HI, "Grow Room {} Temperature Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "Temp", "value", 2, "<", OOST_LO, "Grow Room {} Temperature Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i*2-1, "RH", "delta", 12, ">", DH_HI, "Grow Room {} Relative Humidity deviation High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "RH", "delta", 12, "<", DH_LO, "Grow Room {} Relative Humidity deviation Low Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "RH", "value", 12, ">", OOSH_HI, "Grow Room {} Relative Humidity Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "RH", "value", 12, "<", OOSH_LO,"Grow Room {} Relative Humidity Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i*2-1, "CO2", "delta", 22, ">", DCO2_HI, "Grow Room {} CO2 deviation High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "CO2", "delta", 22, "<", DCO2_LO, "Grow Room {} CO2 deviation Low Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "CO2", "value", 22, ">", OOSCO2_HI, "Grow Room {} CO2 Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "CO2", "value", 22, "<", OOSCO2_LO, "Grow Room {} CO2 Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i*2-1, "DP", "delta", 37, ">", DDP_HI, "Grow Room {} Difference Pressure deviation High Alarm".format(i), sp=0)
TagAlarm("GR{}".format(i), i*2-1, "DP", "delta", 37, "<", DDP_LO, "Grow Room {} Difference Pressure deviation Low Alarm".format(i), sp=0)
TagAlarm("GR{}".format(i), i*2-1, "DP", "value", 37, ">", OOSDP_HI, "Grow Room {} Difference Pressure Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "DP", "value", 37, "<", OOSDP_LO, "Grow Room {} Difference Pressure Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i*2, "Max-Valve", "value", 33, "==", 1, "Grow Room {} Max number of Valves in failure Alarm".format(i)) # digital
TagAlarm("GR{}".format(i), i*2-1, "O2-Life", "value", 38, "<", O2L, "Grow Room {} O2 life safety Low Alarm".format(i))
TagAlarm("GR{}".format(i), i*2-1, "CO2-Life", "value", 39, ">", CO2L, "Grow Room {} CO2 life safety High Alarm".format(i))

TagAlarm("GR{}".format(i), i*2, "AHU 30", "value", 44, "==", 1, "Grow Room {} AHU 30 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "AHU 31", "value", 45, "==", 1, "Grow Room {} AHU 31 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "AHU 32", "value", 46, "==", 1, "Grow Room {} AHU 32 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "AHU 33", "value", 47, "==", 1, "Grow Room {} AHU 33 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "FFU 5", "value", 48, "==", 1, "Grow Room {} FFU 5 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "FFU 6", "value", 49, "==", 1, "Grow Room {} FFU 6 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "Test", "value", 50, "==", 1, "Grow Room {} TestTestTest".format(i)) # test purpose

for i in [3, 4, 5, 6, 7]:
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "delta", 2, ">", DT_HI, "Grow Room {} Temperature	deviation High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "delta", 2, "<", DT_LO, "Grow Room {} Temperature deviation Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "value", 2, ">", OOST_HI, "Grow Room {} Temperature Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "value", 2, "<", OOST_LO, "Grow Room {} Temperature Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2-1, "RH", "delta", 12, ">", DH_HI, "Grow Room {} Relative Humidity deviation High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "RH", "delta", 12, "<", DH_LO, "Grow Room {} Relative Humidity deviation Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "RH", "value", 12, ">", OOSH_HI, "Grow Room {} Relative Humidity Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "RH", "value", 12, "<", OOSH_LO,"Grow Room {} Relative Humidity Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2-1, "CO2", "delta", 22, ">", DCO2_HI, "Grow Room {} CO2 deviation High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "CO2", "delta", 22, "<", DCO2_LO, "Grow Room {} CO2 deviation Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "CO2", "value", 22, ">", OOSCO2_HI, "Grow Room {} CO2 Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "CO2", "value", 22, "<", OOSCO2_LO, "Grow Room {} CO2 Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2-1, "DP", "delta", 37, ">", DDP_HI, "Grow Room {} Difference Pressure deviation High Alarm".format(i), sp=0)
	TagAlarm("GR{}".format(i), i*2-1, "DP", "delta", 37, "<", DDP_LO, "Grow Room {} Difference Pressure deviation Low Alarm".format(i), sp=0)
	TagAlarm("GR{}".format(i), i*2-1, "DP", "value", 37, ">", OOSDP_HI, "Grow Room {} Difference Pressure Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "DP", "value", 37, "<", OOSDP_LO, "Grow Room {} Difference Pressure Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2, "Max-Valve", "value", 33, "==", 1, "Grow Room {} Max number of Valves in failure Alarm".format(i)) # digital
	TagAlarm("GR{}".format(i), i, "O2-Life", "value", 38, "<", O2L, "Grow Room {} O2 life safety Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i, "CO2-Life", "value", 39, ">", CO2L, "Grow Room {} CO2 life safety High Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2, "AHU 1", "value", 44, "==", 1, "Grow Room {} AHU 1 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "AHU 2", "value", 45, "==", 1, "Grow Room {} AHU 2 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "AHU 3", "value", 46, "==", 1, "Grow Room {} AHU 3 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "AHU 4", "value", 47, "==", 1, "Grow Room {} AHU 4 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "FFU 1", "value", 48, "==", 1, "Grow Room {} FFU 1 Equipemnt Failure".format(i))


for i in [8, 9, 10, 11]:
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "delta", 2, ">", DT_HI, "Grow Room {} Temperature	deviation High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "delta", 2, "<", DT_LO, "Grow Room {} Temperature deviation Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "value", 2, ">", OOST_HI, "Grow Room {} Temperature Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "value", 2, "<", OOST_LO, "Grow Room {} Temperature Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2-1, "RH", "delta", 12, ">", DH_HI, "Grow Room {} Relative Humidity deviation High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "RH", "delta", 12, "<", DH_LO, "Grow Room {} Relative Humidity deviation Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "RH", "value", 12, ">", OOSH_HI, "Grow Room {} Relative Humidity Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "RH", "value", 12, "<", OOSH_LO,"Grow Room {} Relative Humidity Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2-1, "CO2", "delta", 22, ">", DCO2_HI, "Grow Room {} CO2 deviation High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "CO2", "delta", 22, "<", DCO2_LO, "Grow Room {} CO2 deviation Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "CO2", "value", 22, ">", OOSCO2_HI, "Grow Room {} CO2 Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "CO2", "value", 22, "<", OOSCO2_LO, "Grow Room {} CO2 Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2-1, "DP", "delta", 37, ">", DDP_HI, "Grow Room {} Difference Pressure deviation High Alarm".format(i), sp=0)
	TagAlarm("GR{}".format(i), i*2-1, "DP", "delta", 37, "<", DDP_LO, "Grow Room {} Difference Pressure deviation Low Alarm".format(i), sp=0)
	TagAlarm("GR{}".format(i), i*2-1, "DP", "value", 37, ">", OOSDP_HI, "Grow Room {} Difference Pressure Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "DP", "value", 37, "<", OOSDP_LO, "Grow Room {} Difference Pressure Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2, "Max-Valve", "value", 33, "==", 1, "Grow Room {} Max number of Valves in failure Alarm".format(i)) # digital
	TagAlarm("GR{}".format(i), i, "O2-Life", "value", 38, "<", O2L, "Grow Room {} O2 life safety Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i, "CO2-Life", "value", 39, ">", CO2L, "Grow Room {} CO2 life safety High Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2, "AHU 1", "value", 44, "==", 1, "Grow Room {} AHU 1 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "AHU 2", "value", 45, "==", 1, "Grow Room {} AHU 2 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "AHU 3", "value", 46, "==", 1, "Grow Room {} AHU 3 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "AHU 4", "value", 47, "==", 1, "Grow Room {} AHU 4 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "FFU 1", "value", 48, "==", 1, "Grow Room {} FFU 1 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "FFU 2", "value", 49, "==", 1, "Grow Room {} FFU 2 Equipemnt Failure".format(i))

for i in [12, 13]:
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "delta", 2, ">", DT_HI, "Grow Room {} Temperature	deviation High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "delta", 2, "<", DT_LO, "Grow Room {} Temperature deviation Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "value", 2, ">", OOST_HI, "Grow Room {} Temperature Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "value", 2, "<", OOST_LO, "Grow Room {} Temperature Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2-1, "RH", "delta", 12, ">", DH_HI, "Grow Room {} Relative Humidity deviation High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "RH", "delta", 12, "<", DH_LO, "Grow Room {} Relative Humidity deviation Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "RH", "value", 12, ">", OOSH_HI, "Grow Room {} Relative Humidity Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "RH", "value", 12, "<", OOSH_LO,"Grow Room {} Relative Humidity Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2-1, "CO2", "delta", 22, ">", DCO2_HI, "Grow Room {} CO2 deviation High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "CO2", "delta", 22, "<", DCO2_LO, "Grow Room {} CO2 deviation Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "CO2", "value", 22, ">", OOSCO2_HI, "Grow Room {} CO2 Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "CO2", "value", 22, "<", OOSCO2_LO, "Grow Room {} CO2 Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2-1, "DP", "delta", 37, ">", DDP_HI, "Grow Room {} Difference Pressure deviation High Alarm".format(i), sp=0)
	TagAlarm("GR{}".format(i), i*2-1, "DP", "delta", 37, "<", DDP_LO, "Grow Room {} Difference Pressure deviation Low Alarm".format(i), sp=0)
	TagAlarm("GR{}".format(i), i*2-1, "DP", "value", 37, ">", OOSDP_HI, "Grow Room {} Difference Pressure Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "DP", "value", 37, "<", OOSDP_LO, "Grow Room {} Difference Pressure Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2, "Max-Valve", "value", 33, "==", 1, "Grow Room {} Max number of Valves in failure Alarm".format(i)) # digital
	TagAlarm("GR{}".format(i), i, "O2-Life", "value", 38, "<", O2L, "Grow Room {} O2 life safety Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i, "CO2-Life", "value", 39, ">", CO2L, "Grow Room {} CO2 life safety High Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2, "AHU 1", "value", 44, "==", 1, "Grow Room {} AHU 1 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "AHU 2", "value", 45, "==", 1, "Grow Room {} AHU 2 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "FFU 1", "value", 46, "==", 1, "Grow Room {} FFU 1 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "FFU 2", "value", 47, "==", 1, "Grow Room {} FFU 2 Equipemnt Failure".format(i))

for i in [14, 15, 16, 17]:
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "delta", 2, ">", DT_HI, "Grow Room {} Temperature	deviation High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "delta", 2, "<", DT_LO, "Grow Room {} Temperature deviation Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "value", 2, ">", OOST_HI, "Grow Room {} Temperature Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "Temp", "value", 2, "<", OOST_LO, "Grow Room {} Temperature Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2-1, "RH", "delta", 12, ">", DH_HI, "Grow Room {} Relative Humidity deviation High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "RH", "delta", 12, "<", DH_LO, "Grow Room {} Relative Humidity deviation Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "RH", "value", 12, ">", OOSH_HI, "Grow Room {} Relative Humidity Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "RH", "value", 12, "<", OOSH_LO,"Grow Room {} Relative Humidity Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2-1, "CO2", "delta", 22, ">", DCO2_HI, "Grow Room {} CO2 deviation High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "CO2", "delta", 22, "<", DCO2_LO, "Grow Room {} CO2 deviation Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "CO2", "value", 22, ">", OOSCO2_HI, "Grow Room {} CO2 Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "CO2", "value", 22, "<", OOSCO2_LO, "Grow Room {} CO2 Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2-1, "DP", "delta", 37, ">", DDP_HI, "Grow Room {} Difference Pressure deviation High Alarm".format(i), sp=0)
	TagAlarm("GR{}".format(i), i*2-1, "DP", "delta", 37, "<", DDP_LO, "Grow Room {} Difference Pressure deviation Low Alarm".format(i), sp=0)
	TagAlarm("GR{}".format(i), i*2-1, "DP", "value", 37, ">", OOSDP_HI, "Grow Room {} Difference Pressure Out of Spec High Alarm".format(i))
	TagAlarm("GR{}".format(i), i*2-1, "DP", "value", 37, "<", OOSDP_LO, "Grow Room {} Difference Pressure Out of Spec Low Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2, "Max-Valve", "value", 33, "==", 1, "Grow Room {} Max number of Valves in failure Alarm".format(i)) # digital
	TagAlarm("GR{}".format(i), i, "O2-Life", "value", 38, "<", O2L, "Grow Room {} O2 life safety Low Alarm".format(i))
	TagAlarm("GR{}".format(i), i, "CO2-Life", "value", 39, ">", CO2L, "Grow Room {} CO2 life safety High Alarm".format(i))

	TagAlarm("GR{}".format(i), i*2, "AHU 1", "value", 44, "==", 1, "Grow Room {} AHU 1 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "AHU 2", "value", 45, "==", 1, "Grow Room {} AHU 2 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "AHU 3", "value", 46, "==", 1, "Grow Room {} AHU 3 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "AHU 4", "value", 47, "==", 1, "Grow Room {} AHU 4 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "FFU 1", "value", 48, "==", 1, "Grow Room {} FFU 1 Equipemnt Failure".format(i))
	TagAlarm("GR{}".format(i), i*2, "FFU 2", "value", 49, "==", 1, "Grow Room {} FFU 2 Equipemnt Failure".format(i))

# LV
i = 18
DT_HI = 5
DT_LO = -5
OOST_HI = 30
OOST_LO = 18

DH_HI = 10
DH_LO = -10
OOSH_HI = 70
OOSH_LO = 40

DCO2_HI = 2000
DCO2_LO = -300
OOSCO2_HI = 2000
OOSCO2_LO = 300

DDP_HI = 0.3
DDP_LO = -0.3
OOSDP_HI = 0.3
OOSDP_LO = -0.3
O2L = 9
CO2L = 3500
TagAlarm("Large Veg", i*2-1, "Temp", "delta", 2, ">", DT_HI, "Large Veg Temperature	deviation High Alarm")
TagAlarm("Large Veg", i*2-1, "Temp", "delta", 2, "<", DT_LO, "Large Veg Temperature deviation Low Alarm")
TagAlarm("Large Veg", i*2-1, "Temp", "value", 2, ">", OOST_HI, "Large Veg Temperature Out of Spec High Alarm")
TagAlarm("Large Veg", i*2-1, "Temp", "value", 2, "<", OOST_LO, "Large Veg Temperature Out of Spec Low Alarm")

TagAlarm("Large Veg", i*2-1, "RH", "delta", 12, ">", DH_HI, "Large Veg Relative Humidity deviation High Alarm")
TagAlarm("Large Veg", i*2-1, "RH", "delta", 12, "<", DH_LO, "Large Veg Relative Humidity deviation Low Alarm")
TagAlarm("Large Veg", i*2-1, "RH", "value", 12, ">", OOSH_HI, "Large Veg Relative Humidity Out of Spec High Alarm")
TagAlarm("Large Veg", i*2-1, "RH", "value", 12, "<", OOSH_LO,"Large Veg Relative Humidity Out of Spec Low Alarm")

TagAlarm("Large Veg", i*2-1, "CO2", "delta", 22, ">", DCO2_HI, "Large Veg CO2 deviation High Alarm")
TagAlarm("Large Veg", i*2-1, "CO2", "delta", 22, "<", DCO2_LO, "Large Veg CO2 deviation Low Alarm")
TagAlarm("Large Veg", i*2-1, "CO2", "value", 22, ">", OOSCO2_HI, "Large Veg CO2 Out of Spec High Alarm")
TagAlarm("Large Veg", i*2-1, "CO2", "value", 22, "<", OOSCO2_LO, "Large Veg CO2 Out of Spec Low Alarm")

TagAlarm("Large Veg", i*2-1, "DP", "delta", 37, ">", DDP_HI, "Large Veg Difference Pressure deviation High Alarm", sp=0)
TagAlarm("Large Veg", i*2-1, "DP", "delta", 37, "<", DDP_LO, "Large Veg Difference Pressure deviation Low Alarm", sp=0)
TagAlarm("Large Veg", i*2-1, "DP", "value", 37, ">", OOSDP_HI, "Large Veg Difference Pressure Out of Spec High Alarm")
TagAlarm("Large Veg", i*2-1, "DP", "value", 37, "<", OOSDP_LO, "Large Veg Difference Pressure Out of Spec Low Alarm")

TagAlarm("Large Veg", i*2, "Max-Valve", "value", 33, "==", 1, "Large Veg Max number of Valves in failure Alarm") # digital
TagAlarm("Large Veg", i, "O2-Life", "value", 38, "<", O2L, "Large Veg O2 life safety Low Alarm")
TagAlarm("Large Veg", i, "CO2-Life", "value", 39, ">", CO2L, "Large Veg CO2 life safety High Alarm")

TagAlarm("Large Veg", i*2, "AHU 1", "value", 44, "==", 1, "Large Veg AHU 1 Equipemnt Failure")
TagAlarm("Large Veg", i*2, "AHU 2", "value", 45, "==", 1, "Large Veg AHU 2 Equipemnt Failure")
TagAlarm("Large Veg", i*2, "AHU 3", "value", 46, "==", 1, "Large Veg AHU 3 Equipemnt Failure")

# MR
i = 19
DT_HI = 5
DT_LO = -5
OOST_HI = 28
OOST_LO = 18

DH_HI = 10
DH_LO = -10
OOSH_HI = 70
OOSH_LO = 40

DCO2_HI = 2000
DCO2_LO = -300
OOSCO2_HI = 2000
OOSCO2_LO = 300

DDP_HI = 0.3
DDP_LO = -0.3
OOSDP_HI = 0.3
OOSDP_LO = -0.3
O2L = 9
CO2L = 3500
TagAlarm("Mother Room", i*2-1, "Temp", "delta", 2, ">", DT_HI, "Mother Room Temperature	deviation High Alarm")
TagAlarm("Mother Room", i*2-1, "Temp", "delta", 2, "<", DT_LO, "Mother Room Temperature deviation Low Alarm")
TagAlarm("Mother Room", i*2-1, "Temp", "value", 2, ">", OOST_HI, "Mother Room Temperature Out of Spec High Alarm")
TagAlarm("Mother Room", i*2-1, "Temp", "value", 2, "<", OOST_LO, "Mother Room Temperature Out of Spec Low Alarm")

TagAlarm("Mother Room", i*2-1, "RH", "delta", 12, ">", DH_HI, "Mother Room Relative Humidity deviation High Alarm")
TagAlarm("Mother Room", i*2-1, "RH", "delta", 12, "<", DH_LO, "Mother Room Relative Humidity deviation Low Alarm")
TagAlarm("Mother Room", i*2-1, "RH", "value", 12, ">", OOSH_HI, "Mother Room Relative Humidity Out of Spec High Alarm")
TagAlarm("Mother Room", i*2-1, "RH", "value", 12, "<", OOSH_LO,"Mother Room Relative Humidity Out of Spec Low Alarm")

TagAlarm("Mother Room", i*2-1, "CO2", "delta", 22, ">", DCO2_HI, "Mother Room CO2 deviation High Alarm")
TagAlarm("Mother Room", i*2-1, "CO2", "delta", 22, "<", DCO2_LO, "Mother Room CO2 deviation Low Alarm")
TagAlarm("Mother Room", i*2-1, "CO2", "value", 22, ">", OOSCO2_HI, "Mother Room CO2 Out of Spec High Alarm")
TagAlarm("Mother Room", i*2-1, "CO2", "value", 22, "<", OOSCO2_LO, "Mother Room CO2 Out of Spec Low Alarm")

TagAlarm("Mother Room", i*2-1, "DP", "delta", 37, ">", DDP_HI, "Mother Room Difference Pressure deviation High Alarm", sp=0)
TagAlarm("Mother Room", i*2-1, "DP", "delta", 37, "<", DDP_LO, "Mother Room Difference Pressure deviation Low Alarm", sp=0)
TagAlarm("Mother Room", i*2-1, "DP", "value", 37, ">", OOSDP_HI, "Mother Room Difference Pressure Out of Spec High Alarm")
TagAlarm("Mother Room", i*2-1, "DP", "value", 37, "<", OOSDP_LO, "Mother Room Difference Pressure Out of Spec Low Alarm")

TagAlarm("Mother Room", i*2, "Max-Valve", "value", 33, "==", 1, "Mother Room Max number of Valves in failure Alarm") # digital
TagAlarm("Mother Room", i, "O2-Life", "value", 38, "<", O2L, "Mother Room O2 life safety Low Alarm")
TagAlarm("Mother Room", i, "CO2-Life", "value", 39, ">", CO2L, "Mother Room CO2 life safety High Alarm")

TagAlarm("Mother Room", i*2, "AHU 5", "value", 44, "==", 1, "Mother Room AHU 5 Equipemnt Failure")
TagAlarm("Mother Room", i*2, "AHU 6", "value", 45, "==", 1, "Mother Room AHU 6 Equipemnt Failure")
TagAlarm("Mother Room", i*2, "FFU 7", "value", 46, "==", 1, "Mother Room FFU 7 Equipemnt Failure")

# CR
i = 20
DT_HI = 5
DT_LO = -5
OOST_HI = 28
OOST_LO = 23

DH_HI = 10
DH_LO = -10
OOSH_HI = 80
OOSH_LO = 60

DCO2_HI = 2000
DCO2_LO = -300
OOSCO2_HI = 2000
OOSCO2_LO = 300

DDP_HI = 0.3
DDP_LO = -0.3
OOSDP_HI = 0.3
OOSDP_LO = -0.3
O2L = 9
CO2L = 3500
TagAlarm("Clone Room", i*2-1, "Temp", "delta", 2, ">", DT_HI, "Clone Room Temperature	deviation High Alarm")
TagAlarm("Clone Room", i*2-1, "Temp", "delta", 2, "<", DT_LO, "Clone Room Temperature deviation Low Alarm")
TagAlarm("Clone Room", i*2-1, "Temp", "value", 2, ">", OOST_HI, "Clone Room Temperature Out of Spec High Alarm")
TagAlarm("Clone Room", i*2-1, "Temp", "value", 2, "<", OOST_LO, "Clone Room Temperature Out of Spec Low Alarm")

TagAlarm("Clone Room", i*2-1, "RH", "delta", 12, ">", DH_HI, "Clone Room Relative Humidity deviation High Alarm")
TagAlarm("Clone Room", i*2-1, "RH", "delta", 12, "<", DH_LO, "Clone Room Relative Humidity deviation Low Alarm")
TagAlarm("Clone Room", i*2-1, "RH", "value", 12, ">", OOSH_HI, "Clone Room Relative Humidity Out of Spec High Alarm")
TagAlarm("Clone Room", i*2-1, "RH", "value", 12, "<", OOSH_LO,"Clone Room Relative Humidity Out of Spec Low Alarm")

TagAlarm("Clone Room", i*2-1, "CO2", "delta", 22, ">", DCO2_HI, "Clone Room CO2 deviation High Alarm")
TagAlarm("Clone Room", i*2-1, "CO2", "delta", 22, "<", DCO2_LO, "Clone Room CO2 deviation Low Alarm")
TagAlarm("Clone Room", i*2-1, "CO2", "value", 22, ">", OOSCO2_HI, "Clone Room CO2 Out of Spec High Alarm")
TagAlarm("Clone Room", i*2-1, "CO2", "value", 22, "<", OOSCO2_LO, "Clone Room CO2 Out of Spec Low Alarm")

TagAlarm("Clone Room", i*2-1, "DP", "delta", 37, ">", DDP_HI, "Clone Room Difference Pressure deviation High Alarm", sp=0)
TagAlarm("Clone Room", i*2-1, "DP", "delta", 37, "<", DDP_LO, "Clone Room Difference Pressure deviation Low Alarm", sp=0)
TagAlarm("Clone Room", i*2-1, "DP", "value", 37, ">", OOSDP_HI, "Clone Room Difference Pressure Out of Spec High Alarm")
TagAlarm("Clone Room", i*2-1, "DP", "value", 37, "<", OOSDP_LO, "Clone Room Difference Pressure Out of Spec Low Alarm")

# TagAlarm("Clone Room", i*2, "Max-Valve", "value", 33, "==", 1, "Clone Room Max number of Valves in failure Alarm") # digital
TagAlarm("Clone Room", i, "O2-Life", "value", 38, "<", O2L, "Clone Room O2 life safety Low Alarm")
TagAlarm("Clone Room", i, "CO2-Life", "value", 39, ">", CO2L, "Clone Room CO2 life safety High Alarm")

TagAlarm("Clone Room", i*2, "AHU 7", "value", 44, "==", 1, "Clone Room AHU 7 Equipemnt Failure")
TagAlarm("Clone Room", i*2, "AHU 8", "value", 45, "==", 1, "Clone Room AHU 8 Equipemnt Failure")
TagAlarm("Clone Room", i*2, "FFU 11", "value", 46, "==", 1, "Clone Room FFU 11 Equipemnt Failure")

# Panel55_DR1607_TR1608
i = 21
DT_HI = 5
DT_LO = -5
OOST_HI = 26
OOST_LO = 18

DH_HI = 10
DH_LO = -10
OOSH_HI = 70
OOSH_LO = 40

TagAlarm("DR1607", i*2-1, "Temp", "delta", 2, ">", DT_HI, "DR1607 Temperature	deviation High Alarm")
TagAlarm("DR1607", i*2-1, "Temp", "delta", 2, "<", DT_LO, "DR1607 Temperature deviation Low Alarm")
TagAlarm("DR1607", i*2-1, "Temp", "value", 2, ">", OOST_HI, "DR1607 Temperature Out of Spec High Alarm")
TagAlarm("DR1607", i*2-1, "Temp", "value", 2, "<", OOST_LO, "DR1607 Temperature Out of Spec Low Alarm")

TagAlarm("DR1607", i*2-1, "RH", "delta", 6, ">", DH_HI, "DR1607 Relative Humidity deviation High Alarm")
TagAlarm("DR1607", i*2-1, "RH", "delta", 6, "<", DH_LO, "DR1607 Relative Humidity deviation Low Alarm")
TagAlarm("DR1607", i*2-1, "RH", "value", 6, ">", OOSH_HI, "DR1607 Relative Humidity Out of Spec High Alarm")
TagAlarm("DR1607", i*2-1, "RH", "value", 6, "<", OOSH_LO,"DR1607 Relative Humidity Out of Spec Low Alarm")

DT_HI = 5
DT_LO = -5
OOST_HI = 22
OOST_LO = 17

DH_HI = 10
DH_LO = -10
OOSH_HI = 65
OOSH_LO = 40

TagAlarm("TR1608", i*2-1, "Temp", "delta", 4, ">", DT_HI, "TR1608 Temperature	deviation High Alarm")
TagAlarm("TR1608", i*2-1, "Temp", "delta", 4, "<", DT_LO, "TR1608 Temperature deviation Low Alarm")
TagAlarm("TR1608", i*2-1, "Temp", "value", 4, ">", OOST_HI, "TR1608 Temperature Out of Spec High Alarm")
TagAlarm("TR1608", i*2-1, "Temp", "value", 4, "<", OOST_LO, "TR1608 Temperature Out of Spec Low Alarm")

TagAlarm("TR1608", i*2-1, "RH", "delta", 8, ">", DH_HI, "TR1608 Relative Humidity deviation High Alarm")
TagAlarm("TR1608", i*2-1, "RH", "delta", 8, "<", DH_LO, "TR1608 Relative Humidity deviation Low Alarm")
TagAlarm("TR1608", i*2-1, "RH", "value", 8, ">", OOSH_HI, "TR1608 Relative Humidity Out of Spec High Alarm")
TagAlarm("TR1608", i*2-1, "RH", "value", 8, "<", OOSH_LO,"TR1608 Relative Humidity Out of Spec Low Alarm")

# ***********************************************************************************************
DDP_HI = 0.3
DDP_LO = -0.3
OOSDP_HI = 0.3
OOSDP_LO = -0.3
for index, name in enumerate(["DR1607 vs WC", "DR1607 vs AL1606", "DR1607 vs AL1605", "DR1607 vs AL1608", "TR1608 vs WC", "TR1608 vs AL1609", "TR1608 vs AL1610", "TR1608 vs AL1607", "TR1608 vs AL1611"]):
	TagAlarm(name, i*2-1, "DP", "delta", index+9, ">", DDP_HI, "{} Difference Pressure deviation High Alarm".format(name), sp=0)
	TagAlarm(name, i*2-1, "DP", "delta", index+9, "<", DDP_LO, "{} Difference Pressure deviation Low Alarm".format(name), sp=0)
	TagAlarm(name, i*2-1, "DP", "value", index+9, ">", OOSDP_HI, "{} Difference Pressure Out of Spec High Alarm".format(name))
	TagAlarm(name, i*2-1, "DP", "value", index+9, "<", OOSDP_LO, "{} Difference Pressure Out of Spec Low Alarm".format(name))

TagAlarm("DR1607", i*2, "AHU 1", "value", 1, "==", 1, "DR1607 AHU 1 Equipemnt Failure")
TagAlarm("DR1607", i*2, "AHU 2", "value", 2, "==", 1, "DR1607 AHU 2 Equipemnt Failure")
TagAlarm("TR1608", i*2, "AHU 1", "value", 3, "==", 1, "TR1608 AHU 1 Equipemnt Failure")


i = 43
# DR1611
TagAlarm("DR1611", i, "AHU 1", "value", 1, "==", 1, "DR1611 AHU 3 Equipemnt Failure")
TagAlarm("DR1611", i, "AHU 2", "value", 2, "==", 1, "DR1611 FFU 1 Equipemnt Failure")
TagAlarm("DR1611", i, "AHU 1", "value", 3, "==", 1, "DR1611 MAU 1 Equipemnt Failure")

i = 44# 45
# Boiler Plants & Dosing Unit

# BP1
DT_HI = 5
DT_LO = -5
GLYCOL_HI = 10
GLYCOL_LO = 10
TagAlarm("BP1", i, "Temp", "delta", 4, ">", DT_HI, "BP1 Supply Temperature deviation High Alarm")
TagAlarm("BP1", i, "Temp", "delta", 4, "<", DT_LO, "BP1 Supply Temperature deviation Low Alarm")

a = TagAlarm("BP1", i, "Glycol Pressure", "value", 1, ">", GLYCOL_HI, "BP1 Glycol Pressure deviation High Alarm").return_tag("BP1", "Glycol Pressure", "value")
a.tag_scale_10()
a.set_tag_unit("inH2O")
a = TagAlarm("BP1", i, "Glycol Pressure", "value", 1, "<", GLYCOL_LO, "BP1 Glycol Pressure deviation Low Alarm").return_tag("BP1", "Glycol Pressure", "value")


TagAlarm("BP1", i+1, "B1", "value", 1, "==", 1, "BP1 B1 Equipemnt Failure")
TagAlarm("BP1", i+1, "B2", "value", 2, "==", 1, "BP1 B2 Equipemnt Failure")
TagAlarm("BP1", i+1, "B3", "value", 3, "==", 1, "BP1 B3 Equipemnt Failure")
TagAlarm("BP1", i+1, "B4", "value", 4, "==", 1, "BP1 B4 Equipemnt Failure")
TagAlarm("BP1", i+1, "B5", "value", 5, "==", 1, "BP1 B5 Equipemnt Failure")
TagAlarm("BP1", i+1, "B6", "value", 6, "==", 1, "BP1 B6 Equipemnt Failure")

TagAlarm("BP1", i+1, "P1", "value", 13, "==", 1, "BP1 Pump 1 Equipemnt Failure")
TagAlarm("BP1", i+1, "P2", "value", 14, "==", 1, "BP1 Pump 2 Equipemnt Failure")

# BP2
DT_HI = 5
DT_LO = -5
GLYCOL_HI = 10
GLYCOL_LO = 10
TagAlarm("BP2", i, "Temp", "delta", 6, ">", DT_HI, "BP2 Supply Temperature deviation High Alarm")
TagAlarm("BP2", i, "Temp", "delta", 6, "<", DT_LO, "BP2 Supply Temperature deviation Low Alarm")

a = TagAlarm("BP2", i, "Glycol Pressure", "value", 2, ">", GLYCOL_HI, "BP2 Glycol Pressure deviation High Alarm").return_tag("BP2", "Glycol Pressure", "value")
a.tag_scale_10()
a.set_tag_unit("inH2O")
a = TagAlarm("BP2", i, "Glycol Pressure", "value", 2, "<", GLYCOL_LO, "BP2 Glycol Pressure deviation Low Alarm").return_tag("BP2", "Glycol Pressure", "value")


TagAlarm("BP2", i+1, "B7", "value", 7, "==", 1, "BP2 B7 Equipemnt Failure")
TagAlarm("BP2", i+1, "B8", "value", 8, "==", 1, "BP2 B8 Equipemnt Failure")
TagAlarm("BP2", i+1, "B9", "value", 9, "==", 1, "BP2 B9 Equipemnt Failure")
TagAlarm("BP2", i+1, "B10", "value", 10, "==", 1, "BP2 B10 Equipemnt Failure")
TagAlarm("BP2", i+1, "B11", "value", 11, "==", 1, "BP2 B11 Equipemnt Failure")
TagAlarm("BP2", i+1, "B12", "value", 12, "==", 1, "BP2 B12 Equipemnt Failure")

TagAlarm("BP2", i+1, "P3", "value", 15, "==", 1, "BP2 Pump 3 Equipemnt Failure")
TagAlarm("BP2", i+1, "P4", "value", 16, "==", 1, "BP2 Pump 4 Equipemnt Failure")

TagAlarm("BP1", i+1, "AHU18", "value", 17, "==", 1, "Boiler Plant AHU18 Equipemnt Failure")
TagAlarm("BP1", i+1, "FFU3", "value", 18, "==", 1, "Boiler Plant FFU3 Equipemnt Failure")

TagAlarm("BR1", i+1, "Leak Det 1", "value", 19, "==", 1, "BR1 Leak Detector 1 Failure")
TagAlarm("BR1", i+1, "Leak Det 2", "value", 20, "==", 1, "BR1 Leak Detector 2 Failure")
TagAlarm("BR1", i+1, "Leak Det 3", "value", 21, "==", 1, "BR1 Leak Detector 3 Failure")
TagAlarm("BR1", i+1, "Leak Det 4", "value", 22, "==", 1, "BR1 Leak Detector 4 Failure")

# BP3
DT_HI = 5
DT_LO = -5
GLYCOL_HI = 10
GLYCOL_LO = 10
TagAlarm("BP3", i, "Temp", "delta", 9, ">", DT_HI, "BP3 Supply Temperature deviation High Alarm")
TagAlarm("BP3", i, "Temp", "delta", 9, "<", DT_LO, "BP3 Supply Temperature deviation Low Alarm")

a = TagAlarm("BP3", i, "Glycol Pressure", "value", 7, ">", GLYCOL_HI, "BP3 Glycol Pressure deviation High Alarm").return_tag("BP3", "Glycol Pressure", "value")
a.tag_scale_10()
a.set_tag_unit("inH2O")
a = TagAlarm("BP3", i, "Glycol Pressure", "value", 7, "<", GLYCOL_LO, "BP3 Glycol Pressure deviation Low Alarm").return_tag("BP3", "Glycol Pressure", "value")

TagAlarm("BP3", i+1, "B13", "value", 23, "==", 1, "BP3 B13 Equipemnt Failure")
TagAlarm("BP3", i+1, "B14", "value", 24, "==", 1, "BP3 B14 Equipemnt Failure")
TagAlarm("BP3", i+1, "B15", "value", 25, "==", 1, "BP3 B15 Equipemnt Failure")
TagAlarm("BP3", i+1, "B16", "value", 26, "==", 1, "BP3 B16 Equipemnt Failure")
TagAlarm("BP3", i+1, "B17", "value", 27, "==", 1, "BP3 B17 Equipemnt Failure")
TagAlarm("BP3", i+1, "B18", "value", 28, "==", 1, "BP3 B18 Equipemnt Failure")
TagAlarm("BP3", i+1, "B19", "value", 29, "==", 1, "BP3 B19 Equipemnt Failure")
TagAlarm("BP3", i+1, "B20", "value", 30, "==", 1, "BP3 B20 Equipemnt Failure")

TagAlarm("BP3", i+1, "P5", "value", 31, "==", 1, "BP3 Pump 5 Equipemnt Failure")
TagAlarm("BP3", i+1, "P6", "value", 32, "==", 1, "BP3 Pump 6 Equipemnt Failure")

TagAlarm("BR2", i+1, "Leak Det 1", "value", 33, "==", 1, "BR2 Leak Detector 1 Failure")
TagAlarm("BR2", i+1, "Leak Det 2", "value", 34, "==", 1, "BR2 Leak Detector 2 Failure")
TagAlarm("BR2", i+1, "Leak Det 3", "value", 35, "==", 1, "BR2 Leak Detector 3 Failure")
TagAlarm("BR2", i+1, "Leak Det 4", "value", 36, "==", 1, "BR2 Leak Detector 4 Failure")

# BP4
DT_HI = 5
DT_LO = -5
GLYCOL_HI = 10
GLYCOL_LO = 10
TagAlarm("BP4", i, "Temp", "delta", 12, ">", DT_HI, "BP4 Supply Temperature deviation High Alarm")
TagAlarm("BP4", i, "Temp", "delta", 12, "<", DT_LO, "BP4 Supply Temperature deviation Low Alarm")

a = TagAlarm("BP4", i, "Glycol Pressure", "value", 10, ">", GLYCOL_HI, "BP4 Glycol Pressure deviation High Alarm").return_tag("BP4", "Glycol Pressure", "value")
a.tag_scale_10()
a.set_tag_unit("inH2O")
a = TagAlarm("BP4", i, "Glycol Pressure", "value", 10, "<", GLYCOL_LO, "BP4 Glycol Pressure deviation Low Alarm").return_tag("BP4", "Glycol Pressure", "value")


TagAlarm("BP4", i+1, "B21", "value", 37, "==", 1, "BP4 B13 Equipemnt Failure")
TagAlarm("BP4", i+1, "B22", "value", 38, "==", 1, "BP4 B14 Equipemnt Failure")
TagAlarm("BP4", i+1, "B23", "value", 39, "==", 1, "BP4 B15 Equipemnt Failure")
TagAlarm("BP4", i+1, "B24", "value", 40, "==", 1, "BP4 B16 Equipemnt Failure")


TagAlarm("BP4", i+1, "P7", "value", 41, "==", 1, "BP4 Pump 7 Equipemnt Failure")
TagAlarm("BP4", i+1, "P8", "value", 42, "==", 1, "BP4 Pump 8 Equipemnt Failure")
TagAlarm("BP4", i+1, "P9", "value", 43, "==", 1, "BP4 Pump 9 Equipemnt Failure")

TagAlarm("BR3", i+1, "Leak Det 1", "value", 45, "==", 1, "BR3 Leak Detector 1 Failure")
TagAlarm("BR3", i+1, "Leak Det 2", "value", 46, "==", 1, "BR3 Leak Detector 2 Failure")
TagAlarm("BR3", i+1, "Leak Det 3", "value", 47, "==", 1, "BR3 Leak Detector 3 Failure")
TagAlarm("BR3", i+1, "Leak Det 4", "value", 48, "==", 1, "BR3 Leak Detector 4 Failure")

TagAlarm("Large Veg", i+1, "Dosing Unit", "value", 49, "==", 1, "Dosing Unit Large Veg Failure")


# ChilledWater
i = 46 
TagAlarm("Condenser Pump", i, "CP-3", "value", 1, "==", 1, "Condenser Pump CP-3 Equipemnt Failure")
TagAlarm("Condenser Pump", i, "CP-4", "value", 2, "==", 1, "Condenser Pump CP-4 Equipemnt Failure")
TagAlarm("Condenser Pump", i, "CP-5", "value", 3, "==", 1, "Condenser Pump CP-5 Equipemnt Failure")
TagAlarm("Cooling Tower", i, "2A", "value", 4, "==", 1, "Cooling Tower 2A Equipemnt Failure")
TagAlarm("Cooling Tower", i, "2B", "value", 5, "==", 1, "Cooling Tower 2B Equipemnt Failure")
TagAlarm("Cooling Tower", i, "2C", "value", 6, "==", 1, "Cooling Tower 2C Equipemnt Failure")

# DR1512 DR1513
i = 47
TagAlarm("DR1512", i, "AHU 4", "value", 1, "==", 1, "DR1512 AHU 4 Equipemnt Failure")
TagAlarm("DR1512", i, "AHU 5", "value", 2, "==", 1, "DR1512 AHU 5 Equipemnt Failure")
TagAlarm("DR1513", i, "AHU 6", "value", 3, "==", 1, "DR1513 AHU 6 Equipemnt Failure")
TagAlarm("DR1513", i, "AHU 7", "value", 4, "==", 1, "DR1513 AHU 7 Equipemnt Failure")
TagAlarm("DR1512/1513", i, "FFU 1", "value", 5, "==", 1, "DR1512/1513 FFU 1 Equipemnt Failure")

# MUA5
i = 48
TagAlarm("MUA5", i, "MUA5", "value", 1, "==", 1, "MUA5 Equipemnt Failure")

# MUA4
i = 49
DT_HI = 5
DT_LO = -5
OOST_HI = 28
OOST_LO = 23

DH_HI = 10
DH_LO = -10
OOSH_HI = 80
OOSH_LO = 60

DDP_HI = 0.3
DDP_LO = -0.3
OOSDP_HI = 0.3
OOSDP_LO = -0.3

TagAlarm("Gummy", i, "Temp", "delta", 2, ">", DT_HI, "Gummy Temperature	deviation High Alarm")
TagAlarm("Gummy", i, "Temp", "delta", 2, "<", DT_LO, "Gummy Temperature deviation Low Alarm")
TagAlarm("Gummy", i, "Temp", "value", 2, ">", OOST_HI, "Gummy Temperature Out of Spec High Alarm")
TagAlarm("Gummy", i, "Temp", "value", 2, "<", OOST_LO, "Gummy Temperature Out of Spec Low Alarm")

TagAlarm("Gummy", i, "RH", "delta", 4, ">", DH_HI, "Gummy Relative Humidity deviation High Alarm")
TagAlarm("Gummy", i, "RH", "delta", 4, "<", DH_LO, "Gummy Relative Humidity deviation Low Alarm")
TagAlarm("Gummy", i, "RH", "value", 4, ">", OOSH_HI, "Gummy Relative Humidity Out of Spec High Alarm")
TagAlarm("Gummy", i, "RH", "value", 4, "<", OOSH_LO,"Gummy Relative Humidity Out of Spec Low Alarm")

TagAlarm("Gummy", i, "DP", "delta", 5, ">", DDP_HI, "Gummy Difference Pressure deviation High Alarm", sp=0)
TagAlarm("Gummy", i, "DP", "delta", 5, "<", DDP_LO, "Gummy Difference Pressure deviation Low Alarm", sp=0)
TagAlarm("Gummy", i, "DP", "value", 5, ">", OOSDP_HI, "Gummy Difference Pressure Out of Spec High Alarm")
TagAlarm("Gummy", i, "DP", "value", 5, "<", OOSDP_LO, "Gummy Difference Pressure Out of Spec Low Alarm")

TagAlarm("AL1101", i, "DP", "delta", 6, ">", DDP_HI, "AL1101 Difference Pressure deviation High Alarm", sp=0)
TagAlarm("AL1101", i, "DP", "delta", 6, "<", DDP_LO, "AL1101 Difference Pressure deviation Low Alarm", sp=0)
TagAlarm("AL1101", i, "DP", "value", 6, ">", OOSDP_HI, "AL1101 Difference Pressure Out of Spec High Alarm")
TagAlarm("AL1101", i, "DP", "value", 6, "<", OOSDP_LO, "AL1101 Difference Pressure Out of Spec Low Alarm")

TagAlarm("AL1102", i, "DP", "delta", 7, ">", DDP_HI, "AL1102 Difference Pressure deviation High Alarm", sp=0)
TagAlarm("AL1102", i, "DP", "delta", 7, "<", DDP_LO, "AL1102 Difference Pressure deviation Low Alarm", sp=0)
TagAlarm("AL1102", i, "DP", "value", 7, ">", OOSDP_HI, "AL1102 Difference Pressure Out of Spec High Alarm")
TagAlarm("AL1102", i, "DP", "value", 7, "<", OOSDP_LO, "AL1102 Difference Pressure Out of Spec Low Alarm")

TagAlarm("AL1104", i, "DP", "delta", 8, ">", DDP_HI, "AL1104 Difference Pressure deviation High Alarm", sp=0)
TagAlarm("AL1104", i, "DP", "delta", 8, "<", DDP_LO, "AL1104 Difference Pressure deviation Low Alarm", sp=0)
TagAlarm("AL1104", i, "DP", "value", 8, ">", OOSDP_HI, "AL1104 Difference Pressure Out of Spec High Alarm")
TagAlarm("AL1104", i, "DP", "value", 8, "<", OOSDP_LO, "AL1104 Difference Pressure Out of Spec Low Alarm")

TagAlarm("Gummy", i+1, "MUA4", "value", 1, "==", 1, "Gummy MUA4 Equipemnt Failure")
TagAlarm("Gummy", i+1, "AHU", "value", 2, "==", 1, "Gummy AHU Equipemnt Failure")

#EXT-AHU1A-1B
i = 51
TagAlarm("EXT1203/1204", i, "CO2-Life", "value", 1, ">", CO2L, "EXT1203/1204 CO2 life safety High Alarm")
TagAlarm("EXT1202-1", i, "CO2-Life", "value", 2, ">", CO2L, "EXT1202-1 CO2 life safety High Alarm")
TagAlarm("EXT1202-1", i, "O2-Life", "value", 3, "<", O2L, "EXT1202-1 O2 life safety Low Alarm")
TagAlarm("EXT1202-2", i, "CO2-Life", "value", 4, ">", CO2L, "EXT1202-2 CO2 life safety High Alarm")
TagAlarm("EXT1202-3", i, "CO2-Life", "value", 5, ">", CO2L, "EXT1202-3 CO2 life safety High Alarm")
TagAlarm("EXT1208", i, "CO2-Life", "value", 6, ">", CO2L, "EXT1208 CO2 life safety High Alarm")
TagAlarm("EXT1208", i, "O2-Life", "value", 7, "<", O2L, "EXT1208 O2 life safety Low Alarm")
TagAlarm("EXT0201-1", i, "CO2-Life", "value", 8, ">", CO2L, "EXT0201-1 CO2 life safety High Alarm")
TagAlarm("EXT0201-1", i, "O2-Life", "value", 9, "<", O2L, "EXT0201-1 O2 life safety Low Alarm")

TagAlarm("Extraction", i+1, "AHU1A", "value", 1, "==", 1, "Extraction AHU1A Equipemnt Failure")
TagAlarm("Extraction", i+1, "AHU1B", "value", 2, "==", 1, "Extraction AHU1B Equipemnt Failure")

i = 53
TagAlarm("Extraction", i, "MAU1", "value", 1, "==", 1, "Extraction MAU1 Equipemnt Failure")
TagAlarm("Extraction", i, "FFU1", "value", 2, "==", 1, "Extraction FFU1 Equipemnt Failure")

i = 54
TagAlarm("DR1212", i, "AHU8", "value", 1, "==", 1, "DR1212 AHU8 Equipemnt Failure")
TagAlarm("DR1212", i, "AHU9", "value", 2, "==", 1, "DR1212 AHU9 Equipemnt Failure")
TagAlarm("DR1212", i, "FFU3", "value", 3, "==", 1, "DR1212 FFU3 Equipemnt Failure")

i = 55
TagAlarm("Plant Waste", i, "Temp", "delta", 2, ">", DT_HI, "Plant Waste Temperature	deviation High Alarm")
TagAlarm("Plant Waste", i, "Temp", "delta", 2, "<", DT_LO, "Plant Waste Temperature deviation Low Alarm")
TagAlarm("Plant Waste", i, "Temp", "value", 2, ">", OOST_HI, "Plant Waste Temperature Out of Spec High Alarm")
TagAlarm("Plant Waste", i, "Temp", "value", 2, "<", OOST_LO, "Plant Waste Temperature Out of Spec Low Alarm")

TagAlarm("Plant Waste", i, "RH", "value", 4, ">", OOSH_HI, "Plant Waste Relative Humidity Out of Spec High Alarm")
TagAlarm("Plant Waste", i, "RH", "value", 4, "<", OOSH_LO,"Plant Waste Relative Humidity Out of Spec Low Alarm")

TagAlarm("Plant Waste", i, "DP", "delta", 5, ">", DDP_HI, "Plant Waste Difference Pressure deviation High Alarm", sp=0)
TagAlarm("Plant Waste", i, "DP", "delta", 5, "<", DDP_LO, "Plant Waste Difference Pressure deviation Low Alarm", sp=0)
TagAlarm("Plant Waste", i, "DP", "value", 5, ">", OOSDP_HI, "Plant Waste Difference Pressure Out of Spec High Alarm")
TagAlarm("Plant Waste", i, "DP", "value", 5, "<", OOSDP_LO, "Plant Waste Difference Pressure Out of Spec Low Alarm")

TagAlarm("Plant Waste", i+1, "RTU2", "value", 1, "==", 1, "Plant Waste RTU2 Equipemnt Failure")

i = 57
TagAlarm("Post Wash", i, "Temp", "delta", 2, ">", DT_HI, "Post Wash Temperature	deviation High Alarm")
TagAlarm("Post Wash", i, "Temp", "delta", 2, "<", DT_LO, "Post Wash Temperature deviation Low Alarm")
TagAlarm("Post Wash", i, "Temp", "value", 2, ">", OOST_HI, "Post Wash Temperature Out of Spec High Alarm")
TagAlarm("Post Wash", i, "Temp", "value", 2, "<", OOST_LO, "Post Wash Temperature Out of Spec Low Alarm")

TagAlarm("Post Wash", i, "RH", "delta", 6, ">", DH_HI, "Post Wash Relative Humidity deviation High Alarm")
TagAlarm("Post Wash", i, "RH", "delta", 6, "<", DH_LO, "Post Wash Relative Humidity deviation Low Alarm")
TagAlarm("Post Wash", i, "RH", "value", 6, ">", OOSH_HI, "Post Wash Relative Humidity Out of Spec High Alarm")
TagAlarm("Post Wash", i, "RH", "value", 6, "<", OOSH_LO,"Post Wash Relative Humidity Out of Spec Low Alarm")

TagAlarm("Wash Room", i, "Temp", "delta", 4, ">", DT_HI, "Wash Room Temperature	deviation High Alarm")
TagAlarm("Wash Room", i, "Temp", "delta", 4, "<", DT_LO, "Wash Room Temperature deviation Low Alarm")
TagAlarm("Wash Room", i, "Temp", "value", 4, ">", OOST_HI, "Wash Room Temperature Out of Spec High Alarm")
TagAlarm("Wash Room", i, "Temp", "value", 4, "<", OOST_LO, "Wash Room Temperature Out of Spec Low Alarm")

TagAlarm("Wash Room", i, "RH", "delta", 8, ">", DH_HI, "Wash Room Relative Humidity deviation High Alarm")
TagAlarm("Wash Room", i, "RH", "delta", 8, "<", DH_LO, "Wash Room Relative Humidity deviation Low Alarm")
TagAlarm("Wash Room", i, "RH", "value", 8, ">", OOSH_HI, "Wash Room Relative Humidity Out of Spec High Alarm")
TagAlarm("Wash Room", i, "RH", "value", 8, "<", OOSH_LO,"Wash Room Relative Humidity Out of Spec Low Alarm")

for index, name in enumerate(["CS vs W Corr", "CS vs PW", "PW vs WR", "CS vs PWAL", "PW vs PWAL", "WR vs PWAL", "WR vs W Corr"]):
	TagAlarm(name, i, "DP", "delta", index+9, ">", DDP_HI, "{} Difference Pressure deviation High Alarm".format(name), sp=0)
	TagAlarm(name, i, "DP", "delta", index+9, "<", DDP_LO, "{} Difference Pressure deviation Low Alarm".format(name), sp=0)
	TagAlarm(name, i, "DP", "value", index+9, ">", OOSDP_HI, "{} Difference Pressure Out of Spec High Alarm".format(name))
	TagAlarm(name, i, "DP", "value", index+9, "<", OOSDP_LO, "{} Difference Pressure Out of Spec Low Alarm".format(name))

TagAlarm("Clean Storage/Post Wash", i+1, "AHU11", "value", 1, "==", 1, "Clean Storage/Post Wash AHU11 Equipemnt Failure")
TagAlarm("Clean Storage/Post Wash", i+1, "FFU9", "value", 2, "==", 1, "Clean Storage/Post Wash FFT9 Equipemnt Failure")
TagAlarm("Wash Room", i+1, "AHU29", "value", 3, "==", 1, "Wah Room AHU29 Equipemnt Failure")


i = 59
TagAlarm("Drying Room 1603", i, "AHU13", "value", 1, "==", 1, "Drying Room 1603 AHU13 Equipemnt Failure")
TagAlarm("Drying Room 1603", i, "AHU14", "value", 2, "==", 1, "Drying Room 1603 AHU14 Equipemnt Failure")
TagAlarm("Trimming Room 1605", i, "AHU15", "value", 3, "==", 1, "Trimming Room 1605 AHU15 Equipemnt Failure")
TagAlarm("Drying Room 1603", i, "FFU10", "value", 4, "==", 1, "Drying Room 1603 FFU10 Equipemnt Failure")

i = 60
TagAlarm("Fin Goods", i, "Temp", "delta", 2, ">", DT_HI, "Fin Goods Temperature	deviation High Alarm")
TagAlarm("Fin Goods", i, "Temp", "delta", 2, "<", DT_LO, "Fin Goods Temperature deviation Low Alarm")
TagAlarm("Fin Goods", i, "Temp", "value", 2, ">", OOST_HI, "Fin Goods Temperature Out of Spec High Alarm")
TagAlarm("Fin Goods", i, "Temp", "value", 2, "<", OOST_LO, "Fin Goods Temperature Out of Spec Low Alarm")

TagAlarm("Fin Goods", i, "RH", "delta", 4, ">", DH_HI, "Fin Goods Relative Humidity deviation High Alarm")
TagAlarm("Fin Goods", i, "RH", "delta", 4, "<", DH_LO, "Fin Goods Relative Humidity deviation Low Alarm")
TagAlarm("Fin Goods", i, "RH", "value", 4, ">", OOSH_HI, "Fin Goods Relative Humidity Out of Spec High Alarm")
TagAlarm("Fin Goods", i, "RH", "value", 4, "<", OOSH_LO,"Fin Goods Relative Humidity Out of Spec Low Alarm")

for index, name in enumerate(["FG vs AL1220", "PR vs AL1220", "SR vs AL1220", "AL1220 vs SRAL", "SR vs SRAL"]):
	TagAlarm(name, i, "DP", "delta", index+5, ">", DDP_HI, "{} Difference Pressure deviation High Alarm".format(name), sp=0)
	TagAlarm(name, i, "DP", "delta", index+5, "<", DDP_LO, "{} Difference Pressure deviation Low Alarm".format(name), sp=0)
	TagAlarm(name, i, "DP", "value", index+5, ">", OOSDP_HI, "{} Difference Pressure Out of Spec High Alarm".format(name))
	TagAlarm(name, i, "DP", "value", index+5, "<", OOSDP_LO, "{} Difference Pressure Out of Spec Low Alarm".format(name))

TagAlarm("Hallway East and West", i+1, "AHU12", "value", 1, "==", 1, "Hallway East and West AHU12 Equipemnt Failure")
TagAlarm("Hallway East and West", i+1, "FFU4", "value", 2, "==", 1, "Hallway East and West FFU4 Equipemnt Failure")
TagAlarm("Fin Goods/Pack./Sec.", i+1, "AHU17", "value", 3, "==", 1, "Fin Goods/Pack./Sec. AHU17 Equipemnt Failure")

i = 62
TagAlarm("Shipping 1221", i, "Temp", "delta", 2, ">", DT_HI, "Shipping 1221 Temperature	deviation High Alarm")
TagAlarm("Shipping 1221", i, "Temp", "delta", 2, "<", DT_LO, "Shipping 1221 Temperature deviation Low Alarm")
TagAlarm("Shipping 1221", i, "Temp", "value", 2, ">", OOST_HI, "Shipping 1221 Temperature Out of Spec High Alarm")
TagAlarm("Shipping 1221", i, "Temp", "value", 2, "<", OOST_LO, "Shipping 1221 Temperature Out of Spec Low Alarm")

TagAlarm("Shipping 1221", i, "RH", "value", 4, ">", OOSH_HI, "Shipping 1221 Relative Humidity Out of Spec High Alarm")
TagAlarm("Shipping 1221", i, "RH", "value", 4, "<", OOSH_LO,"Shipping 1221 Relative Humidity Out of Spec Low Alarm")

TagAlarm("Shipping 1221", i, "DP", "delta", 5, ">", DDP_HI, "Shipping 1221 Difference Pressure deviation High Alarm", sp=0)
TagAlarm("Shipping 1221", i, "DP", "delta", 5, "<", DDP_LO, "Shipping 1221 Difference Pressure deviation Low Alarm", sp=0)
TagAlarm("Shipping 1221", i, "DP", "value", 5, ">", OOSDP_HI, "Shipping 1221 Difference Pressure Out of Spec High Alarm")
TagAlarm("Shipping 1221", i, "DP", "value", 5, "<", OOSDP_LO, "Shipping 1221 Difference Pressure Out of Spec Low Alarm")

TagAlarm("Fresh Air", i+1, "AHU16", "value", 1, "==", 1, "Fresh Air AHU16 Equipemnt Failure")
TagAlarm("Shipping 1221", i+1, "Ductless Split", "value", 2, "==", 1, "Shipping 1221 Ductless Split Equipemnt Failure")

i = 64
TagAlarm("Roadhouse", i, "AHU9", "value", 1, "==", 1, "Roadhouse AHU9 Equipemnt Failure")
TagAlarm("Roadhouse", i, "AHU10", "value", 2, "==", 1, "Roadhouse AHU10 Equipemnt Failure")
TagAlarm("Roadhouse", i, "FFU8", "value", 3, "==", 1, "Roadhouse FFU8 Equipemnt Failure")

i = 65
TagAlarm("Roadhouse C1D1", i, "SF1", "value", 1, "==", 1, "Roadhouse C1D1 SF1 Equipemnt Failure")
TagAlarm("Roadhouse C1D1", i, "SF2", "value", 2, "==", 1, "Roadhouse C1D1 SF2 Equipemnt Failure")
TagAlarm("Roadhouse C1D1", i, "EF1", "value", 3, "==", 1, "Roadhouse C1D1 EF1 Equipemnt Failure")
TagAlarm("Roadhouse C1D1", i, "EF2", "value", 4, "==", 1, "Roadhouse C1D1 EF2 Equipemnt Failure")
TagAlarm("Roadhouse C1D1", i, "EF3", "value", 5, "==", 1, "Roadhouse C1D1 EF3 Equipemnt Failure")

# Chiller Plant
i = 66
TagAlarm("Chiller Plant Zone 1", i, "Temp", "delta", 1, ">", DT_HI, "Chiller Plant Zone 1 Supply Temperature deviation High Alarm", sp=3.3)
TagAlarm("Chiller Plant Zone 1", i, "Temp", "delta", 1, "<", DT_LO, "Chiller Plant Zone 1 Supply Temperature deviation Low Alarm", sp=3.3)
TagAlarm("Chiller Plant Zone 2", i, "Temp", "delta", 2, ">", DT_HI, "Chiller Plant Zone 2 Supply Temperature deviation High Alarm", sp=3.3)
TagAlarm("Chiller Plant Zone 2", i, "Temp", "delta", 2, "<", DT_LO, "Chiller Plant Zone 2 Supply Temperature deviation Low Alarm", sp=3.3)
TagAlarm("Chiller Plant Zone 3", i, "Temp", "delta", 3, ">", DT_HI, "Chiller Plant Zone 3 Supply Temperature deviation High Alarm", sp=3.3)
TagAlarm("Chiller Plant Zone 3", i, "Temp", "delta", 3, "<", DT_LO, "Chiller Plant Zone 3 Supply Temperature deviation Low Alarm", sp=3.3)

a = TagAlarm("Chiller Plant", i, "Glycol Pressure", "value", 4, ">", DT_HI, "Chiller Plant Glycol Pressure deviation High Alarm").return_tag("Chiller Plant", "Glycol Pressure", "value")
a.tag_scale_10()
a.set_tag_unit("psi")
TagAlarm("Chiller Plant", i, "Glycol Pressure", "value", 4, "<", DT_LO, "Chiller Plant Glycol Pressure deviation Low Alarm")

a = TagAlarm("Chiller Plant Zone 1", i, "DP", "value", 5, ">", OOSDP_HI, "Chiller Plant Zone 1 Difference Pressure deviation High Alarm").return_tag("Chiller Plant Zone 1", "DP", "value")
a.set_tag_unit("psi")
TagAlarm("Chiller Plant Zone 1", i, "DP", "value", 5, "<", OOSDP_LO, "Chiller Plant Zone 1 Difference Pressure deviation Low Alarm")
a = TagAlarm("Chiller Plant Zone 2", i, "DP", "value", 6, ">", OOSDP_HI, "Chiller Plant Zone 2 Difference Pressure deviation High Alarm").return_tag("Chiller Plant Zone 2", "DP", "value")
a.set_tag_unit("psi")
TagAlarm("Chiller Plant Zone 2", i, "DP", "value", 6, "<", OOSDP_LO, "Chiller Plant Zone 2 Difference Pressure deviation Low Alarm")
a = TagAlarm("Chiller Plant Zone 3", i, "DP", "value", 7, ">", OOSDP_HI, "Chiller Plant Zone 3 Difference Pressure deviation High Alarm").return_tag("Chiller Plant Zone 3", "DP", "value")
a.set_tag_unit("psi")
TagAlarm("Chiller Plant Zone 3", i, "DP", "value", 7, "<", OOSDP_LO, "Chiller Plant Zone 3 Difference Pressure deviation Low Alarm")

TagAlarm("Cooling Tower 1", i, "Temp", "delta", 9, ">", DT_HI, "Cooling Tower 1 Supply Temperature deviation High Alarm")
TagAlarm("Cooling Tower 1", i, "Temp", "delta", 9, "<", DT_LO, "Cooling Tower 1 Supply Temperature deviation Low Alarm")
TagAlarm("Cooling Tower 2-3", i, "Temp", "delta", 11, ">", DT_HI, "Cooling Tower 2-3 Supply Temperature deviation High Alarm")
TagAlarm("Cooling Tower 2-3", i, "Temp", "delta", 11, "<", DT_LO, "Cooling Tower 2-3 Supply Temperature deviation Low Alarm")

i = 67
TagAlarm("Chiller", i, "1", "value", 1, "==", 1, "Chiller 1 Equipemnt Failure")
TagAlarm("Chiller", i, "2", "value", 2, "==", 1, "Chiller 2 Equipemnt Failure")
TagAlarm("Primary Pump", i, "CPP-1", "value", 3, "==", 1, "Primary Pump CPP-1 Equipemnt Failure")
TagAlarm("Primary Pump", i, "CPP-2", "value", 4, "==", 1, "Primary Pump CPP-2 Equipemnt Failure")
TagAlarm("Primary Pump", i, "CPP-3", "value", 5, "==", 1, "Primary Pump CPP-3 Equipemnt Failure")
TagAlarm("Secondary Pump", i, "CSP-1", "value", 6, "==", 1, "Secondary Pump CSP-1 Equipemnt Failure")
TagAlarm("Secondary Pump", i, "CSP-2", "value", 7, "==", 1, "Secondary Pump CSP-2 Equipemnt Failure")
TagAlarm("Secondary Pump", i, "CSP-3", "value", 8, "==", 1, "Secondary Pump CSP-3 Equipemnt Failure")
TagAlarm("Secondary Pump", i, "CSP-4", "value", 9, "==", 1, "Secondary Pump CSP-4 Equipemnt Failure")
TagAlarm("Secondary Pump", i, "CSP-5", "value", 10, "==", 1, "Secondary Pump CSP-5 Equipemnt Failure")
TagAlarm("Condenser Pump", i, "CP-1", "value", 11, "==", 1, "Condenser Pump CP-1 Equipemnt Failure")
TagAlarm("Condenser Pump", i, "CP-2", "value", 12, "==", 1, "Condenser Pump CP-2 Equipemnt Failure")
TagAlarm("Cooling Tower", i, "1", "value", 13, "==", 1, "Cooling Tower 1 Equipemnt Failure")
TagAlarm("Irrigation", i, "RTU4", "value", 14, "==", 1, "Irrigation RTU4 Equipemnt Failure")
TagAlarm("Irrigation", i, "RTU5", "value", 15, "==", 1, "Irrigation RTU5 Equipemnt Failure")

TagAlarm("Chiller Room", i, "Leak Detector 1", "value", 16, "==", 1, "Chiller Room Leak Detector 1 Equipemnt Failure")
TagAlarm("Chiller Room", i, "Leak Detector 2", "value", 17, "==", 1, "Chiller Room Leak Detector 2 Equipemnt Failure")
TagAlarm("Chiller Room", i, "Leak Detector 3", "value", 18, "==", 1, "Chiller Room Leak Detector 3 Equipemnt Failure")
TagAlarm("Chiller Room", i, "Leak Detector 4", "value", 19, "==", 1, "Chiller Room Leak Detector 4 Equipemnt Failure")
TagAlarm("Chiller Room Refrig", i, "Leak Detector", "value", 20, "==", 1, "Chiller Room Refrig Leak Detector Alarm")
# TagAlarm("Chiller Room Refrig", 66, "Leak Detector 1", "value", 12, ">", 5, "Chiller Room Refrig Leak Detector 1 Alarm")
# TagAlarm("Chiller Room Refrig", 66, "Leak Detector 2", "value", 13, ">", 5, "Chiller Room Refrig Leak Detector 2 Alarm")
# TagAlarm("Chiller Room Refrig", 66, "Leak Detector 3", "value", 14, ">", 5, "Chiller Room Refrig Leak Detector 3 Alarm")
# TagAlarm("Chiller Room Refrig", 66, "Leak Detector 4", "value", 15, ">", 5, "Chiller Room Refrig Leak Detector 4 Alarm")

TagAlarm("Chiller Room Refrig", i, "Leak Detector 2", "value", 21, "==", 1, "Chiller Room Refrig Leak Detector 2 Equipemnt Failure")

TagAlarm("Primary Pump", i, "CPP-4", "value", 22, "==", 1, "Primary Pump CPP-4 Equipemnt Failure")
TagAlarm("Primary Pump", i, "CPP-5", "value", 23, "==", 1, "Primary Pump CPP-5 Equipemnt Failure")
TagAlarm("Chiller", i, "3", "value", 24, "==", 1, "Chiller 3 Equipemnt Failure")
TagAlarm("Chiller", i, "4", "value", 25, "==", 1, "Chiller 4 Equipemnt Failure")


# Irrg
i = 68
TagAlarm("Recipe1", i, "Pump", "value", 69, "==", 1, "Recipe1 Pump Equipemnt Failure")
TagAlarm("Recipe2", i, "Pump", "value", 70, "==", 1, "Recipe2 Pump Equipemnt Failure")
TagAlarm("Recipe3", i, "Pump", "value", 71, "==", 1, "Recipe3 Pump Equipemnt Failure")
TagAlarm("Recipe4", i, "Pump", "value", 72, "==", 1, "Recipe4 Pump Equipemnt Failure")

TagAlarm("Dosing Unit", i, "1", "value", 5, "==", 1, "Dosing Unit 1 Equipemnt Failure")
TagAlarm("Dosing Unit", i, "2", "value", 15, "==", 1, "Dosing Unit 2 Equipemnt Failure")

TagAlarm("Fertilizer Line", i, "1", "value", 26, "==", 1, "Ferfilizer Line 1 Equipemnt Failure")
TagAlarm("Fertilizer Line", i, "2", "value", 36, "==", 1, "Ferfilizer Line 2 Equipemnt Failure")
TagAlarm("Fertilizer Line", i, "3", "value", 46, "==", 1, "Ferfilizer Line 3 Equipemnt Failure")
TagAlarm("Fertilizer Line", i, "4", "value", 56, "==", 1, "Ferfilizer Line 4 Equipemnt Failure")

TagAlarm("RO", i, "UV", "value", 63, "==", 1, "RO-UV Equipemnt Failure")
TagAlarm("RO-UV", i, "Filling Pump 1A", "value", 65, "==", 1, "RO-UV Filling Pump 1A Equipemnt Failure")
TagAlarm("RO-UV", i, "Filling Pump 1B", "value", 66, "==", 1, "RO-UV Filling Pump 1B Equipemnt Failure")
TagAlarm("RO-UV", i, "Filling Pump 2A", "value", 67, "==", 1, "RO-UV Filling Pump 2A Equipemnt Failure")
TagAlarm("RO-UV", i, "Filling Pump 2B", "value", 68, "==", 1, "RO-UV Filling Pump 2B Equipemnt Failure")



def make_excel(results, name):
	keys = results[0].keys()
	a_file = open("{}.csv".format(name), "w",newline='')
	dict_writer = csv.DictWriter(a_file, keys)
	dict_writer.writeheader()
	dict_writer.writerows(results)
	a_file.close()


make_excel(Tag.taglist, "tag_db")
make_excel(Alarm.alarmlist, "alarm_db")

zipfile.ZipFile('tag_db.zip', mode='w').write("tag_db.csv")
zipfile.ZipFile('alarm_db.zip', mode='w').write("alarm_db.csv")