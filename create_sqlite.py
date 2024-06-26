import sqlite3
import pandas as pd

from pathlib import Path

database_path = "wind_farm_a_data.sqlite"
Path(database_path).touch()

conn = sqlite3.connect(database_path)
c = conn.cursor()

c.execute('''CREATE TABLE wind_farm_a_data (
    time_stamp timestamp,
    asset_id INT,
    status_type_id INT,
    sensor_0_avg FLOAT,
    sensor_1_avg FLOAT,
    sensor_2_avg FLOAT,
    wind_speed_3_avg FLOAT,
    wind_speed_4_avg FLOAT,
    wind_speed_3_max FLOAT,
    wind_speed_3_min FLOAT,
    wind_speed_3_std FLOAT,
    sensor_5_avg FLOAT,
    sensor_5_max FLOAT,
    sensor_5_min FLOAT,
    sensor_5_std FLOAT,
    sensor_6_avg FLOAT,
    sensor_7_avg FLOAT,
    sensor_8_avg FLOAT,
    sensor_9_avg FLOAT,
    sensor_10_avg FLOAT,
    sensor_11_avg FLOAT,
    sensor_12_avg FLOAT,
    sensor_13_avg FLOAT,
    sensor_14_avg FLOAT,
    sensor_15_avg FLOAT,
    sensor_16_avg FLOAT,
    sensor_17_avg FLOAT,
    sensor_18_avg FLOAT,
    sensor_18_max FLOAT,
    sensor_18_min FLOAT,
    sensor_18_std FLOAT,
    sensor_19_avg FLOAT,
    sensor_20_avg FLOAT,
    sensor_21_avg FLOAT,
    sensor_22_avg FLOAT,
    sensor_23_avg FLOAT,
    sensor_24_avg FLOAT,
    sensor_25_avg FLOAT,
    sensor_26_avg FLOAT,
    reactive_power_27_avg FLOAT,
    reactive_power_27_max FLOAT,
    reactive_power_27_min FLOAT,
    reactive_power_27_std FLOAT,
    reactive_power_28_avg FLOAT,
    reactive_power_28_max FLOAT,
    reactive_power_28_min FLOAT,
    reactive_power_28_std FLOAT,
    power_29_avg FLOAT,
    power_29_max FLOAT,
    power_29_min FLOAT,
    power_29_std FLOAT,
    power_30_avg FLOAT,
    power_30_max FLOAT,
    power_30_min FLOAT,
    power_30_std FLOAT,
    sensor_31_avg FLOAT,
    sensor_31_max FLOAT,
    sensor_31_min FLOAT,
    sensor_31_std FLOAT,
    sensor_32_avg FLOAT,
    sensor_33_avg FLOAT,
    sensor_34_avg FLOAT,
    sensor_35_avg FLOAT,
    sensor_36_avg FLOAT,
    sensor_37_avg FLOAT,
    sensor_38_avg FLOAT,
    sensor_39_avg FLOAT,
    sensor_40_avg FLOAT,
    sensor_41_avg FLOAT,
    sensor_42_avg FLOAT,
    sensor_43_avg FLOAT,
    sensor_44 FLOAT,
    sensor_45 FLOAT,
    sensor_46 FLOAT,
    sensor_47 FLOAT,
    sensor_48 FLOAT,
    sensor_49 FLOAT,
    sensor_50 FLOAT,
    sensor_51 FLOAT,
    sensor_52_avg FLOAT,
    sensor_52_max FLOAT,
    sensor_52_min FLOAT,
    sensor_52_std FLOAT,
    sensor_53_avg FLOAT
)''')

csv_icecream = pd.read_csv("wind_farm_a_data.csv")
csv_icecream.to_sql("wind_farm_a_data", conn, if_exists='append', index=False)

conn.close()
