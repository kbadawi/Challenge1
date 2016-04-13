all: 
	@py Challenge1.py
	@open data.csv

clean:
	@rm data.csv

re: clean all