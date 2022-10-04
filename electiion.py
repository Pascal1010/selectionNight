us_recession_start_years=[1920, 1923, 1926, 1929, 1937,
1945, 1949,1953, 1958, 1960, 1969, 1973, 1980, 1981,
1990, 2001, 2008, 2020]
total_election_years = 0
for year in us_recession_start_years:
    if year % 4 ==0:
        #total_election_years = total_election_years+1
        total_election_years += 1
        print(f"there was a recession in {year}")
print(f"there were {total_election_years} recessions in election years 1920-2020")
