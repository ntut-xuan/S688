# S688 - Swagger Validation Tool

S688 is a validation tool written in Python that verifies whether Swagger route descriptions align with the actual application behavior. It achieves this by parsing Swagger JSON files to extract interface descriptions. Users can create scripts to test whether payloads match the Swagger specifications and if sending payloads to the application results in non-400 error responses, ensuring payload consistency.

## Features

- Validate Swagger route descriptions against the application.
- Read and parse Swagger JSON files to extract interface descriptions.
- Scripted testing for payload alignment with Swagger specifications.
- Confirm payload consistency by checking non-400 error responses on payload delivery.


## Roadmap

### Phase 0: Setup and Foundation

- [x] **Repository Initialization**
  - [x] Create a new GitHub repository.
  - [x] Set up the initial project structure.

- [x] **Environment Setup**
  - [x] Install required dependencies specified in `requirements.txt`.

- [x] **.gitignore File**
  - [x] Create a `.gitignore` file to exclude unnecessary files from version control.

- [x] **Basic README.md**
  - [x] Create a comprehensive README.md with project overview, features, and usage instructions.


### Phase 1: Swagger JSON Parsing

- [x] **Swagger JSON Parsing**
  - [x] Implement logic to read and parse Swagger JSON files.
  - [x] Extract API routes and descriptions.
  - [x] Flatten Swagger JSON, expanding `$ref` references to components.

### Phase 2: Transform Payload Descriptions to Actual Payload

- [x] **Payload Transformation Logic**
  - [x] Develop logic to transform JSON payload descriptions to actual payloads.
  - [x] Generate payloads based on Swagger route specifications.

- [x] **Interactive Feedback**
  - [x] Provide clear and informative feedback during payload transformation.
  - [x] Display generated payloads and transformation status.

### Phase 3: Application CLI and Command Processing

- [ ] **Command-line Interface (CLI)**
  - [ ] Develop a user-friendly CLI for the application.
  - [ ] Implement CLI commands for processing Swagger JSON.

- [ ] **Command Processing Logic**
  - [ ] Enhance the application to read and process Swagger JSON files.
  - [ ] Implement logic to flatten Swagger JSON, expanding `$ref` references.

- [ ] **Interactive Feedback**
  - [ ] Provide clear and informative feedback during command execution.
  - [ ] Display results and messages directly within the CLI.

### Phase 4: Assertion Class for Payload Validation

- [ ] **Assertion Class**
  - [ ] Create an `Assertion` class to handle payload validation.
  - [ ] Implement methods to compare payload against Swagger route specifications.

- [ ] **Payload Validation Logic**
  - [ ] Utilize the `Assertion` class to validate payload consistency.
  - [ ] Check if payload adheres to Swagger specifications.

### Phase 5: Documentation and Testing

- [ ] **Documentation**
  - [ ] Document the tool's usage and functions in the README.md.
  - [ ] Provide examples of payload validation and error scenarios.

- [ ] **Unit Testing**
  - [ ] Write unit tests to ensure payload validation functions correctly.
  - [ ] Cover major validation cases and edge scenarios.

### Phase 6: Finalization

- [ ] **Code Review**
  - [ ] Review code for readability, modularity, and adherence to best practices.

- [ ] **Contributing Guidelines**
  - [ ] Include guidelines for external contributions, if desired.

- [ ] **License**
  - [ ] Choose and add an open-source license to the repository.

### Phase 7: Release and Maintenance

- [ ] **Version Tagging**
  - [ ] Tag a version for the initial release.

- [ ] **Continuous Integration**
  - [ ] Set up CI/CD for automated testing and deployment (optional).

- [ ] **Maintenance**
  - [ ] Monitor issues and address them for ongoing maintenance.
