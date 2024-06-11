
![PrestigeWhirldWind](https://github.com/Focused79/project4_bad_mother_clusters/assets/152096353/512d8d52-55da-4287-8323-6438d25b5a5e)


# Prestige WhirldWind
Martin Z. Paul A. Matt Z. Mario G. 

> For project four, we are focusing on predictive maintenance for renewable energy systems. This project addresses critical challenges in the industry, the longevity of cutting-edge technology, and aims to contribute to a sustainable future. Our goal is to combine the practical benefits of cost savings and efficiency with the broader goal of supporting global renewable energy initiatives. This project was completed with the support of Peers, Stack Overflow, Google, AI, and Activities. 

Our research aims to address these key questions:

1. How can predictive maintenance contribute to renewable energy systems sustainability?

2. What trends can be identified in the cost production of turbine installation from historical data?

3. What is the optimal strategy for using classification models to identify failure points?

# Electricity Cost Analysis

According to the United States Energy Information Administration, the average U.S. home purchases 899 kWh of energy per month.

The United States Geological Survey states that a wind turbine with a 42% capacity factor (the average among recently built wind turbines since 2021), generates over 843,000 kWh of electricity per month. 

This means that one wind turbine that came online in 2020 generates enough electricity to power 937 US homes a month.


$\text{Number of homes powered per month} = \frac{{843,000kWh}}{{899 kWh/home}}=937.71 \text{ homes}$



it takes this wind turbine 46.8 minutes to power 1 US home.



$\text{Time to power one home for one month} = \frac{{1 \text{ home}}}{{937.71 \text{ homes/month}}}=0.001066 \text{ months}$



Currently, wind turbines experience around 23 hours of downtime per month, the equivalent of roughly 30 homes per month. With our predictive modeling in place to identify up to 75% of failures, this downtime could be cut to roughly six hours per month. Thats enough to power 22 homes per month **per wind turbine using our predictive maintenance model!**


## Visualizations: Bar Chart, Data Results Output, Neural Network


* Bar Chart displaying **Replacement Costs** with hover over tooltip details. The color gradients represent years and cost percentage. The higher the percentage the darker the color; the years are placed in a chronological order colored from light to dark.

* The **Data Trial Results** displays how a dataset can be fed into a model to correctly predict faulty sensor issues of wind turbines with 75% accuracy.

* Mock **Neural Network** Demo  



## Demo
![Screenshot 2024-06-10 at 3 28 12 PM](https://github.com/Focused79/project4_bad_mother_clusters/assets/152096353/8ccf3151-afad-4945-8a45-868cee7e3346)

 

>Bar Chart displaying **Replacement Costs** with hover over tooltip details. The color gradients represent years and cost percentage. (Tableau)

![MachineLearningCodePaul-ezgif com-video-to-gif-converter](https://github.com/Focused79/project4_bad_mother_clusters/assets/152096353/1a9f4566-c14e-4ab0-b9ef-41c227df5d4c)

>The **Data Trial Results** displays how a dataset can be fed into a model to correctly predict faulty sensor issues of wind turbines with 75% accuracy. (Python)

![NeuralNetworkClip-ezgif com-video-to-gif-converter](https://github.com/Focused79/project4_bad_mother_clusters/assets/152096353/6948d743-67d4-4ce0-a140-06947e5df0d6)

>The Mock **Neural Network** Demo  (TensorFlow Playground) 




 **Ethical Consideration**
 The data used is public and we avoided including sensitive information.

## Data Team
Martin Z. - Data Analyst Specialist: Specialized in advanced coding techniques to analyze complex datasets for querying databases, cleaning and transforming data, and creating Neural Network Models.

Paul A. - Data Analyst Specialist: Specialized in advanced coding techniques to analyze complex datasets for querying databases, cleaning and transforming data, and creating Neural Network Models.

Mario G. - Junior Analyst, Visual Communication Specialist: Skilled in information design for presentation, assisted in analyzing data to identify trends, patterns, and correlations. 

Matt Z. - Data Analyst Specialist: Specialized in advanced coding techniques to analyze complex datasets for querying databases, cleaning and transforming data, and creating Neural Network Models. 

### Dataset Citation

Name: **United States Geological Survey Data**
  - Authors: USWTDB -  American Wind Energy Association, LBNL, USGS 
  - Dates: Data is current and updated frequently
  - https://eerscmap.usgs.gov/uswtdb/ 

 Name: **Zenobo Wind Turbine SCADA Data**
  - Authors: Zenbo - Guck, Christian; Roelofs, Cyriana; Maria, Antonia 
  - Dates: Data is current and updated frequently. 
  - https://zenodo.org/records/10958775 

  Name: **International Renewable Energy Agency**
  - Authors: IRENA
  - Renewable Energy and Wind Turbine Installions Costs
  - https://www.irena.org/Publications/2023/Aug/Renewable-Power-Generation-Costs-in-2022
    
  Name: **National Renewable Energy Laboratory**
  - Authors: NREL
  - Cost of Energy Savings
  - https://www.nrel.gov/docs/fy08osti/40581.pdf

### Dataset Description
- Wind Turbine SCADA Data
- Renewable Energy and Wind Turbine Installions & Parts Costs



### Analysis
1. **Predictive Maintenance**: Our analysis shows neural networks can signifcantly improve cost efficiency through predictive maintenance. Neural network are essential for Wind Turbine renewable energy systems and can a increase reliability, lower maintenance costs, and improved sustainability, contributing to a more efficient energy supply.

2. **Cost Trends**: Analyzing wind turbine cost breakdowns highlights the production complexity and the importance of effective maintainance. Technological advancements, government policies, lower material costs, and improved practices have driven down production costs globally from 2010 to 2022. 

3. **Strategy**: Utilizing a model to identify non-operational turbine data from historical datasets allows us to detect trends in faulty equipment. This empowers us to make preemptive decisions, such as dispatching maintenance workers and consulting engineers to troubleshoot potential issues, minimizing repair and breakdown costs.

## Summary
Our analysis shows that neural networks can significantly enhance cost efficiency and reliability in wind turbine renewable energy systems through predictive maintenance. By analyzing historical data to identify trends in faulty equipment, these models enable preemptive actions such as dispatching maintenance workers and consulting engineers, reducing repair and breakdown costs. Technological advancements, and improved practices in neural networks contribute to lower production costs globally, highlighting the importance of effective maintenance in sustaining reneable energy.






