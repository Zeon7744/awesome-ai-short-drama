name: New Issue
about: General issue (use the bug or feature templates above if applicable)
title: ""
labels: ["triage"]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        Before opening an issue, please search existing ones to avoid duplicates.
  - type: dropdown
    id: type
    attributes:
      label: Issue Type
      options:
        - Bug Report
        - Feature Request
        - Documentation
        - Other
      default: 3
    validations:
      required: true
  - type: input
    id: title
    attributes:
      label: Title
      description: Clear and concise title
      placeholder: Clear and concise title
    validations:
      required: true
  - type: textarea
    id: description
    attributes:
      label: Description
      description: Detailed description
      placeholder: Detailed description...
    validations:
      required: true
  - type: textarea
    id: environment
    attributes:
      label: Environment
      description: OS, Python version, dependencies (if relevant)
      placeholder: |
        - OS:
        - Python:
        - Key packages:
    validations:
      required: false
  - type: textarea
    id: logs
    attributes:
      label: Logs / Screenshots
      description: Error output or relevant images
      render: text
    validations:
      required: false
  - type: checkboxes
    id: checklist
    attributes:
      label: Pre-flight Checklist
      options:
        - label: I have searched existing issues
          required: true
        - label: I have read the README and documentation
          required: true
