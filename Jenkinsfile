pipeline {
  agent {
    docker {
      image 'python_venv_pytest'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
  }

  environment {
    DOCKERHUB_CREDENTIAL_ID = 'credential_dockerhub_fiodo'
    DOCKER_IMAGE_NAME = 'fiodo/my_calcul_test_python'
    DOCKER_IMAGE_TAG  = "calcul-${BUILD_NUMBER}"
  }

  stages {
    stage('Checkout from Git') {
      steps {
        git branch: 'calcul',
            url: 'https://github.com/FionaDoDev/my-python.git'
      }
    }

    stage('Run pytest') {
      steps {
        sh 'pytest -q'
      }
    }

    stage('Build Docker image') {
      steps {
        sh "docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} -t ${DOCKER_IMAGE_NAME}:latest ."
      }
    }

    stage('Push to DockerHub') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIAL_ID}", usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
          sh '''
            echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin
            docker push ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}
            docker push ${DOCKER_IMAGE_NAME}:latest
            docker logout
          '''
        }
      }
    }
  }
}
