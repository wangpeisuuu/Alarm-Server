from utils import *

# delta type use setpoint raddr
# room, mid, alarm_type, tag_type, raddr, logic, target, msg, sp=None

i = 1
TagAlarm("GR{}".format(i), i, "Temp", "delta", 1, ">", 5, "Grow Room {} Temperature	deviation High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "Temp", "delta", 1, "<", -5, "Grow Room {} Temperature deviation Low Alarm".format(i))
TagAlarm("GR{}".format(i), i, "Temp", "value", 2, ">", 30, "Grow Room {} Temperature Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "Temp", "value", 2, "<", 20, "Grow Room {} Temperature Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i, "RH", "delta", 11, ">", 10, "Grow Room {} Relative Humidity deviation High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "RH", "delta", 11, "<", -10, "Grow Room {} Relative Humidity deviation Low Alarm".format(i))
TagAlarm("GR{}".format(i), i, "RH", "value", 12, ">", 70, "Grow Room {} Relative Humidity Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "RH", "value", 12, "<", 35,"Grow Room {} Relative Humidity Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i, "CO2", "delta", 21, ">", 300, "Grow Room {} CO2 deviation High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "CO2", "delta", 21, "<", -300, "Grow Room {} CO2 deviation Low Alarm".format(i))
TagAlarm("GR{}".format(i), i, "CO2", "value", 22, ">", 3000, "Grow Room {} CO2 Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "CO2", "value", 22, "<", 200, "Grow Room {} CO2 Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i, "DP", "delta", 37, ">", 0.3, "Grow Room {} Difference Pressure deviation High Alarm".format(i), sp=0)
TagAlarm("GR{}".format(i), i, "DP", "delta", 37, "<", -0.3, "Grow Room {} Difference Pressure deviation Low Alarm".format(i), sp=0)
TagAlarm("GR{}".format(i), i, "DP", "value", 37, ">", 0.3, "Grow Room {} Difference Pressure Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "DP", "value", 37, "<", -0.3, "Grow Room {} Difference Pressure Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i*2, "Max-Valve", "value", 33, "==", 1, "Grow Room {} Max number of Valves in failure Alarm".format(i)) # digital
TagAlarm("GR{}".format(i), i, "O2-Life", "value", 38, "<", 9, "Grow Room {} O2 life safety Low Alarm".format(i))
TagAlarm("GR{}".format(i), i, "CO2-Life", "value", 39, ">", 3500, "Grow Room {} CO2 life safety High Alarm".format(i))

TagAlarm("GR{}".format(i), i*2, "AHU 1", "value", 44, "==", 1, "Grow Room {} AHU 1 Equipemnt Failure, AHU 1".format(i))
TagAlarm("GR{}".format(i), i*2, "AHU 2", "value", 45, "==", 1, "Grow Room {} AHU 2 Equipemnt Failure, AHU 2".format(i))
TagAlarm("GR{}".format(i), i*2, "AHU 3", "value", 46, "==", 1, "Grow Room {} AHU 3 Equipemnt Failure, AHU 3".format(i))
TagAlarm("GR{}".format(i), i*2, "AHU 4", "value", 47, "==", 1, "Grow Room {} AHU 4 Equipemnt Failure, AHU 4".format(i))
TagAlarm("GR{}".format(i), i*2, "FFU 1", "value", 48, "==", 1, "Grow Room {} FFU 1 Equipemnt Failure, FFU 1".format(i))
TagAlarm("GR{}".format(i), i*2, "FFU 2", "value", 49, "==", 1, "Grow Room {} FFU 2 Equipemnt Failure, FFU 2".format(i))


i = 2
TagAlarm("GR{}".format(i), i, "Temp", "delta", 1, ">", 5, "Grow Room {} Temperature	deviation High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "Temp", "delta", 1, "<", -5, "Grow Room {} Temperature deviation Low Alarm".format(i))
TagAlarm("GR{}".format(i), i, "Temp", "value", 2, ">", 30, "Grow Room {} Temperature Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "Temp", "value", 2, "<", 20, "Grow Room {} Temperature Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i, "RH", "delta", 11, ">", 10, "Grow Room {} Relative Humidity deviation High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "RH", "delta", 11, "<", -10, "Grow Room {} Relative Humidity deviation Low Alarm".format(i))
TagAlarm("GR{}".format(i), i, "RH", "value", 12, ">", 70, "Grow Room {} Relative Humidity Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "RH", "value", 12, "<", 35,"Grow Room {} Relative Humidity Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i, "CO2", "delta", 21, ">", 300, "Grow Room {} CO2 deviation High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "CO2", "delta", 21, "<", -300, "Grow Room {} CO2 deviation Low Alarm".format(i))
TagAlarm("GR{}".format(i), i, "CO2", "value", 22, ">", 3000, "Grow Room {} CO2 Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "CO2", "value", 22, "<", 200, "Grow Room {} CO2 Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i, "DP", "delta", 37, ">", 0.3, "Grow Room {} Difference Pressure deviation High Alarm".format(i), sp=0)
TagAlarm("GR{}".format(i), i, "DP", "delta", 37, "<", -0.3, "Grow Room {} Difference Pressure deviation Low Alarm".format(i), sp=0)
TagAlarm("GR{}".format(i), i, "DP", "value", 37, ">", 0.3, "Grow Room {} Difference Pressure Out of Spec High Alarm".format(i))
TagAlarm("GR{}".format(i), i, "DP", "value", 37, "<", -0.3, "Grow Room {} Difference Pressure Out of Spec Low Alarm".format(i))

TagAlarm("GR{}".format(i), i*2, "Max-Valve", "value", 33, "==", 1, "Grow Room {} Max number of Valves in failure Alarm".format(i)) # digital
TagAlarm("GR{}".format(i), i, "O2-Life", "value", 38, "<", 9, "Grow Room {} O2 life safety Low Alarm".format(i))
TagAlarm("GR{}".format(i), i, "CO2-Life", "value", 39, ">", 3500, "Grow Room {} CO2 life safety High Alarm".format(i))

TagAlarm("GR{}".format(i), i*2, "AHU 30", "value", 44, "==", 1, "Grow Room {} AHU 30 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "AHU 31", "value", 45, "==", 1, "Grow Room {} AHU 31 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "AHU 32", "value", 46, "==", 1, "Grow Room {} AHU 32 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "AHU 33", "value", 47, "==", 1, "Grow Room {} AHU 33 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "FFU 5", "value", 48, "==", 1, "Grow Room {} FFU 5 Equipemnt Failure".format(i))
TagAlarm("GR{}".format(i), i*2, "FFU 6", "value", 49, "==", 1, "Grow Room {} FFU 6 Equipemnt Failure".format(i))

import zipfile

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