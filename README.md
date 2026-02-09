US Accidents Data Analysis and Visualization

Dataset:

The dataset used is US_Accidents_March23.csv, which contains accident records across the United States including accident time, location coordinates, severity level, weather conditions, visibility, wind speed, precipitation, light conditions, and accident distance impact.

Technologies Used:

Python
Pandas
NumPy
Matplotlib

Project Features:

Analyzes accident frequency by hour of the day
Analyzes accident trends by day of the week
Displays monthly accident trends
Shows accident severity distribution
Analyzes weather conditions during accidents
Compares severity across weather conditions
Analyzes hourly accidents based on severity
Identifies accident hotspot cities
Visualizes geographic accident density using hexbin plots
Analyzes accident distance distribution
Examines visibility, wind speed, and precipitation impact on severity
Analyzes accidents by light condition

Data Processing Steps:

Loads accident dataset using Pandas
Converts time columns into datetime format
Extracts hour, day, and month from accident time
Orders weekdays for proper visualization
Handles missing values and removes invalid data
Applies sampling for large geographic datasets
Clips extreme outliers for better visualization clarity

Visualizations Generated:
]
Line chart showing accidents by hour
Bar chart showing accidents by weekday
Line chart showing monthly accident trends
Bar chart showing severity distribution
Weather condition accident comparison charts
Stacked bar chart for severity across weather types
Line chart for hourly accidents by severity
Bar chart for top accident hotspot cities
Hexbin map showing accident density
Histogram showing accident distance distribution
Boxplot showing visibility vs severity
Bar charts showing wind speed and precipitation impact
Bar chart showing accidents by day and night

How to Run the Project:

Install required libraries using:

pip install pandas numpy matplotlib

Update dataset file path inside the script

Run the script using:

python accident_analysis.py

Expected Output:

Multiple charts visualizing accident trends and patterns across different factors.

Notes:

The dataset is large and may require higher system memory
Geographic plots use sampling for faster performance
Some extreme values are clipped to improve visualization clarity

Future Improvements:

Add interactive dashboards using Plotly or Tableau
Build machine learning models for accident severity prediction
Perform state-wise or region-wise accident comparison
Integrate real-time traffic accident data
Develop accident risk prediction system
