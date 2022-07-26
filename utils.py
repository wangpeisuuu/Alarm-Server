from dicts import *
import csv


d = {}
class Tag():
	# tag used for tag alarm
	tag_id = 1
	taglist = []
	def __init__(self, room, alarm_type, tag_type, mid, raddr, sp=None):
		self.tag = dict(tags)
		self.tag["tag_id"] = Tag.tag_id
		self.room = room
		self.alarm_type = alarm_type
		self.mid = mid
		self.raddr = raddr
		self.sp = sp
		Tag.tag_id = Tag.tag_id+1
		if tag_type == "value":
			self.create_value_tag()
		if tag_type == "delta":
			self.create_dev_tag()
		if tag_type == "sp":
			self.create_sp_tag()

	def tag_name_value(self):
		self.tag["tag_name"] = "{}_{}_value".format(self.room, self.alarm_type)

	def tag_name_setpoint(self):
		self.tag["tag_name"] = "{}_{}_sp".format(self.room, self.alarm_type)

	def tag_name_delta(self):
		self.tag["tag_name"] = "{}_{}_delta".format(self.room, self.alarm_type)

	def _tag_scale_1(self):
		self.tag["tag_scale"] = "[{\"tag\":0,\"source\":0},{\"tag\":1,\"source\":1}]"

	def _tag_scale_10(self):
		self.tag["tag_scale"] = "[{\"tag\":0,\"source\":0},{\"tag\":1,\"source\":10}]"

	def _tag_scale_1000(self):
		self.tag["tag_scale"] = "[{\"tag\":0,\"source\":0},{\"tag\":1,\"source\":1000}]"

	def tag_unit(self):
		unit = ""
		if self.alarm_type == "Temp":
			unit = " Celcius"
			self._tag_scale_10()
		elif self.alarm_type == "RH" or self.alarm_type == "O2-Life" :
			unit = "%"
			self._tag_scale_10()
		elif "CO2" in self.alarm_type :
			unit = "ppm"
			self._tag_scale_1()
		elif self.alarm_type == "DP":
			unit = "inH2O"
			self._tag_scale_1000()
		self.tag["tag_unit"] = unit

	def tag_type(self, ttype):
		# modbus or tag
		self.tag["tag_type"] = ttype

	def tag_math_source(self, value, sp):
		self.tag["tag_source"] = "{\"source\":\"tag_math\",\"math\":\"%s-%s\"}" %(value, sp)

	def tag_value_source(self, raddr):
		# modbus id, register id
		self.tag["tag_source"] = "{\"source\":\"modbus\",\"modbus_id\":%d,\"register_type\":3,\"register_address\":%d,\"block_size\":1}" %(self.mid, raddr)

	def get_tag_name(self):
		return self.tag["tag_name"]

	def create_value_tag(self):
		self.tag_name_value()
		self.tag_unit()
		self.tag_type("modbus")
		self.tag_value_source(self.raddr)
		Tag.taglist.append(self.tag)

	def create_sp_tag(self):
		self.tag_name_setpoint()
		self.tag_unit()
		self.tag_type("modbus")
		self.tag_value_source(self.raddr)
		Tag.taglist.append(self.tag)

	def create_dev_tag(self):
				# gr1:
				# 	temp:
				# 		value -> 1 tag
				# 		delta -> 3 tags
				# 	rh:
				# 		value
				# 		delta
		if "value" not in d[self.room][self.alarm_type]:
			d[self.room][self.alarm_type]["value"] = Tag(self.room, self.alarm_type, "value", self.mid, self.raddr+1) # TODO

		value = d[self.room][self.alarm_type]["value"].get_tag_name()
		if self.sp == None:
			sp = Tag(self.room, self.alarm_type, "sp", self.mid, self.raddr).get_tag_name()
		else:
			sp = self.sp
		self.tag_name_delta()
		self.tag_unit()
		self.tag_type("tag")
		self.tag_math_source(value, sp)
		Tag.taglist.append(self.tag)

class Alarm:

	alarm_id=100
	alarmlist = []
	def __init__(self):
		pass

	def alarm_logic(self, logic):
		self.alarm["trigger_logic"] = logic

	def alarm_target(self, target):
		self.alarm["trigger_target"] = target

	def alarm_modbus_id(self, mid): 
		self.alarm["modbus_id"] = mid

	def alarm_tag_name(self, name):
		self.alarm["tag_name"] = name

	def alarm_msg(self, msg):
		self.alarm["message"] = msg

	def alarm_raddr(self, raddr):
		self.alarm["register_address"] = raddr

class TagAlarm(Alarm):

	def __init__(self, room, mid, alarm_type, tag_type, raddr, logic, target, msg, sp=None):

		if room not in d.keys():
			d[room] = {}

		if alarm_type not in d[room].keys():
			d[room][alarm_type] = {}

		if tag_type not in d[room][alarm_type].keys():
			d[room][alarm_type][tag_type] = {}
			d[room][alarm_type][tag_type] = Tag(room, alarm_type, tag_type, mid, raddr, sp)

		tag = d[room][alarm_type][tag_type].get_tag_name()
		self.alarm = dict(tag_alarm)
		self.alarm["alarm_id"] = Alarm.alarm_id
		Alarm.alarm_id = Alarm.alarm_id + 1

		self.alarm_logic(logic)
		self.alarm_target(target)
		self.alarm_tag_name(tag)
		self.alarm_msg(msg)

		Alarm.alarmlist.append(self.alarm)


class ModAlarm(Alarm):

	def __init__(self, room, mid, raddr, logic, target, msg):
		self.alarm = dict(mod_alarm)
		self.alarm["alarm_id"] = Alarm.alarm_id
		Alarm.alarm_id = Alarm.alarm_id + 1

		self.alarm_logic(logic)
		self.alarm_target(target)
		self.alarm_modbus_id(mid)
		self.alarm_raddr(raddr)
		self.alarm_msg(msg)

		Alarm.alarmlist.append(self.alarm)

