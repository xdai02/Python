def format_date(year=1970, month=1, day=1):
	return "%04d/%02d/%02d" % (year, month, day)

def main():
    print(format_date(2022, 12, 16))
    print(format_date(2022, 12))
    print(format_date(2022))
    print(format_date())

if __name__ == "__main__":
	main()