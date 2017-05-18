library(shiny)

# Define UI for application that plots random distributions 
shinyUI(pageWithSidebar(

  # Application title
  headerPanel("Interactive Histogram R Shiny App"),

  # Sidebar with a slider input for number of observations
  sidebarPanel(
    sliderInput("obs", "Number of observations:",
                 min=10, max=5000, value=500),
    sliderInput("breaks", "Bins:",
                 min=3, max =50, value=20)
  ),

  # Show a plot of the generated distribution
  mainPanel(
    plotOutput("distPlot")
  )
))
