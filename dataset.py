# Importing Dataset1 
dataset1 = pd.read_csv("covid.csv") 
dataset1.head() # returns first 5 rows 
# Returns tuple of shape (Rows, columns) 
print(dataset1.shape) 

# Returns size of dataframe 
print(dataset1.size) 
# Information about Dataset1 
# return concise summary of dataframe 
dataset1.info() 
# Importing Dataset2 
dataset2 = pd.read_csv("covid_grouped.csv") 
dataset2.head() # return first 5 rows of dataset2 
# Returns tuple of shape (Rows, columns) 
print(dataset2.shape) 

# Returns size of dataframe 
print(dataset2.size) 
# Information about Dataset2 
dataset2.info() # return concise summary of dataframe 
# Columns labels of a Dataset1 
dataset1.columns 
# Drop NewCases, NewDeaths, NewRecovered rows from dataset1 

dataset1.drop(['NewCases', 'NewDeaths', 'NewRecovered'], 
			axis=1, inplace=True) 

# Select random set of values from dataset1 
dataset1.sample(5) 
# Import create_table Figure Factory 

from plotly.figure_factory import create_table 

colorscale = [[0, '#4d004c'], [.5, '#f2e5ff'], [1, '#ffffff']] 
table = create_table(dataset1.head(15), colorscale=colorscale) 
py.iplot(table) 
px.bar(dataset1.head(15), x = 'Country/Region', 
	y = 'TotalCases',color = 'TotalCases', 
	height = 500,hover_data = ['Country/Region', 'Continent'])
px.bar(dataset1.head(15), x = 'Country/Region', y = 'TotalCases', 
	color = 'TotalDeaths', height = 500, 
	hover_data = ['Country/Region', 'Continent'])
px.bar(dataset1.head(15), x = 'Country/Region', y = 'TotalCases', 
	color = 'TotalDeaths', height = 500, 
	hover_data = ['Country/Region', 'Continent'])
px.bar(dataset1.head(15), x = 'Country/Region', y = 'TotalCases', 
	color = 'TotalTests', height = 500, hover_data = ['Country/Region', 'Continent'])
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
