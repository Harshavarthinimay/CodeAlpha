# 📈 Sales Prediction using Python

This project predicts future sales based on advertising spend, target segment, and platform using regression models.

## Features
- Data cleaning and preprocessing
- Feature encoding and selection
- Linear regression modeling
- Advertising impact analysis
- Actionable business insights

## Folder Structure
- `data/` - contains the dataset (`advertising.csv`)
- `notebooks/` - Jupyter notebook for experimentation
- `src/` - script to train and evaluate model

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sales-prediction.git
   cd sales-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the notebook or script:
   ```bash
   jupyter notebook notebooks/sales_prediction.ipynb
   ```
   or
   ```bash
   python src/model.py
   ```

## Sample Dataset Columns
- TV
- Radio
- Social Media
- Platform
- Target_Segment
- Sales

> Replace `advertising.csv` with your actual dataset if different.

## License
MIT
