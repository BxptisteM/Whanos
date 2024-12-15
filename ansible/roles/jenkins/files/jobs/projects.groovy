folder('Projects') {
    description('The folder for all the projects')
}

freeStyleJob('link-project') {
    description('This job is used to link a specified project to the Jenkins infrastructure ' +
                'by creating a new job in the Projects folder.')

    parameters {
        stringParam('PROJECT_NAME', '', 'The name of the project to link to')
        stringParam('REPO_SSH_URL', '', 'The SSH URL of the repository to link to (e.g. git@github.com:username/repo.git)')
        credentialsParam('DEPLOY_KEY') {
            type('com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey')
            required()
            defaultValue('ssh-key-staging')
            description('SSH Key for deploying build artifacts')
        }
        choiceParam('BRANCH', ['main', 'master', 'develop'], 'Git branch to checkout')
    }

    steps {
        dsl {
            text('''
                def projectName = "${PROJECT_NAME}".trim()
                def repoUrl = "${REPO_SSH_URL}".trim()
                def deployKey = "${DEPLOY_KEY}".trim()
                def branchToBuild = "${BRANCH}".trim()


                freeStyleJob("Projects/${projectName}") {
                    description("This job is used to link to the ${projectName} project")

                    logRotator {
                        daysToKeep(2)
                        numToKeep(4)
                        artifactDaysToKeep(2)
                        artifactNumToKeep(4)
                    }
                    scm {
                        git {
                            remote {
                                url("${repoUrl}")
                                credentials("${deployKey}")
                            }
                            branch("${branchToBuild}")
                        }
                    }
                    triggers {
                        scm('* * * * *')
                    }
                    steps {
                        shell("/var/lib/jenkins/deployment_pipeline/main.py --project ${projectName}")
                    }
                }
            '''.stripIndent())
        }
    }
}
