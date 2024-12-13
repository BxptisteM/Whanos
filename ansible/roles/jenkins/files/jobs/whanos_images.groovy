def whanosLanguages = ['c', 'python', 'java', 'javascript', 'befunge']

folder('Whanos base images') {
    description('The base images for Whanos')
}

freeStyleJob('Whanos base images/Build all base images') {
    description('This job triggers the build of all base images.')
    steps {
        shell("""
            echo "Building all base images"
            docker build -t whanos-c - < /var/lib/jenkins/images/c/Dockerfile.base
            docker build -t whanos-python - < /var/lib/jenkins/images/python/Dockerfile.base
            docker build -t whanos-java - < /var/lib/jenkins/images/java/Dockerfile.base
            docker build -t whanos-javascript - < /var/lib/jenkins/images/javascript/Dockerfile.base
            docker build -t whanos-befunge - < /var/lib/jenkins/images/befunge/Dockerfile.base
        """)
    }
}

whanosLanguages.each { language ->
    freeStyleJob("Whanos base images/whanos-${language}") {
        description("This job builds the ${language} base image.")
        steps {
            shell("""
                echo "Building ${language} base image"
                docker build -t whanos-${language} - < /var/lib/jenkins/images/${language}/Dockerfile.base
            """)
        }
    }
}
