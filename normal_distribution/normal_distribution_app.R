library(shiny)
library(argparse)

parser <- ArgumentParser(description='Process some integers')
parser$add_argument('--anaconda-project-port', metavar='--anaconda-project-port', type="integer", nargs='+',
                    default=8086, help='Port to be used by shiny')
parser$add_argument('--anaconda-project-host', metavar='--anaconda-project-host', type="character", nargs='+',
                    default='127.0.0.1', help='project hostname')
parser$add_argument('--anaconda-project-iframe-hosts', metavar='--anaconda-project-iframe-hosts', type="character", nargs='+',
                    default='https://anaconda.example.com:6990', help='project iframe host')
parser$add_argument('--anaconda-project-use-xheaders', action='store_true', help='use xheaders')

parsed_args <- parser$parse_args()
port <- as.integer(parsed_args$anaconda_project_port)
print(parsed_args)

runApp(appDir = "hello", port = port, launch.browser = TRUE, quiet = FALSE, host = '127.0.0.1')
