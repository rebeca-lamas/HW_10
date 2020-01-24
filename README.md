# Climate Analysis and Exploration
## Precipitation Analysis
We will analyze the climate for Hawaii's for a specific data range for a potential vacation. Python and SQLAlchemy were used to initially explore the climate database. Precipitation was analyzed for the past 12 months. The results were then plotted using Matplotlib. Next the stations were analyzed. The total number of stations were calculated, then the most active station was determined. Next, the last 12 months of temperature data was queried, filtered and plotted as a histogram. 
## Climate App
Based on the above queries, a Flask API was designed. It included the following routes:
* /
* /api/v1.0/precipitation
* /api/v1.0/stations
* /api/v1.0/tobs
* /api/v1.0/< start >
* /api/v1.0/< start >/< end >
