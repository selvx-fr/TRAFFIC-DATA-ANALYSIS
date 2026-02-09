import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r"C:\Users\selvxfr\Downloads\US_Accidents_March23.csv"
df = pd.read_csv(file_path, low_memory=False)

if 'Start_Time' in df.columns:
    df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
else:
    raise ValueError("Start_Time column not found")

if 'End_Time' in df.columns:
    df['End_Time'] = pd.to_datetime(df['End_Time'], errors='coerce')

df['Hour'] = df['Start_Time'].dt.hour
df['DayOfWeek'] = df['Start_Time'].dt.day_name()
df['Month'] = df['Start_Time'].dt.to_period('M').astype(str)

weekday_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
df['DayOfWeek'] = pd.Categorical(df['DayOfWeek'], categories=weekday_order, ordered=True)

plt.figure(figsize=(10,5))
df['Hour'].value_counts().sort_index().plot(kind='line', marker='o')
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(9,5))
df['DayOfWeek'].value_counts().reindex(weekday_order).plot(kind='bar')
plt.title("Accidents by Day of Week")
plt.xlabel("Day")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(11,5))
df['Month'].value_counts().sort_index().plot(kind='line', marker='o')
plt.title("Monthly Trend of Accidents")
plt.xlabel("Month")
plt.ylabel("Count")
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.tight_layout()
plt.show()

if 'Severity' in df.columns:
    plt.figure(figsize=(7,5))
    df['Severity'].value_counts().sort_index().plot(kind='bar')
    plt.title("Accident Severity Distribution")
    plt.xlabel("Severity")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

if 'Weather_Condition' in df.columns:
    plt.figure(figsize=(12,5))
    df['Weather_Condition'].value_counts().head(15).plot(kind='bar')
    plt.title("Top 15 Weather Conditions During Accidents")
    plt.xlabel("Weather Condition")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if {'Weather_Condition','Severity'}.issubset(df.columns):
    top_weather = df['Weather_Condition'].value_counts().head(8).index
    pivot_ws = df[df['Weather_Condition'].isin(top_weather)].pivot_table(index='Weather_Condition', columns='Severity', values='ID' if 'ID' in df.columns else df.columns[0], aggfunc='count', fill_value=0)
    pivot_ws = pivot_ws.loc[top_weather]
    pivot_ws.plot(kind='bar', stacked=True, figsize=(12,6))
    plt.title("Severity Mix by Top Weather Conditions")
    plt.xlabel("Weather Condition")
    plt.ylabel("Accident Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if {'Hour','Severity'}.issubset(df.columns):
    hourly_sev = df.pivot_table(index='Hour', columns='Severity', values='ID' if 'ID' in df.columns else df.columns[0], aggfunc='count', fill_value=0).sort_index()
    hourly_sev.plot(kind='line', figsize=(12,6), marker='o')
    plt.title("Hourly Accidents by Severity")
    plt.xlabel("Hour")
    plt.ylabel("Count")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if 'City' in df.columns:
    plt.figure(figsize=(12,5))
    df['City'].value_counts().head(20).plot(kind='bar')
    plt.title("Top 20 Accident Hotspot Cities")
    plt.xlabel("City")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if {'Start_Lat','Start_Lng'}.issubset(df.columns):
    sample = df[['Start_Lat','Start_Lng']].dropna()
    if len(sample) > 150000:
        sample = sample.sample(150000, random_state=42)
    plt.figure(figsize=(8,6))
    hb = plt.hexbin(sample['Start_Lng'], sample['Start_Lat'], gridsize=60, mincnt=1)
    plt.title("Geographic Accident Hotspots (Hexbin)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    cb = plt.colorbar(hb)
    cb.set_label("Accident Density")
    plt.tight_layout()
    plt.show()

if 'Distance(mi)' in df.columns:
    plt.figure(figsize=(9,5))
    df['Distance(mi)'].clip(upper=df['Distance(mi)'].quantile(0.99)).plot(kind='hist', bins=50)
    plt.title("Distribution of Accident Distance (mi)")
    plt.xlabel("Distance (mi)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

if {'Visibility(mi)','Severity'}.issubset(df.columns):
    data_vs = [df[df['Severity']==s]['Visibility(mi)'].dropna().clip(upper=df['Visibility(mi)'].quantile(0.99)) for s in sorted(df['Severity'].dropna().unique())]
    plt.figure(figsize=(9,5))
    plt.boxplot(data_vs, labels=sorted(df['Severity'].dropna().unique()))
    plt.title("Visibility vs Severity")
    plt.xlabel("Severity")
    plt.ylabel("Visibility (mi)")
    plt.tight_layout()
    plt.show()

if {'Wind_Speed(mph)','Severity'}.issubset(df.columns):
    bins = [-np.inf,5,15,25,40,np.inf]
    labels = ["0-5","6-15","16-25","26-40","40+"]
    spd = pd.cut(df['Wind_Speed(mph)'], bins=bins, labels=labels)
    tbl = pd.crosstab(spd, df['Severity'])
    tbl.plot(kind='bar', figsize=(10,5))
    plt.title("Wind Speed Bands vs Severity")
    plt.xlabel("Wind Speed (mph)")
    plt.ylabel("Accident Count")
    plt.tight_layout()
    plt.show()

if {'Precipitation(in)','Severity'}.issubset(df.columns):
    bins = [-np.inf,0,0.05,0.2,0.5,1,np.inf]
    labels = ["0","0.01-0.05","0.06-0.2","0.21-0.5","0.51-1","1+"]
    pr = pd.cut(df['Precipitation(in)'], bins=bins, labels=labels)
    tbl2 = pd.crosstab(pr, df['Severity'])
    tbl2.plot(kind='bar', figsize=(10,5))
    plt.title("Precipitation Bands vs Severity")
    plt.xlabel("Precipitation (in)")
    plt.ylabel("Accident Count")
    plt.tight_layout()
    plt.show()

if 'Sunrise_Sunset' in df.columns:
    plt.figure(figsize=(7,5))
    df['Sunrise_Sunset'].value_counts().plot(kind='bar')
    plt.title("Accidents by Light Condition")
    plt.xlabel("Light Condition")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()