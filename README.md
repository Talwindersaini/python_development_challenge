# python_development_challenge

Resulta Development challenge

Steps to execute this project
  #clone the project
  #Go to the project file
  #Building the Docker Container
      docker build -t python_development_challenge .
  #Verify the Image Build
      docker images
  #Running the Docker Container
      docker run -it python_development_challenge
      
Notes: -
  1. Max date range should be 7 days only
  2. Result generated on the bases of start and end date
  3. Rather than posting on API we are just printing the data.
  4. Fetching data only for NFL
