## 📊 EDA Quick Revision Notes

### 🔎 How to Detect Outliers

Use these 3 checks:

- Mean far from median  
- Max much larger than 75th percentile  
- Standard deviation unusually high compared to mean  

If all three happen → likely outliers.


### 📈 How to Detect Skewness

Compare Mean and Median (50% value).

- Mean > Median → Right Skew  
  Most values are small  
  Few values are very large  

- Mean < Median → Left Skew  
  Most values are large  
  Few values are very small  

If Mean ≠ Median → data is skewed.


### ⚠ Why Skewed Data Matters

Skewed data affects:

- Scaling  
- Model performance  
- Outlier impact  


### 📊 Understanding Standard Deviation

- Std > Mean → High spread, possible skew  
- Std < Mean → More stable distribution  


### 🧠 EDA Mindset

EDA is not random plotting.

Always ask:

Does this feature affect the target?

Only analyze features that logically impact the outcome.


### 🧮 Missing Value Handling Rule

- Numeric + Skewed → Use Median  
- Numeric + Normal → Use Mean  
- Categorical → Use Mode  
