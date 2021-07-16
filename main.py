# Importing all needed libraries
import os
import sys
import json
# General Class
class musick_sourter:
	audio_dir_default_name = "\\Audio_files"
	audio_file_extention_type = ".txt"
	Json_Output_File = "./data.json"
	get_current_pah = os.getcwd()
	Json_file_append_dict = {}


	def _help(self) :
		print("Please Select correct answer the music is Noise or Clear ")
		print("	You must be can us for")
		print("	Noise:")
		print("		n/N/Noise/NOISE/noise")
		print("	Clear:")
		print("		c/C/Clear/CLEAR/clear")
		print("Or you can exit from application with 'Q' button")


	def append_to_dict(self,option = "Noise",dict_key = "",audio_file_name =""):
		self.Json_file_append_dict[dict_key].append({
			"File Name": audio_file_name,
			"Selected parameter": option,
		})



	def create_write_json_file (self):
		jsonFile = open(self.Json_Output_File, "w")
		jsonFile.write(json.dumps(self.Json_file_append_dict, indent=4))

		jsonFile.close()

	def __init__(self,audio_dir_default_name = "\\Audio_files",audio_file_extention_type = ".txt" ,
				 get_current_pah = os.getcwd() , Json_Output_File = "./data.json" ):

		# Start the App with checking existence of set directory
		if os.path.isdir(get_current_pah+audio_dir_default_name):
			audio_file_full_path = self.get_current_pah+self.audio_dir_default_name
			files = os.listdir(audio_file_full_path)
			# Make new Key for Dictionary
			dict_key = str("Directory : " + audio_file_full_path)
			self.Json_file_append_dict[dict_key] = []

			# Start general loop
			for audio_file_name in files:
				# Set boolean for check correction of set argument
				noise_clear_checking_loop_bool = True

				while noise_clear_checking_loop_bool:
					# Check Audio file extention I this moment it text file with txt extension
					if audio_file_name.lower().endswith(audio_file_extention_type):
						print(audio_file_name)
						# It can be only too options "n/N/noise/Noise" or "c/C/clear/Clear"
						answer = input()
						# Case for Noises
						if answer.lower() == 'n' or answer.lower() == "noise":
							noise_clear_checking_loop_bool = False
							self.append_to_dict ("Noise",dict_key,audio_file_name)
						elif answer.lower() == 'c' or answer.lower() == "clear":
							noise_clear_checking_loop_bool = False
							self.append_to_dict ("Clear",dict_key,audio_file_name)
						# Case for Quit from App
						elif answer.lower() == 'q':
							print ("You are exit from App !!!")
							sys.exit()
						# Help
						else:
							self._help()
		else:
			print ("Directory cannot by find")
		self.create_write_json_file ()




def _help ():
	print ("By Default:")
	print ("	Input File extention : .TXT")
	print ("	Input File location  : ./Audio_Files")
	print ("	Output File name     : ./data.json")
	print ("")

_help()
musick_obj = musick_sourter()


