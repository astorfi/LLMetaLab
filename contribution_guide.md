# 🚀 **LLMetaLab Contribution Guide** 🤝

Thank you for your interest in contributing to **LLMetaLab**! Your contributions are crucial for making this repository a central resource for anyone interested in Large Language Models (LLMs). We welcome all kinds of contributions—whether it's fixing a typo, suggesting new content, adding hands-on tutorials, or building new tools. Let's collaborate to push forward the boundaries of LLM innovation! 💡

## 🌟 **How Can You Contribute?**

### 1. **Report Bugs and Issues** 🐛
Found an issue or bug? Please let us know by [opening an issue](https://github.com/astorfi/LLMetaLab/issues). Be as detailed as possible—screenshots, version details, and error messages are super helpful!

### 2. **Propose Enhancements** 💡
Have a great idea that could improve LLMetaLab? You can suggest new features, improvements, or even just conceptual changes. Submit an [enhancement issue](https://github.com/astorfi/LLMetaLab/issues) to start the conversation.

### 3. **Write Content** 📄
LLMetaLab covers several complex topics, and we want it to be as comprehensive as possible. You can contribute by:

- Expanding existing topics.
- Adding new topics within areas such as Retrieval-Augmented Generation (RAG), alignment, fine-tuning, or emerging research.
- Writing tutorials, step-by-step guides, or practical examples.

If you'd like to contribute a new section, please **open a new issue** first to discuss the outline. This ensures alignment with the overall content strategy.

### 4. **Code Contributions** 🖥️
If you're interested in adding or improving code (tutorials, automation scripts, example projects), please:

1. Fork the repository.
2. Clone your fork locally and create a new branch for your changes.
   ```bash
   git clone https://github.com/YourUsername/LLMetaLab.git
   git checkout -b your-branch-name
   ```
3. Make your changes and commit them. Ensure your code follows best practices and includes adequate documentation.
   ```bash
   git commit -m "Add your clear commit message here"
   ```
4. Push the branch to your fork and **open a pull request**. Make sure you describe what you've done clearly.
   ```bash
   git push origin your-branch-name
   ```

#### ⚙️ **Enforcing Code Quality and Consistency**
- **Docker Requirement**: To ensure the reproducibility and consistency of all code contributions, each Python script or project must include a `Dockerfile`. This guarantees that the code runs end-to-end with the necessary dependencies, isolated from other parts of the repository.
- **Environment Isolation**: We use a `requirements.txt` file for project-wide dependencies. However, contributors are encouraged to add their own `requirements.txt` or `environment.yml` file for isolated scripts, ensuring backward compatibility with existing code.
- **Testing New Dependencies**: If you add new packages, please ensure that they do not break compatibility with existing code. Use Docker to validate your setup, and consider using tools like `tox` for multi-environment testing. Details can be found in the [Setup Guide](setup_guide.md).

### 5. **Review Existing Pull Requests** 🔍
A great way to contribute is to help review [open pull requests](https://github.com/astorfi/LLMetaLab/pulls). Your insights could help improve someone else's contribution and ensure high-quality additions.

## 🛠️ **Setting Up Your Environment**
To contribute effectively, follow these steps to set up your environment:

1. **Clone the Repo**
   ```bash
   git clone https://github.com/astorfi/LLMetaLab.git
   ```
2. **Install Dependencies**
   Make sure you have Python, Docker, and Git installed. You can install project dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
3. **Branching**
   Create a branch before making changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Run Using Docker**
   For new contributions, create a `Dockerfile` to encapsulate dependencies and test your code in a Docker environment to ensure consistency across different systems.

## 🔄 **How to Submit Changes**
1. **Pull Request Guidelines**:
   - Provide a **clear and descriptive title** for your pull request.
   - Include a brief **summary** of what your pull request changes or adds.
   - **Link to the related issue**, if applicable.
   - Describe the **motivation and context** for your changes.

2. **Check the Checklist** before submitting a pull request:
   - Have you provided meaningful commit messages?
   - Have you checked for typos, grammar issues, and code formatting?
   - Have you linked any related issues?
   - **Docker and Compatibility Check**: Verify that your Docker setup runs successfully, and confirm compatibility with existing code.

## ✅ **Contribution Guidelines**
- **Follow the Folder Structure**: LLMetaLab follows a structured folder layout (see the README for full details). Ensure any new content is placed in the correct folder.
- **Documentation and Comments**: Document your changes wherever necessary. Your contributions should be understandable to other readers and contributors.
- **Code Style**: Follow PEP8 guidelines for Python. Maintain clean, readable, and reusable code. Use comments to explain non-obvious code logic.
- **Testing New Code**: Every code addition must be tested in an isolated Docker container to verify functionality.
- **Respect Diversity**: We believe in maintaining a healthy and inclusive community. Be respectful when providing feedback and always assume good intentions.

## 🙌 **First-Time Contributors Welcome!**
We are always excited to work with new contributors! You can start by looking at issues labeled [**good first issue**](https://github.com/astorfi/LLMetaLab/labels/good%20first%20issue). These are beginner-friendly tasks that are perfect for anyone just getting started.

Here is an example of a good first issue that you could contribute to:

- [**Improve RAG documentation - Fix Typo in key_components.md**](https://github.com/astorfi/LLMetaLab/issues/1)

## 📢 **Join the Conversation**
- **Feedback**: We value your insights. Feel free to provide feedback by opening an issue or commenting on ongoing discussions.

## 💌 **Code of Conduct**
We follow a [**Code of Conduct**](CODE_OF_CONDUCT.md) to ensure a welcoming environment for everyone. Please make sure you have read and understood the guidelines.

---

**Thank you again for considering contributing to LLMetaLab**. Let's collaborate, innovate, and make a positive impact in the world of Large Language Models together! 🌟

