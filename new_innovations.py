clusters = {
    "AI and ML": {
        "AI in Finance and Business": ["AI financial research", "Financial AI", "AI in finance", "AI-driven business models", "AI-powered investment analysis", "Predictive startup analytics", "AI in business operations", "Business intelligence AI", "AI in business strategy"],
        "AI Development and Tools": ["AI Development Tools", "AI Development Environment", "AI Research Lab", "AI Innovation Platform", "AI Data Refining", "Machine Learning Platform", "ML Resource Management", "AI Training Platform"],
        "AI in Productivity and Operations": ["AI for productivity", "AI-powered operations management", "AI Cost Reduction", "AI Accessibility", "AI in organizational efficiency", "AI in Human Resources", "AI Workforce Management", "AI in job automation analysis"],
        "AI in Specific Applications": ["AI in privacy protection", "Privacy-preserving AI", "AI-driven data privacy", "AI in product development", "Rapid prototyping AI", "Intelligent feature generation", "AI-generated legal threat simulation"],
        "AI Education and Training": ["AI Education", "AI Training Platform", "Digital learning platform", "Interactive education", "Content-based learning", "AI in Education", "AI Training Data Acquisition", "AI in team management"]
    },
    "Energy and Environmental Technologies": {
        "Renewable Energy": ["Solar-powered devices", "Solar PV Manufacturing", "Ground-mounted solar systems", "Bifacial Solar Cells", "Community Solar Energy", "Onshore wind farms", "Wind power generation", "Renewable energy systems"],
        "Energy Storage and Efficiency": ["Energy Storage Systems", "Energy Efficiency", "Sustainable Solar Solutions", "Gas recycling"],
        "Green Energy Production": ["Clean Energy", "Green Hydrogen Production", "Nuclear Energy", "Renewable Energy Development", "Energy Generation"],
        "Sustainable Practices": ["Sustainable Steel Production", "Low-Carbon Industrial Processes", "Sustainable Waste Management", "Sustainable Procurement", "Green Supply Chain", "Environmental Governance"]
    },
    "Aerospace and Defense": {
        "Aircraft and Aviation": ["Next-gen aircraft design", "Bio-inspired flight systems", "Advanced Military Technology", "High-Speed UAVs", "Hypersonic Flight", "Supersonic Aviation", "Military Aircraft"],
        "Defense Systems": ["Directed-Energy Weapons", "Counter-Drone Systems", "Autonomous military robots", "Electronic Warfare", "Air Defense Systems", "Land-based Missile Defense"],
        "Naval and Marine Technologies": ["Underwater Propulsion", "Underwater Electric Propulsion", "Electric Naval Vessels", "Naval Weaponry", "Antisubmarine Warfare", "Naval Vessel Maintenance"]
    },
    "Medical and Biotech Innovations": {
        "Medical Devices and Treatments": ["Cardiovascular therapies", "Cardiovascular Interventional Devices", "Novel statin alternatives", "Medical Device Improvisation", "Unconventional Medical Solutions"],
        "Biotechnology": ["Cellular Agriculture", "Synthetic manufacturing", "Lab-grown materials", "Synthetic Viral Engineering", "Gene editing obesity treatments"],
        "Vaccines and Pharmaceuticals": ["Urinary Tract Infection Vaccines", "Bacterial Infection Vaccines", "Oral Vaccines", "Fermentation-based antibiotics production"]
    },
    "Transportation and Automotive": {
        "Electric Vehicles (EVs)": ["Affordable EVs", "Electric Sedans", "Mass EV Production", "EV Production Optimization", "Premium Electric Vehicles"],
        "Advanced Vehicle Technologies": ["Racing Car Technology", "High-Performance Vehicles", "Supersonic Aerial Vehicles", "Electric SUVs"],
        "Maritime and Underwater Vehicles": ["Lithium-Ion Submarines", "Underwater Exploration", "Autonomous Underwater Systems", "Nuclear Submarines"]
    },
    "Materials and Manufacturing": {
        "Advanced Materials": ["Organic Solar Cells", "Artificial gemstones", "Lab-grown materials", "Low-cost EVs", "Flexible Materials"],
        "Manufacturing Technologies": ["Semiconductor fabrication", "Advanced Microchips", "Production Scheduling", "Manufacturing Flexibility", "Laser Engraving", "Laser Marking"]
    },
    "Communication and Data Technologies": {
        "Data and Information Systems": ["High-Speed Data Transfer", "Machine Learning Infrastructure", "AI Data Processing", "Real-time Data Management", "Enterprise AI Solutions"],
        "Networking and Connectivity": ["Undersea fiber optic cables", "Satellite Constellations", "Network-enabled military operations"],
        "Visualization and Analytics": ["Data Visualization", "Predictive Analytics", "Advanced Analytics", "Astrophysical Visualization"]
    },
    "Construction and Infrastructure": {
        "Sustainable Construction": ["Seismic-resistant construction", "Earthquake-resistant infrastructure", "Climate-Resilient Naval Operations"],
        "Urban Development": ["Urban Infrastructure Management", "Modular Infrastructure", "Sustainable Landscaping", "Smart Urban Agriculture"],
        "Innovative Building Materials": ["Textile recycling technology", "Flooring material quality control", "Surface Restoration", "Antique Preservation"]
    },
    "Financial and Legal Technologies": {
        "Financial Platforms": ["Rapid Capital Access Platforms", "Startup Funding Platforms", "AI in startup analysis", "Predictive startup analytics"],
        "Legal Technologies": ["AI in Law Enforcement", "AI for Judicial Systems", "Legal Tech AI", "Autonomous Intellectual Property Management"]
    },
    "Education and Learning Technologies": {
        "Learning Platforms": ["AI Education", "AI Training Platform", "Digital learning platform", "Interactive education", "Content-based learning", "Cloud-based Learning Platforms"],
        "Training and Development": ["Vocational Training", "Professional Certification", "Accelerated Learning", "AI Workforce Development", "AI Talent Acquisition"]
    },
    "Robotics and Automation": {
        "Industrial Automation": ["Autonomous Software Development", "Autonomous Workforce Development", "AI-driven Process Optimization"],
        "Service Robots": ["Interactive robots", "Robot-assisted computing", "Humanoid robots"],
        "Specialized Robotics": ["AI in Immigration", "AI in product development", "Rapid prototyping AI"]
    },
    "Consumer Electronics and Lifestyle": {
        "Customizable Devices": ["Modular computing", "Open-source hardware", "Customizable electronics"],
        "Smart Home and Lifestyle": ["Fast Charging Accessories", "Compact Charging Solutions", "Smart Golf Equipment"]
    },
    "Security and Surveillance": {
        "Surveillance Technologies": ["Aerial Surveillance", "Intelligent dashboard systems", "Electronic Warfare", "Collision Avoidance Systems"],
        "Security Systems": ["Acoustic weaponry", "Non-lethal weapons", "Counter-Drone Systems", "AI in Law Enforcement"]
    },
    "Sustainable and Green Technologies": {
        "Environmental Conservation": ["Glacier Preservation", "Ocean Conservation", "Climate Change Mitigation", "Ecological Restoration Tools"],
        "Green Manufacturing": ["Sustainable Automotive Manufacturing", "Sustainable Procurement", "Green Supply Chain", "Environmental Governance"]
    },
    "Ocean and Underwater Technologies": {
        "Marine Exploration": ["Underwater Exploration", "Autonomous Underwater Systems", "Computational Ocean Acoustics"],
        "Marine Energy": ["Wave energy converters", "Underwater Electric Propulsion", "Energy Generation"]
    },
    "Space and Astronomy": {
        "Space Technologies": ["Astrophysics and Space Exploration", "Space-Based Telescopes", "Satellite Constellations"],
        "Space Missions": ["Space Mission Analytics", "Exoplanetary Science", "Astrophysical Visualization"]
    }
}
import streamlit as st

# Define the clusters

# Function to display inner categories
def display_inner_categories(inner_categories):
    for inner in inner_categories:
        st.write(f"- {inner}")

# Main function to render the dashboard
def main():
    st.title("Interactive Cluster Dashboard")

    selected_category = st.selectbox("Select a Category", list(clusters.keys()))

    if selected_category:
        subcategories = clusters[selected_category]
        selected_subcategory = st.selectbox("Select a Subcategory", list(subcategories.keys()))

        if selected_subcategory:
            inner_categories = subcategories[selected_subcategory]
            st.subheader("Inner Categories")
            display_inner_categories(inner_categories)

if __name__ == "__main__":
    main()
