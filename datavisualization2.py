px.bar(dataset2, x="Date", y="Confirmed", color="Confirmed", 
	hover_data=["Confirmed", "Date", "Country/Region"], height=400)
px.bar(dataset2, x="Date", y="Confirmed", color="Confirmed", 
	hover_data=["Confirmed", "Date", "Country/Region"],log_y=True, height=400)
px.bar(dataset2, x="Date", y="Deaths", color="Deaths", 
	hover_data=["Confirmed", "Date", "Country/Region"], 
	log_y=False, height=400)
df_US= dataset2.loc[dataset2["Country/Region"]=="US"]
px.bar(df_US, x="Date", y="Confirmed", color="Confirmed", height=400)
px.bar(df_US,x="Date", y="Recovered", color="Recovered", height=400)
px.line(df_US,x="Date", y="Recovered", height=400)
px.line(df_US,x="Date", y="Deaths", height=400)
px.line(df_US,x="Date", y="Confirmed", height=400)
px.line(df_US,x="Date", y="New cases", height=400)
px.bar(df_US,x="Date", y="New cases", height=400)
px.scatter(df_US, x="Confirmed", y="Deaths", height=400)
