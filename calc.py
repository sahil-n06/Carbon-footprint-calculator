import random

def generate_tips():
    tips = [
        "Switch to energy-efficient appliances!",
        "Carpool or use public transport to reduce emissions.",
        "Go vegan for a day to cut down on food-related CO2!",
        "Unplug devices when not in use to save power.",
        "Consider using renewable energy sources like solar power.",
        "Reduce, Reuse, Recycle – it really makes a difference!",
    ]
    return random.choice(tips)

def carbon_footprint_calculator():
    print("🌍 Welcome to the Crazy Carbon Footprint Calculator! 🚀")
    
    # Electricity Consumption
    electricity_kwh = float(input("⚡ Enter your monthly electricity consumption (in kWh): "))
    electricity_emission_factor = 0.92  # kg CO2 per kWh
    electricity_emissions = electricity_kwh * electricity_emission_factor
    
    # Transportation
    vehicle_km = float(input("🚗 Enter the distance you drive per month (in km): "))
    fuel_efficiency = float(input("⛽ Enter your vehicle's fuel efficiency (km per liter): "))
    fuel_emission_factor = 2.31  # kg CO2 per liter of gasoline
    fuel_consumed = vehicle_km / fuel_efficiency
    transport_emissions = fuel_consumed * fuel_emission_factor
    
    # Food Consumption
    meat_consumption = float(input("🍖 How many servings of meat do you eat per week? "))
    dairy_consumption = float(input("🥛 How many servings of dairy do you consume per week? "))
    plant_based_consumption = float(input("🥗 How many servings of plant-based meals do you have per week? "))
    
    meat_emission_factor = 27.0  # kg CO2 per serving per year
    dairy_emission_factor = 9.0  # kg CO2 per serving per year
    plant_based_emission_factor = 2.0  # kg CO2 per serving per year
    
    food_emissions = ((meat_consumption * meat_emission_factor) + (dairy_consumption * dairy_emission_factor) + (plant_based_consumption * plant_based_emission_factor)) / 52
    
    # Total Carbon Footprint
    total_emissions = electricity_emissions + transport_emissions + food_emissions
    
    print("\n🌱 Your estimated monthly carbon footprint is:")
    print(f"⚡ Electricity: {electricity_emissions:.2f} kg CO2")
    print(f"🚗 Transportation: {transport_emissions:.2f} kg CO2")
    print(f"🍽️ Food: {food_emissions:.2f} kg CO2")
    print(f"🔥 TOTAL: {total_emissions:.2f} kg CO2")
    
    if total_emissions < 200:
        print("🎉 Amazing! Your carbon footprint is super low. Mother Earth loves you! 💚")
    elif total_emissions < 500:
        print("😎 Not bad! But you can still do better. Keep up the good work!")
    else:
        print("🚨 Whoa! Your carbon footprint is on fire! Time to switch to greener habits! 🌿")
    
    print("💡 Eco Tip: " + generate_tips())
    
if __name__ == "__main__":
    carbon_footprint_calculator()
