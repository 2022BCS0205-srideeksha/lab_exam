pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                sh 'pip3 install --break-system-packages -r requirements.txt'
            }
        }

        stage('Train') {
            steps {
                sh 'python3 train.py'
            }
        }

        stage('Identity') {
            steps {
                echo 'Student: Sri Deekshaa | Roll No: 2022BCS0205'
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'model.pkl, metrics.json'
            }
        }
    }
}