folder('Projects') {
    description('The folder for all the projects')
}

freeStyleJob('link-project') {
    description('This job is used to link a specified project to the Jenkins infrastructure ' +
                'by creating a new job in the Projects folder.')

    parameters {
        stringParam('PROJECT_NAME', '', 'The name of the project to link to')
    }

    steps {
        dsl {
            text('''
                def projectName = "${PROJECT_NAME}".trim()

                if (projectName) {
                    freeStyleJob("Projects/${projectName}") {
                        description("This job is used to link to the ${projectName} project")
                        steps {
                            shell('echo "This is a dummy job for ${projectName}"')
                        }
                    }
                } else {
                    error("No project name provided.")
                }
            '''.stripIndent())
        }
    }
}
