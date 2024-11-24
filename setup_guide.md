# 📋 **Setup Guide for LLMetaLab Repository**

Welcome to **LLMetaLab**! This guide will help you set up the environment needed for running, developing, and contributing to the LLMetaLab repository. We prioritize consistency and reproducibility, and have a few mandatory requirements to ensure that all contributions are easy to integrate, execute, and maintain.

## 🔧 **Environment Setup**

### **1. Clone the Repository**
First, clone the LLMetaLab repository to your local machine.
```sh
$ git clone https://github.com/YourRepo/LLMetaLab.git
$ cd LLMetaLab
```

### **2. Docker Requirements**
To ensure consistent environments across different machines, each module must run within a **Docker container**. Docker guarantees that dependencies and configurations are reproducible for everyone using the code.

- **Install Docker**:
  - [Docker Installation Guide](https://docs.docker.com/get-docker/)
- Verify Docker installation by running:
  ```sh
  $ docker --version
  ```
  You should see the Docker version output if it is installed correctly.

### **3. Python Requirements**
- Every Python module has its own **`requirements.txt`** file or **`environment.yaml`** specifying the dependencies required for that module.
- Install [Python](https://www.python.org/downloads/) (preferably version 3.9 or higher).
- To ensure you have `pip` installed, run:
  ```sh
  $ pip --version
  ```
  If not installed, refer to the [pip installation guide](https://pip.pypa.io/en/stable/installation/).

### **4. Setting Up Local Environment (Optional)**
If you prefer working in your local environment without Docker, you can follow these steps to set up the dependencies manually:

1. **Virtual Environment Setup**:
   - Create a virtual environment to isolate dependencies:
     ```sh
     $ python -m venv llmetalab_env
     $ source llmetalab_env/bin/activate  # Linux/macOS
     $ .\llmetalab_env\Scripts\activate  # Windows
     ```

2. **Install Dependencies**:
   - Navigate to the specific project/module folder and install its requirements:
     ```sh
     $ pip install -r requirements.txt
     ```

### **5. Running with Docker**
Each Python script or module in LLMetaLab must have its own **Dockerfile**. The Dockerfile ensures that the code runs in a clean, reproducible environment, with all dependencies included.

- **Build and Run Docker Container**:
  1. Navigate to the folder containing your Dockerfile.
  2. Build the Docker image:
     ```sh
     $ docker build -t your-module-name .
     ```
  3. Run the Docker container:
     ```sh
     $ docker run your-module-name
     ```
- **Dockerfile Requirements**:
  - The Dockerfile should use an official Python base image (e.g., `python:3.9`).
  - Copy necessary files into the Docker container.
  - Install dependencies using `requirements.txt`.
  - Set the default command to run the script.

### **6. Testing Your Code**
- **Local Testing**:
  - Make sure your code runs successfully in your Docker container or local environment before pushing it to the repository.
- **CI/CD Integration**:
  - When you push your code, **GitHub Actions** will automatically test it.
  - Ensure that your code passes all the checks to be merged successfully.

## 🚀 **Contributing to LLMetaLab**
If you want to contribute to LLMetaLab, please ensure that you follow the repository guidelines to maintain compatibility and high standards:

### **1. Every Contribution Must Have**
- A **Dockerfile**: Ensures reproducibility for other contributors.
- A **`requirements.txt`** file or **`environment.yaml`**: Specifies the dependencies required for your script/module.

### **2. Version Compatibility**
- If your script/module requires new versions of existing libraries, make sure the updated versions do not break compatibility with existing code.
- Use tools like `pipenv` or `conda` to create isolated environments if necessary.

### **3. CI/CD Checks**
- All contributions will undergo **GitHub Actions** CI/CD checks.
- The CI pipeline will:
  - Verify the presence of a **Dockerfile** and **requirements.txt**.
  - Build the Docker image and run your code to confirm that everything works as expected.

## 📚 **Useful Commands**
- **Building a Docker Image**:
  ```sh
  docker build -t <image-name> .
  ```
- **Running a Docker Container**:
  ```sh
  docker run <image-name>
  ```
- **Listing Docker Containers**:
  ```sh
  docker ps -a
  ```
- **Stopping a Docker Container**:
  ```sh
  docker stop <container-id>
  ```
- **Removing Docker Containers and Images**:
  ```sh
  docker rm <container-id>
  docker rmi <image-id>
  ```

## 🤝 **Getting Help**
If you have any questions or run into any issues during setup:
- Check the **Issues** page on GitHub to see if anyone else has had the same problem.
- Create a new issue if your problem is unique.
- Reach out to the community through GitHub Discussions.

We’re excited to have you contribute to LLMetaLab and help advance the field of large language models! Happy coding! 🎉

