folder('Whanos base images') {
    description('The base images for Whanos')
}

freeStyleJob('Whanos base images/Build all base images') {
    description('This job is used to build all the base images')
    steps {
        shell('echo "This is a dummy job"')
    }
}

def whanosLanguages = ['c', 'python', 'java', 'javascript', 'befunge']

whanosLanguages.each { language ->
    freeStyleJob("Whanos base images/whanos-${language}") {
        description("This job is used to build the ${language} base image")
        steps {
            shell('echo "This is a dummy job"')
        }
    }
}
