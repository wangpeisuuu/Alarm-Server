tags = {
			"tag_id": 0,
			"tag_name": "",
			"tag_unit": "None",
			"tag_scale": "[{\"tag\":0,\"source\":0},{\"tag\":1,\"source\":1}]",
			"tag_filter": 0,
			"tag_type": "modbus",
			"tag_source": "{\"source\":\"modbus\",\"modbus_id\":%d,\"register_type\":3,\"register_address\":%d,\"block_size\":1}" ,
			"tag_comment": "new tag",
			"tag_value": 0,
			"tag_cycles": 0,
			"tag_sum": 0,
			"tag_rate": 0,
			"tag_frequency": 0,
			"tag_data_type": "float",
			"tag_default_trigger_delta": 0.0,
			"tag_error": "",
			"tag_mqtt": "read-write"
      }

mod_alarm = {
			"alarm_id": 0,
			"source": "",
			"debounce": 15,
			"cgroups": "default",
			"delay": 15,
			"sendalarm": "Till Acknowledged",
			"message": "alarm message",
			"trigger_edge": "ON",
			"trigger_logic": ">",
			"trigger_target": 0,
			"notify_logic": "ALARM",
			"alarm_type": "modbus",
			"modbus_id": 1,
			"register_address": 1,
			"register_bit": "",
			"tag_name": "",
			"tag_param": ""
}

tag_alarm = {
			"alarm_id": 0,
			"source": "",
			"debounce": 15,
			"cgroups": "default",
			"delay": 240,
			"sendalarm": "Till Acknowledged",
			"message": "alarm message",
			"trigger_edge": "ON",
			"trigger_logic": ">",
			"trigger_target": 0,
			"notify_logic": "ALARM",
			"alarm_type": "tag",
			"modbus_id": "",
			"register_address": "",
			"register_bit": "",
			"tag_name": "room17_CO2_d",
			"tag_param": "0",
	        "target_type": "Fixed",
        	"enabled": "Yes"
}

rooms = {
	"GR":{
		"num" : 17,
		"type" : {	"Temperature":[30, 16, 3, -3], 
					"RH":[65, 45, 15, -15], 
					"CO2":[3000, 350, 200, -200], 
					"DP":[0, 0, 0 ,0]
					},
		"id" : None
	},
	"MR":{
		"num" : 1,
		"type" : {	"Temperature":[30, 16, 3, -3], 
					"RH":[65, 45, 15, -15], 
					"CO2":[3000, 350, 200, -200], 
					"DP":[0, 0, 0, 0]
					},
		"id" : 18
	},
	"CR":{
		"num" : 1,
		"type" : {	"Temperature":[30, 16, 3, -3], 
					"RH":[65, 45, 15, -15], 
					"CO2":[3000, 350, 200, -200], 
					"DP":[0, 0, 0, 0]
					},
		"id" : 19
	},
	"LV":{
		"num" : 1,
		"type" : {	"Temperature":[30, 16, 3, -3], 
					"RH":[65, 45, 15, -15], 
					"CO2":[3000, 350, 200, -200], 
					"DP":[0, 0, 0, 0]
					},
		"id" : 20
	},
	"DR":{
		"num" : 1,
		"type" : {	"Temperature":[30, 16, 3, -3], 
					"RH":[65, 45, 15, -15], 
					"DP":[0, 0, 0, 0]
					},
		"id" : 21
	},

	"TR":{
		"num" : 1,
		"type" : {	"Temperature":[30, 16, 3, -3], 
					"RH":[65, 45, 15, -15], 
					"DP":[0, 0, 0, 0]
					},
		"id" : 22
	},
	"Ship":{
		"num" : 1,
		"type" : {	"Temperature":[30, 16, 3, -3], 
					"RH":[65, 45, 15, -15], 
					"DP":[0, 0, 0, 0]
					},
		"id" : 23
	},
	"Finished":{
		"num" : 1,
		"type" : {	"Temperature":[30, 16, 3, -3], 
					"RH":[65, 45, 15, -15], 
					"DP":[0, 0, 0, 0]
					},
		"id" : 24
	},
	"Clean":{
		"num" : 1,
		"type" : {	"Temperature":[30, 16, 3, -3], 
					"RH":[65, 45, 15, -15], 
					"DP":[0, 0, 0, 0]
					},
		"id" : 25
	},
	"Washroom":{
		"num" : 1,
		"type" : {	"Temperature":[30, 16, 3, -3], 
					"RH":[65, 45, 15, -15], 
					"DP":[0, 0, 0, 0]
					},
		"id" : 26
	},
	"Waste":{
		"num" : 1,
		"type" : {	"Temperature":[30, 16, 3, -3], 
					"RH":[65, 45, 15, -15], 
					"DP":[0, 0, 0, 0]
					},
		"id" : 27
	},
	"Bakery1103":{
		"num" : 1,
		"type" : {	"Temperature":[30, 16, 3, -3], 
					"RH":[65, 45, 15, -15], 
					"DP":[0, 0, 0, 0]
					},
		"id" : 28
	},
	"Bakery1101":{
		"num" : 1,
		"type" : {	
					"DP":[0, 0, 0, 0]
					},
		"id" : 28
	},
	"Bakery1102":{
		"num" : 1,
		"type" : {	
					"DP":[0, 0, 0, 0]
					},
		"id" : 28
	},
	"Bakery1104":{
		"num" : 1,
		"type" : {	
					"DP":[0, 0, 0, 0]
					},
		"id" : 28
	},
	
}
