library(shiny)

port <- 8086

runApp(appDir = "hist", port = port, launch.browser = TRUE, quiet = FALSE, host = '127.0.0.1')
