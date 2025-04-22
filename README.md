# 🚴‍♂️ Rent A Bike With Dynamic Price Adjustment

A smart bike rental price prediction web app built using **Streamlit** and **TensorFlow**. The application dynamically adjusts bike rental prices based on real-time **weather conditions**, **season**, **day of the week**, and **city-specific currency rates**.

---

## ✨ Features

- Real-time **weather API** integration
- Intelligent **season and holiday detection**
- Neural network-based **rental demand prediction**
- **Currency API** support for localized pricing
- Dynamic **health rating** of conditions for bike riding
- Responsive **bike gallery with prices**

---

## ⚙️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, TensorFlow (Keras)
- **APIs**: OpenWeatherMap, Currency Conversion API
- **Deployment**: Streamlit Share / Localhost

---

The Dataset used to train the model From Seoul City 
* One can download the following dataset from Kaggle : https://www.kaggle.com/datasets/joebeachcapital/seoul-bike-sharing?resource=download

---

## 📁 File Structure

```bash
├── .devcontainer/             # Dev container setup
├── Model/                     # Multiple Models we trained in the experimentation phase but the  (normalized_model.h5) model was the best and is used in the application
├── datasets/                  # Contains BikeData.csv used for training the model
├── images/                    # UI images and Model performance insights 
├── training/                  # Model training scripts and notebooks used for experimentation
├── LICENSE
├── README.md
├── environment.yml            # Environment dependencies
├── main.py                    # Streamlit app entry point

```
---

🖼️ Images & Description
Below is an example of the Streamlit interface:
---

🚀 How To Run
1) Clone the repository

```bash
git clone https://github.com/vrmaverick/RentalBike
cd RentalBike
```
2) Create a virtual environment and activate it
```bash
conda env create -f environment.yml
conda activate bikeshare
```
3) Set your API keys (# If you want to try )
```bash
Weather_API = "your_openweathermap_api_key"
Currencey_API = "your_currency_api_endpoint"
```

4) Run the app

```bash
streamlit run main.py
```

---

🔌 APIs Used
🌤️ OpenWeatherMap API – For real-time weather data
💱 Currency Conversion API – To adjust prices by local currency

---

Let me know if you'd like me to directly export this as a file or expand the image descriptions for more screenshots! 
vedantranade2612@gmail.com
[My Portfolio](https://vedant-ranade.netlify.app/)
[My LinkdIn](https://www.linkedin.com/in/vedant-ranade-683867271/)


