library(shiny)

# Define server logic required to generate
# and plot a random distribution
shinyServer(function(input, output) {

  output$distPlot <- renderPlot({

    # generate an rnorm distribution and plot it
    dist <- rnorm(input$obs)
    hist(dist, breaks=input$breaks)
  })
})
