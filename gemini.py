import google.generativeai as genai
import os
api_key = os.getenv("GEMINI_API_TOKEN")
genai.configure(api_key=api_key)




def generate_query_result(question, schema):
    prompt = f"""
    You are an expert in converting English questions to SQL query!
    The SQL database has the following schema -
    {schema};
    
    For example,
    Example 1 - What is the number of cars with more than 4 cylinders?,
    the SQL command will be something like this SELECT COUNT(*) AS num_cars_with_more_than_4_cylinders FROM Cars WHERE Cylinders > 4;

    Example 2 - For each continent, how many countries are there?,
    the SQL command will be something like this SELECT Continent, COUNT(DISTINCT Country) AS num_countries FROM Cars GROUP BY Continent;

    also the sql code should not have ``` in beginning or end and sql word in output;
    the sql code should only be in context of table Cars and its columns;
    There is no need to join other tables or use other tables in the database;
    """

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text


# y = generate_query_result("What is the number of cars with more than 4 cylinders?", "Cars (CarID, MPG, Cylinders, Edispl, Horsepower, Weight, Accelerate, Year, Model, Make, MakerID, Maker, FullName, Country, CountryName, ContinentID, Continent, language_id, name, overall_score, justice_score)")