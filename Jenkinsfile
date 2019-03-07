pipeline {
    agent none
    stages {
        stage('clone') {
            agent any
            steps {
                checkout(
                    [$class: 'GitSCM', branches: [[name: '*/v1_iris_jenkins']], 
                    doGenerateSubmoduleConfigurations: false, 
                    extensions: [], 
                    submoduleCfg: [], 
                    userRemoteConfigs: [[name: 'twister', url: 'https://github.com/iris-edu-int/twister-imct-editor.git']]]
                )
                stash includes: '**/*', name: 'app_src'
            }
        }
        stage('build') {
            environment {
                frontEnd = ""
                backEnd = ""
            }
            steps {
                node('docker1') {
                    script {
                        unstash 'app_src'
                        sh "sudo docker build -t frontend-test -f Dockerfile.tomcat ./frontend"
                        sh "sudo docker build -t backend-test -f Dockerfile.tomcat ./backend"
                    }
                }
            }
        }
    }
}
