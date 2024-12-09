def whanosLanguages = ['c', 'python', 'java', 'javascript', 'befunge']

folder('Whanos base images') {
    description('The base images for Whanos')
}

freeStyleJob('Whanos base images/Build all base images') {
    description('This job triggers the build of all base images.')
    steps {
        shell("""
            echo "Building all base images"
            docker build -t whanos-c ./whanos-c
            docker build -t whanos-python ./whanos-python
            docker build -t whanos-java ./whanos-java
            docker build -t whanos-javascript ./whanos-javascript
            docker build -t whanos-befunge ./whanos-befunge
        """)
    }
}

whanosLanguages.each { language ->
    freeStyleJob("Whanos base images/whanos-${language}") {
        description("This job builds the ${language} base image.")
        steps {
            shell("""
                echo "Building ${language} base image"
                docker build -t whanos-${language}: ./whanos-${language}
            """)
        }
    }
}
