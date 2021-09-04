import requests
import random

categories = ['Femtech', 'Enterprise', 'Energy', 'Industrial', 'Logistics', 'Agritech', 'Aerospace', 'Edtech', 'Fintech',
       'GovTech', 'PropTech', 'IoT', 'Blockchain', 'Consumer', 'Legaltech', 'Robotics', 'DevOps',
       'Greentech', 'Foodtech', 'Transportation', 'Insurtech', 'Gaming', 'Cannabis', 'Cleantech', 'Cybersecurity', 'SocialTech', 
       'Climatetech', 'Insurance', 'Deeptech', 'Creator', 'SportsTech','Telecoms', 'Spacetech', 'Salestech', 'Defensetech', 'Analytics', 
       'Defense', 'Energytech', 'Traveltech', 'Trasportation', 'Games', 'Insuretech', 'Devops', 'Customer', 'RegTech', 'Comptech', 'Dev', 'Transformation',
       'Enterprise Solutions', 'Healthcare', 'Construction', 'Communication', 'Food', 'Fitness', 'Consumer Products', 'Cloud',
       'Consumer Internet', 'Lifestyle', 'Hardware', 'Chemtech', 'Quantum Computing', 'Hardtech', 'Proptech', 'Drones', 'Mobility', 'Safetytech', 'Moonshot', 'Real Estate', 
       'Real estate', 'Communications', 'Digital Infrastructure', 'Hospitality', 'Entertainment', 'EV', 'Socialtech', 'Industry',
       'Media', 'CleanTech', 'Education', 'Marketing', 'Mobile', 'Wearables', 'Drones/Robotics', 'Biotech', 'Big Data']

def get_recent_funded():
    url = 'https://vc-funded-api.herokuapp.com/funded'
    response = requests.get(url).json()[random.randint(1,25)]

    return f"'{response['company_name']}' in the {response['company_category']} sector \n> raised ${response['raise_amount_mill_dollars']}m on {response['raise_date']} \n> {response['company_website']} "

def get_by_category():
    rand_category = categories[random.randint(0,80)]
    url = f"https://vc-funded-api.herokuapp.com/funded/category/{rand_category}"
    response = requests.get(url).json()[0]

    return f"'{response['company_name']}' in the {response['company_category']} sector \n> raised ${response['raise_amount_mill_dollars']}m on {response['raise_date']} \n> {response['company_website']} "

if __name__ == "__main__":
    print(get_recent_funded())
    print(get_by_category())
