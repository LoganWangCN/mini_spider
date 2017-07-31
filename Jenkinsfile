Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('No-op') {
            steps {
                sh 'ls'
            }
        }
    }
    post {
        always {
            echo 'One way or another, I have finished'
            archive 'build/libs/**/*.jar'
            junit 'build/reports/**/*.xml'
            deleteDir() /* clean up our workspace */
        }
        success {
            echo 'I succeeeded!'
            mail to: 'wangxdthu@163.com',
            subject: "Successed Pipeline: ${currentBuild.fullDisplayName}",
            body: "Everything is right with ${env.BUILD_URL}"
        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'I failed :('
            mail to: 'wangxdthu@163.com',
            subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
            body: "Something is wrong with ${env.BUILD_URL}"
        }
        changed {
            echo 'Things were different before...'
        }
    }
}
