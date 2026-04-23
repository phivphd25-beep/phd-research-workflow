# Methodology

## 1. Purpose of the Dataset
The dataset is used to analyze relationships between different variables such as score, temperature, and humidity. It serves as a simple experimental dataset to demonstrate data cleaning and visualization techniques.

## 2. Handling Missing Values
Missing numeric values were handled using mean imputation. Each missing value was replaced with the average value of its respective column.

## 3. Reason for Choosing This Strategy
Mean imputation was chosen because it is simple, easy to implement, and suitable for small experimental datasets. It helps maintain the overall distribution of the data without removing records.

## 4. Visualizations Generated
The following visualizations were created:
- Score plot to observe variation in values
- Temperature vs humidity plot to study environmental relationships

These visualizations help identify patterns and trends in the dataset.

## 5. Limitations
- Mean imputation may introduce bias if the data is not normally distributed
- Outliers can affect the mean value significantly
- The dataset is small and may not represent real-world complexity