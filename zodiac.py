

class UserZodiac:

	def __init__(self, name, year, month, day):
		self.name = name
		self.year = year
		self.month = month
		self.day = day
		self.sign = None


	def checkForSign(self):
		if self.month.lower() == "march":
			
			if self.day < 21:
				self.sign = "Pisces"

			else:
				self.sign = "Aries"



		elif self.month.lower() == "april":

			if self.day < 21:
				self.sign = "Aries"

			else:
				self.sign = "Taurus"



		elif self.month.lower() == "may":

			if self.day < 22:
				self.sign = "Taurus"

			else: 
				self.sign = "Twins"



		elif self.month.lower() == "june":

			if self.day < 22:
				self.sign = "Twins"

			else:
				self.sign = "Cancer"



		elif self.month.lower() == "july":

			if self.day < 24:
				self.sign = "Cancer"

			else:
				self.sign = "Leo"



		elif self.month.lower() == "august":

			if self.day < 24:
				self.sign = "Leo"

			else:
				self.sign = "Virgo"



		elif self.month.lower() == "september":

			if self.day < 24:
				self.sign = "Virgo"

			else:
				self.sign = "Libra"


		elif self.month.lower() == "october":
			
			if self.day < 24:
				self.sign = "Libra"

			else:
				self.sign = "Scorpio"



		elif self.month.lower() == "november":

			if self.day < 23:
				self.sign = "Scorpio"

			else:
				self.sign = "Sagittarius"


		elif self.month.lower() == "december":

			if self.day < 22:
				self.sign = "Sagittarius"

			else:
				self.sign = "Capricorn"


		elif self.month.lower() == "january":

			if self.day < 21:
				self.sign = "Capricorn"

			else:
				self.sign = "Aquarius"


		elif self.month.lower() == "february":

			if self.day < 20:
				self.sign = "Aquarius"

			else:
				self.sign = "Pisces " 

		return f"{user_name} თქვენი ზოდიაქოს ნიშანია - {self.sign} "



user_name = input("შეიტანეთ თქვენი სახელი: ")

user_birth_year = int(input("შეიტანეთ დაბადების წელი(მაგალითად 2003): "))

user_birth_month = input("შეიტანეთ დაბადების თვე(e.g: March): ")

user_birth_day = int(input("შეიტანეთ დაბადების დღე(მაგ: 19) : "))

try:
	user_birth_year = int(user_birth_year)
except:
	print("გთხოვთ შეიტანოთ მხოლოდ რიცხვები!!! ")
	


user = UserZodiac(user_name, user_birth_year, user_birth_month, user_birth_day)

print(user.checkForSign())