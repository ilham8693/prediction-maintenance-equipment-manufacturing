## Prediction Model of Equipment in Smart Manufacturing for Predictive Maintenance

## Repository Outline
1. README.md - About the project
2. notebook.ipynb - Code script for data analysis and modeling
3. notebook_inf.ipynb - Code script for data inference
4. model_best.pkl - Saved best model
5. dataset.csv - Dataset as source for data analysis

## Problem Background
In a manufacturing environment, the production process is crucial to meet market demand. One key factor in ensuring smooth production is the performance condition of equipment/machines. Smart manufacturing has enabled the collection of real-time operational data from machines via IoT-based systems to enable digital monitoring and ensure efficient processes. One major application of this data is in predictive maintenance strategy to anticipate equipment failures and perform maintenance before breakdowns occur. This helps avoid unexpected downtime, minimizes production halts, and ultimately reduces cost. If the maintannace can be predicted, it will help teams in manufacturing environment (Production, Maintenance and Enginnering teams) to achive production efficiency. This project aims to build a Machine Learning classification model that can predict whether an equipment (under certain operational parameters and time) requires maintenance or not. The goal is to support maintenance and production scheduling with data-driven insights.  For equipment predicted to require maintenance, proactive actions can be scheduled by the maintenance team, coordinated with production, minimizing downtime. For equipment predicted to be healthy, the operational conditions can be studied and used as a benchmark for other machines. This predictive system reduces total maintenance costs and avoids production disruption.

## Project Output
This project aims to perform comprehensive data analysis and develop a machine learning-based predictive maintenance system for smart manufacturing environments. The objective is to analyze operational equipment data and build multiple classification models to predict whether a machine requires maintenance. Five different machine learning algorithms—K-Nearest Neighbors (KNN), Support Vector Machine (SVM), Decision Tree, Random Forest, and XGBoost—will be implemented and compared based on their performance, particularly focusing on recall score, which is crucial to minimize the risk of undetected equipment failures. The best-performing model will support predictive maintenance scheduling, helping reduce downtime, optimize resource allocation, and improve overall production efficiency. `XGBoost` prove to be the best model in this project also after parameter tuning with `recall score` for `train 97%` and `test 91%`.

## Data
The dataset used in this project was sourced from Kaggle.com and is intended for smart manufacturing practice, this dataset offers a comprehensive snapshot of smart manufacturing operations, emphasizing sustainability and process optimization. Provided in CSV format, it contains 100,000 rows and 13 columns with no missing values. List of the colomns:
- Timestamps – Time at which the sensor readings were recorded
- Machine ID – Unique identifier for each machine
- Sensor Reading (five columns) – Temperature, Vibration, Humidity, Pressure, Energy Consumption
- Machine Status – Indicates whether the machine is Idle, Running, or in Failure (0, 1 or 2)
- Anomaly Flags – Identifies extreme values in temperature and vibration
- Predicted Remaining Life – Estimated time before maintenance is needed
- Failure Type – The reason for machine failure (Overheating, Vibration Issue and etc.)
- Downtime Risk Score – Probability of machine breakdown
- Maintenance Required (maintenance_required) – Target column (0 = No, 1 = Yes)

## Method
This project employs Python and its libararies to conduct data analyis and modeling. Analysis and model is deployed in huggingface.co as space and can be used to do exploration and prediction of data.

## Stacks
The programming language, tools, and Python libraries utilized in this project, including:
- Pandas – used for data manipulation and analysis.
- Numpy - used for data manipulation and analysis.
- SciPy Stats – used for performing statistical analysis.
- Matplotlib Pyplot – used for data visualization.
- Seaborn - used for data visualization.
- Scikit-Learn - used for modeling, preprocessing, evaluation, pipieline and etc.
- XGBoost - used for model boosting.

## Reference
- [Dataset Source](https://www.kaggle.com/datasets/ziya07/smart-manufacturing-iot-cloud-monitoring-dataset/data)
- [Deployment Model](https://huggingface.co/spaces/ilham86/manufacturing_predictive_maintenance)