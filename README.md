# CS-340 Grazioso Salvare Animal Rescue Dashboard

**Author:** Brad Mills  
**Date:** March 26, 2025

## Project Overview

This dashboard, developed for Grazioso Salvare, is an interactive tool designed to explore and analyze the Austin Animal Center Outcomes dataset. It empowers users to filter animal data by rescue type, visualize breed distributions, and locate animals geographically. Built with maintainability and usability in mind, the dashboard serves both end-users and developers effectively.

---

## Features

### Interactive Filters
- **Rescue Types:**
  - Water Rescue
  - Mountain or Wilderness Rescue
  - Disaster Rescue or Individual Tracking
  - Reset (restores unfiltered state)
- **Purpose:** Allows users to narrow down animal data based on specific rescue roles.

### Dynamic Data Table
- Displays filtered animal records.
- Features pagination, sorting, and filtering for seamless navigation.
- Supports single-row selection to trigger map updates.

### Geolocation Map
- Visualizes the location of a selected animal using latitude and longitude.
- Centers on the selected animal with a tooltip (breed) and popup (name).

### Breed Distribution Chart
- A dynamic pie chart showing the breed breakdown of filtered animals.
- Updates automatically with filter changes.

---

## Demo

Watch a screencast of the dashboard in action:  
[Video Link](https://1drv.ms/v/s!AjoOhhMeaijyg84ttsY6H1_iNBz9zg?e=6QSw4n)

---

## Technologies Used

### Core Tools
- **Python:** Powers data processing, database interaction, and dashboard logic due to its robust library ecosystem.
- **MongoDB:** Stores animal data in a flexible, document-based structure.
- **Dash Framework:** Drives the interactive web interface with Python-based front-end and back-end components.

### Libraries
- **PyMongo:** Facilitates MongoDB integration with Python.
- **Dash Core Components:** Provides interactive UI elements (e.g., radio buttons, tables).
- **Dash Leaflet:** Enables geolocation mapping.
- **Dash Table & Plotly Express:** Renders dynamic tables and charts.
- **Pandas:** Handles data manipulation and DataFrame operations.

### Why MongoDB?
- **Document-Oriented:** Adapts to varied animal data attributes.
- **Scalability:** Supports large datasets for future growth.
- **Python Integration:** Seamless querying via PyMongo.

### Why Dash?
- **No JavaScript Required:** Simplifies development with Python.
- **Interactivity:** Offers responsive components for filters, charts, and maps.
- **Visualization:** Integrates Plotly for dynamic graphics.

---

## Installation

### Prerequisites
- Python 3.9+
- MongoDB installed and running
- Git

1. Clone the Repository: Clone the project repository to your local machine.
   
   git clone <repository_url>
   
2. Set Up MongoDB:
   - Install MongoDB and populate it with the Austin Animal Center Outcomes dataset.
   - Use the provided `crud.py` file to manage CRUD operations on the dataset.
3. Install Required Python Packages:
   Use `pip` to install the required libraries:
   
   pip install dash jupyter_dash dash_leaflet plotly pandas pymongo
   
4. Run the Jupyter Notebook:
   Open and run the `ProjectTwoDashboard.ipynb` Jupyter Notebook, or run the code as a standalone app by executing:
   
   python ProjectTwoDashboard.py
   
5. Access the Dashboard:
   - If running locally, access the dashboard at `http://127.0.0.1:8050`.
   - Test the filter options, select a record from the data table, and verify the map and chart updates.
Challenges and Solutions
- MongoDB Integration:
  - Challenge: Initial difficulties in setting up efficient data retrieval queries and handling MongoDB’s ObjectID data type.
  - Solution: Developed customized CRUD functions and ensured MongoDB’s `_id` field was removed from data frames to prevent crashes in the data table.

- Interactive Map and Data Table Integration:
  - Challenge: Configuring the map to dynamically display a selected record’s location and information.
  - Solution: Utilized Dash callbacks to make the map center on selected data and display relevant animal details, improving usability.

- User-Friendly Interactivity:
  - Challenge: Providing clear, intuitive filter and selection options.
  - Solution: Implemented radio buttons for filtering rescue types and enabled single-row selection in the data table for an interactive experience.
Resources and References
- https://dash.plotly.com/introduction: Guidance on setting up Dash components and layouts.
- https://docs.mongodb.com/: Information on database setup, CRUD operations, and PyMongo.
- https://plotly.com/python/plotly-express/: Reference for creating responsive charts.


How do you write programs that are maintainable, readable, and adaptable?
Writing maintainable, readable, and adaptable code is essential for building applications that can evolve over time. I follow best practices such as clear naming conventions, modular design, and consistent documentation. In my CRUD Python module from Project One, I applied these principles by creating functions that each perform a specific task related to database operations. By structuring the CRUD module this way, I made it easy to connect dashboard widgets to the database for Project Two. This approach not only simplifies debugging but also makes the code adaptable to new database structures or additional functionality. In the future, I could reuse this CRUD module for other applications that need database interactions, saving development time and ensuring consistency across projects.

How do you approach a problem as a computer scientist?
As a computer scientist, I approach problems by breaking them down into manageable components and designing solutions iteratively. For the dashboard and database requirements that Grazioso Salvare requested, I started by identifying the core database operations (CRUD) and understanding the types of data that the dashboard would need to display. This approach ensured that each part of the project was well-defined and met the client’s requirements. Compared to previous assignments, this project required more planning to ensure all parts of the application worked seamlessly together. In the future, I’ll continue using modular design and data modeling techniques to create databases that effectively meet client requirements, using diagrams or pseudocode to plan complex systems before implementation.

What do computer scientists do, and why does it matter?
Computer scientists design and build systems that solve real-world problems, focusing on efficiency, scalability, and innovation. Projects like this one for Grazioso Salvare demonstrate how computer scientists can create tools to improve a company’s efficiency and decision-making. By building a dashboard with an integrated database, I provided a way for Grazioso Salvare to manage and analyze data seamlessly. This capability allows the company to perform their work more effectively, making data-driven decisions and automating tasks that would otherwise require manual effort. Ultimately, computer scientists empower organizations by creating systems that improve productivity and deliver insights that support better outcomes.
