library(shiny)
library(findpython)
library(argparse)

found_python <- find_python_cmd(required_modules = c('argparse', 'json | simplejson'))

if(is.null(found_python)) {
    options(python_cmd="/opt/continuum/project/envs/default/bin/python")
} else {
    python_cmd <- found_python
}

print(python_cmd)

parser <- ArgumentParser(description='Process some integers')
parser$add_argument('--anaconda-project-port', metavar='--anaconda-project-port', type="integer", nargs='+',
                    default=8086, help='Port to be used by shiny')
parser$add_argument('--anaconda-project-host', metavar='--anaconda-project-host', type="character", nargs='+',
                    default='0.0.0.0', help='project hostname')
parser$add_argument('--anaconda-project-iframe-hosts', metavar='--anaconda-project-iframe-hosts', type="character", nargs='+',
                    default='https://anaconda.example.com:6990', help='project iframe host')
parser$add_argument('--anaconda-project-use-xheaders', action='store_true', help='use xheaders')
parser$add_argument('--anaconda-project-no-browser', action='store_true')
parser$add_argument('--anaconda-project-address', metavar='--anaconda-project-address', type="character", nargs='+', default='0.0.0.0', help='IP address to listen to.')
parser$add_argument('--anaconda-project-url-prefix', metavar='--anaconda-project-address', type="character", nargs='+', default='', help='Prefix in front of urls')


parsed_args <- parser$parse_args()
port <- as.integer(parsed_args$anaconda_project_port)
print(parsed_args)

runApp(appDir = "hist", port = port, launch.browser = FALSE, quiet = FALSE, host = '0.0.0.0')
