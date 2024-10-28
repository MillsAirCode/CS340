CS340 Grazioso Salvare Animal Rescue ReadMe

Brad Mills

Project Description

This dashboard project, developed for Grazioso Salvare, allows users to filter, view, and interact with the Austin Animal Center Outcomes dataset. The dashboard includes several interactive features, such as filtering options for different rescue types, a dynamic data table, and visualizations that display the location and breed distribution of animals suited for various rescue operations.

The dashboard was designed with maintainability and ease of use in mind, making it accessible for both users and future developers.
Required Functionality
The project includes the following key functionalities:
- Interactive Filter Options: Users can filter the data based on specific rescue types:
  - Water Rescue
  - Mountain or Wilderness Rescue
  - Disaster Rescue or Individual Tracking
  - Reset (returns all widgets to their unfiltered state)
- Dynamic Data Table: Displays animal data based on filter options with pagination, sorting, and filtering features for easy navigation.
- Geolocation Map: Displays the location of a selected animal, centering the map on that animal's position and providing additional information.
- Breed Distribution Chart: A pie chart that dynamically displays the breed distribution of animals in the filtered data.
Screenshots / Screencast

Video link to screencast below:
https://1drv.ms/v/s!AjoOhhMeaijyg84ttsY6H1_iNBz9zg?e=6QSw4n
Tools and Rationale
The following tools and technologies were used to achieve the required functionality:

- Python: Chosen for its rich ecosystem of data processing, web development, and database libraries, which allowed for efficient dashboard creation.
- MongoDB: Used as the database model for storing and retrieving animal data. MongoDB was selected due to its:
  - Document-based structure: Allows for flexible data storage, which is suitable for varying animal data attributes.
  - Ease of integration with Python (via PyMongo): Facilitates efficient data retrieval directly from Python applications.
  - Scalability: Supports large datasets, making it ideal for future expansion.
- Dash Framework: Provides the view (front-end) and controller (back-end) components for the web application.
  - Dash Core Components: Interactive components like radio buttons, dropdowns, and data tables.
  - Dash Leaflet: Enables map integration for geolocation data visualization.
  - Dash Table and Plotly Express: Used for creating a dynamic table and charts that respond to filtering inputs.
Why MongoDB?
MongoDB was selected as the data model for its capabilities to store and retrieve semi-structured data. Its document-oriented design and JSON-like data storage format allow us to efficiently interface with animal records, and its ease of integration with Python libraries (such as PyMongo) provides streamlined interaction with the dashboard components. Additionally, MongoDB’s scalability supports the storage and quick retrieval of potentially large animal datasets, a necessary feature for Grazioso Salvare’s requirements.
Why Dash?
The Dash framework enables rapid development of interactive web applications without the need for JavaScript. Its component-based design integrates well with Python and provides extensive support for data visualization and interactivity, which are essential for creating dynamic elements such as filter options, charts, and maps.
Installation and Reproduction Steps
To reproduce this project:

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
