# CSV Analyzer

## 📊 Project Overview

CSV Analyzer is a Django-based web application that allows users to upload CSV files, perform data analysis using pandas and numpy, and display the results and visualizations on a web interface.

This project was developed as part of an internship assessment, demonstrating skills in web development, data analysis, and data visualization.

## 🚀 Features

- **File Upload**: Users can easily upload CSV files through a user-friendly interface.
- **Data Analysis**: The application performs basic data analysis tasks including:
  - Displaying the first few rows of the data
  - Calculating summary statistics (mean, median, standard deviation) for numerical columns
  - Identifying and handling missing values
- **Data Visualization**: Generates basic plots such as histograms for numerical columns.
- **Filtering**: Users can filter the data based on specific columns and values.
- **PDF Download**: Analysis results can be downloaded as a PDF file.

## 🛠️ Technologies Used

- Django
- Pandas
- NumPy
- Matplotlib
- Seaborn
- HTML/CSS
- JavaScript (for PDF generation)

## 📋 Setup Instructions

1. **Clone the repository**
  ```
  git clone https://github.com/your-username/csv-analyzer.git
  cd csv-analyzer
  ```
2. **Create a virtual environment**
  ```
  python -m venv venv
  ```
3. **Activate the virtual environment**
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. **Install the required packages**
  ```
  pip install -r requirements.txt
  ```
5. **Create a folder named 'media' in your project's root directory**

6. **Set up SECRET_KEY**
- In the `settings.py` file, locate the following line:
  ```python
  SECRET_KEY = 'enter-your-django-secret-key-here'
  ```
- Replace 'enter-your-django-secret-key-here' with a new secret key. You can generate a new key by running the following Python code:
  ```python
  from django.core.management.utils import get_random_secret_key
  print(get_random_secret_key())
  ```
- Copy the generated key and paste it as the SECRET_KEY value in `settings.py`.

7. **Set DEBUG value**
- For development, ensure DEBUG is set to True in `settings.py`:
  ```python
  DEBUG = True
  ```
- Note: Set DEBUG to False in a production environment.

8. **Run migrations**
  ```
  python manage.py migrate
  ```
9. **Start the development server**
  ```
  python manage.py runserver
  ```
10. Open your web browser and navigate to `http://127.0.0.1:8000/`

## 🔧 Usage

1. On the home page, click on "Choose CSV File" to select your CSV file.
2. Click "Upload and Analyze" to process the file.
3. View the analysis results, including summary statistics and visualizations.
4. Use the filter option to refine the data if needed.
5. Click "Download Analysis (PDF)" to save the results as a PDF file.

## 🧪 Sample Data

A sample data is included in the repository(Sample Data) for testing purposes. You can use this file to test the functionality of the application.

## 👀 Demo Video


https://github.com/user-attachments/assets/74179030-d8ae-4248-b9fa-fbd73bb032c1



## 👤 Author

- GitHub: (https://github.com/krakken190)
- LinkedIn: (https://www.linkedin.com/in/prajwal-dongre-/)

## 🔐 Security Notes

- Never share your `SECRET_KEY` publicly or commit it to the repository.
- In a production environment, ensure `DEBUG` is set to `False` in `settings.py`.
- Consider using environment variables for sensitive settings in a production setup.

---

<p align="center">
made with 👨‍💻 by [Prajwal Dongre]
</p>
