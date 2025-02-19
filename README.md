# Predicting Future Profit of an ECommerce Store using Machine Learning

A small Linear Regression-based model for predicting the yearly cost spent by a customer on an eCommerce store. This project covers data analysis, model training, and deployment using Streamlit for easy interaction.

Specially handcrafted for CodeZen Hackathon -> [Link](https://codezen2025.devfolio.co/overview)

## Demo
![demo_image](https://raw.githubusercontent.com/rajatrajputdev/ecommerce-price-prediction/refs/heads/main/resources/demonstration.png)

## Features
- **Linear Regression Model:** A simple yet effective approach to predicting customer spending.
- **Jupyter Notebook:** Contains code for data analysis, model training, and evaluation.
- **Streamlit App:** Provides an interactive UI to input customer data and get predictions.
- **Deployment Ready:** Can be hosted on cloud platforms like Heroku or Streamlit Sharing.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Jupyter Notebook
- Streamlit
- Required Python libraries (listed below)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/rajatrajputdev/ecommerce-price-prediction.git
   cd ecommerce-price-prediction
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook to explore the dataset and train the model:
   ```sh
   jupyter notebook
   ```
   Open `ECommerce Price Prediction.ipynb` and execute the cells.

## How to Use?
1. Train the Linear Regression model by running `ECommerce Price Prediction.ipynb`.
2. Start the Streamlit app:
   ```sh
   streamlit run app.py
   ```
3. Enter customer details in the UI and get predictions on yearly spending.

## Dataset
The dataset contains customer-related features such as:
- Average Session Length
- Time spent on the website
- Time spent on the app
- Membership status

These features help predict the yearly spending of a customer.

## Model
We use **Linear Regression**, a simple yet powerful algorithm, to predict yearly cost spending based on customer features. The model is trained using `scikit-learn` and evaluated for accuracy.

## Deployment
This project is deployed using:
- **Streamlit Sharing:** Quick and easy deployment.

## Contributing
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

## License
This project is licensed under the MIT License.

**Free and Open Source Software with Open Source Hardware, Hell Yeah!**

