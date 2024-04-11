px.scatter(dataset1.head(100), x='Country/Region', y='TotalCases', 
		hover_data=['Country/Region', 'Continent'], 
		color='TotalCases', size='TotalCases', size_max=80)
px.scatter(dataset1.head(30), x='Country/Region', y='TotalCases', 
		hover_data=['Country/Region', 'Continent'], 
		color='Country/Region', size='TotalCases', size_max=80, log_y=True)
px.scatter(dataset1.head(10), x='Country/Region', y= 'TotalDeaths', 
		hover_data=['Country/Region', 'Continent'], 
		color='Country/Region', size= 'TotalDeaths', size_max=80)
px.scatter(dataset1.head(30), x='Country/Region', y= 'Tests/1M pop', 
		hover_data=['Country/Region', 'Continent'], 
		color='Country/Region', size= 'Tests/1M pop', size_max=80)
px.scatter(dataset1.head(30), x='Country/Region', y= 'Tests/1M pop', 
		hover_data=['Country/Region', 'Continent'], 
		color='Tests/1M pop', size= 'Tests/1M pop', size_max=80)
px.scatter(dataset1.head(30), x='TotalCases', y= 'TotalDeaths', 
		hover_data=['Country/Region', 'Continent'], 
		color='TotalDeaths', size= 'TotalDeaths', size_max=80)
px.scatter(dataset1.head(30), x='TotalCases', y= 'TotalDeaths', 
		hover_data=['Country/Region', 'Continent'], 
		color='TotalDeaths', size= 'TotalDeaths', size_max=80, 
		log_x=True, log_y=True)
px.scatter(dataset1.head(30), x='TotalTests', y= 'TotalCases', 
		hover_data=['Country/Region', 'Continent'], 
		color='TotalTests', size= 'TotalTests', size_max=80, 
		log_x=True, log_y=True)
px.bar(dataset2, x="Date", y="Confirmed", color="Confirmed", 
	hover_data=["Confirmed", "Date", "Country/Region"], height=400)
px.bar(dataset2, x="Date", y="Confirmed", color="Confirmed", 
	hover_data=["Confirmed", "Date", "Country/Region"],log_y=True, height=400)
px.bar(dataset2, x="Date", y="Deaths", color="Deaths", 
	hover_data=["Confirmed", "Date", "Country/Region"], 
	log_y=False, height=400)
px.bar(dataset1.head(15), x = 'TotalTests', y = 'Country/Region', 
	color = 'TotalTests',orientation ='h', height = 500, 
	hover_data = ['Country/Region', 'Continent'])
px.bar(dataset1.head(15), x = 'TotalTests', y = 'Continent', 
	color = 'TotalTests',orientation ='h', height = 500, 
	hover_data = ['Country/Region', 'Continent'])
px.scatter(dataset1, x='Continent',y='TotalCases', 
		hover_data=['Country/Region', 'Continent'], 
		color='TotalCases', size='TotalCases', size_max=80)
px.scatter(dataset1.head(57), x='Continent',y='TotalCases', 
		hover_data=['Country/Region', 'Continent'], 
		color='TotalCases', size='TotalCases', size_max=80, log_y=True)
px.scatter(dataset1.head(54), x='Continent',y='TotalTests', 
		hover_data=['Country/Region', 'Continent'], 
		color='TotalTests', size='TotalTests', size_max=80)
px.scatter(dataset1.head(50), x='Continent',y='TotalTests', 
		hover_data=['Country/Region', 'Continent'], 
		color='TotalTests', size='TotalTests', size_max=80, log_y=True)
px.scatter(dataset1.head(100), x='Country/Region', y='TotalCases', 
		hover_data=['Country/Region', 'Continent'], 
		color='TotalCases', size='TotalCases', size_max=80)
px.scatter(dataset1.head(30), x='Country/Region', y='TotalCases', 
		hover_data=['Country/Region', 'Continent'], 
		color='Country/Region', size='TotalCases', size_max=80, log_y=True)
px.scatter(dataset1.head(10), x='Country/Region', y= 'TotalDeaths', 
		hover_data=['Country/Region', 'Continent'], 
		color='Country/Region', size= 'TotalDeaths', size_max=80)
px.scatter(dataset1.head(30), x='Country/Region', y= 'Tests/1M pop', 
		hover_data=['Country/Region', 'Continent'], 
		color='Country/Region', size= 'Tests/1M pop', size_max=80)
px.scatter(dataset1.head(30), x='Country/Region', y= 'Tests/1M pop', 
		hover_data=['Country/Region', 'Continent'], 
		color='Tests/1M pop', size= 'Tests/1M pop', size_max=80)
px.scatter(dataset1.head(30), x='TotalCases', y= 'TotalDeaths', 
		hover_data=['Country/Region', 'Continent'], 
		color='TotalDeaths', size= 'TotalDeaths', size_max=80)
px.scatter(dataset1.head(30), x='TotalCases', y= 'TotalDeaths', 
		hover_data=['Country/Region', 'Continent'], 
		color='TotalDeaths', size= 'TotalDeaths', size_max=80, 
		log_x=True, log_y=True)
px.scatter(dataset1.head(30), x='TotalTests', y= 'TotalCases', 
		hover_data=['Country/Region', 'Continent'], 
		color='TotalTests', size= 'TotalTests', size_max=80, 
		log_x=True, log_y=True)
