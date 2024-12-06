folder('Projects') {
    description('Projects stored in the current instance')
}

freeStyleJob('link-project') {
    description('This job is used to link to another project')
    steps {
        shell('echo "This is a dummy job"')
    }
}
