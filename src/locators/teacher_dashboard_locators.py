from selenium.webdriver.common.by import By

# A Class for Teacher Dashboard locators
class TeacherDashboardLocators(object):
    #Plix locators in Teacher dashboard
    TDB_PLIX_HEADING = (By.XPATH,"//span[contains(text(),'Plix')]")
    TDB_PLIX_ICON = (By.XPATH,"//body/div[@id='dashboard']/div[1]/div[5]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/span[1]/i[1]")
    TDB_PLIX_RIGHT_ARROW = (By.XPATH,"//body/div[@id='dashboard']/div[1]/div[5]/div[1]/div[1]/div[1]/div[8]/div[1]/div[2]/div[3]/span[1]/i[1]")
    TDB_PLIX_CONTENT = (By.XPATH,"//body[1]/div[3]/div[1]/div[5]/div[1]/div[1]/div[1]/div[8]/div[1]/div[2]/div[2]/div[1]")
    TDB_PLIX_LEFT_ARROW = (By.XPATH,"//body/div[@id='dashboard']/div[1]/div[5]/div[1]/div[1]/div[1]/div[8]/div[1]/div[2]/div[1]/span[1]/i[1]")

    #Simulation locators in Teacher dashboard 
    TDB_SIMULATION_HEADING = (By.XPATH,"//span[contains(text(),'Simulations')]")
    TDB_SIMULATION_ICON = (By.XPATH,"//body/div[@id='dashboard']/div[1]/div[5]/div[1]/div[1]/div[1]/div[9]/div[1]/div[1]/div[1]/span[1]/i[1]")
    TDB_SIMULATION_RIGHT_ARROW = (By.XPATH,"//body/div[@id='dashboard']/div[1]/div[5]/div[1]/div[1]/div[1]/div[9]/div[1]/div[2]/div[3]/span[1]/i[1]")
    TDB_SIMULATION_LEFT_ARROW = (By.XPATH,"//body/div[@id='dashboard']/div[1]/div[5]/div[1]/div[1]/div[1]/div[9]/div[1]/div[2]/div[1]/span[1]/i[1]")
    TDB_SIMULATION_CONTENT = (By.XPATH,"//body[1]/div[3]/div[1]/div[5]/div[1]/div[1]/div[1]/div[9]/div[1]/div[2]/div[2]/div[1]")

