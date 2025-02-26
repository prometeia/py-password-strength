@Library('promebuilder')_

pipeline {
  agent any
  parameters {
    booleanParam(
      name: 'skip_tests',
      defaultValue: false,
      description: 'Skip unit tests'
    )
    booleanParam(
      name: 'deep_tests',
      defaultValue: false,
      description: 'Do deep testing (regression, sonarqube, install, etc..)'
    )
    booleanParam(
      name: 'python3',
      defaultValue: true,
      description: 'Building also for Pytho3'
    )
    booleanParam(
      name: 'force_upload',
      defaultValue: false,
      description: 'Force Anaconda upload, overwriting the same build.'
    )
    booleanParam(
      name: 'keep_on_fail',
      defaultValue: false,
      description: 'Keep job environment on failed build.'
    )
  }
  options {
    buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '5'))
    disableConcurrentBuilds()
  }
  environment {
    PYVER = "2.7"
    PYVER3 = "3.7"
    CONDAENV = "${env.JOB_NAME}_${env.BUILD_NUMBER}_PY2".replace('%2F','_').replace('/', '_')
    CONDAENV3 = "${env.JOB_NAME}_${env.BUILD_NUMBER}_PY3".replace('%2F','_').replace('/', '_')
  }
  stages {
    stage('Bootstrap') {
      steps {
        writeFile file: 'buildnum', text: "${env.BUILD_NUMBER}"
        writeFile file: 'commit', text: "${env.GIT_COMMIT}"
        writeFile file: 'branch', text: "${env.GIT_BRANCH}"
        stash(name: "source", useDefaultExcludes: true)
      }
    }
    stage("MultiBuild") {
      parallel {
        stage("Build on Linux - Legacy Python") {
          steps {
            doubleArchictecture('linux', 'base', false, PYVER, CONDAENV)
          }
        }
        stage("Build on Windows - Legacy Python") {
          steps {
            script {
              try {
                doubleArchictecture('windows', 'base', false, PYVER, CONDAENV)
              } catch (exc) {
                echo 'Build failed on Windows Legacy Python'
                echo 'Current build result is' + currentBuild.result
                if (!currentBuild.result || currentBuild.result == 'SUCCESS') {
                  currentBuild.result = 'UNSTABLE'
                } else (
                  currentBuild.result = 'FAILED'
                )
              }
            }
          }
        }
        stage("Build on Linux - Python3") {
          when { expression { return params.python3 } }
          steps {
            doubleArchictecture('linux', 'base', false, PYVER3, CONDAENV3)
          }
        }
        stage("Build on Windows - Python3") {
          when { expression { return params.python3 } }
          steps {
            doubleArchictecture('windows', 'base', false, PYVER3, CONDAENV3)
          }
        }
      }
    }
  }
  post {
    always {
      deleteDir()
    }
    success {
      slackSend color: "good", message: "Builded ${env.JOB_NAME} (<${env.BUILD_URL}|Open>)"
    }
    failure {
      slackSend color: "warning", message: "Failed ${env.JOB_NAME} (<${env.BUILD_URL}|Open>)"
    }
  }
}
