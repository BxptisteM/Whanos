folder('Projects') {
    description('Projects linked via the link-project job')
}

freeStyleJob('link-project') {
    description('This job is used to link to another project')
    steps {
        shell('echo "This is a dummy job"')
    }
}
