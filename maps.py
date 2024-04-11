px.choropleth(dataset2, 
			locations="iso_alpha", 
			color="Confirmed", 
			hover_name="Country/Region", 
			color_continuous_scale="Blues", 
			animation_frame="Date")
px.choropleth(dataset2, 
			locations='iso_alpha', 
			color="Deaths", 
			hover_name="Country/Region", 
			color_continuous_scale="Viridis", 
			animation_frame="Date" )
px.choropleth(dataset2, 
			locations='iso_alpha', 
			color="Recovered", 
			hover_name="Country/Region", 
			color_continuous_scale="RdYlGn", 
			projection="natural earth", 
			animation_frame="Date" )
px.bar(dataset2, x="WHO Region", y="Confirmed", color="WHO Region", 
	animation_frame="Date", hover_name="Country/Region")
