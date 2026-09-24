name: Feature Request
about: Suggest an idea for this project
title: "[FEATURE] "
labels: ["enhancement"]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        Have an idea? Share it here!
  - type: input
    id: title
    attributes:
      label: Title
      description: Short descriptive title.
      placeholder: e.g. Add ETH prediction support
    validations:
      required: true
  - type: textarea
    id: problem
    attributes:
      label: Problem
      description: What problem does this solve?
    validations:
      required: false
  - type: textarea
    id: solution
    attributes:
      label: Proposed Solution
      description: How should this be implemented?
    validations:
      required: true
  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives
      description: Any alternatives you considered.
    validations:
      required: false
  - type: textarea
    id: context
    attributes:
      label: Additional Context
      description: Screenshots, references, etc.
    validations:
      required: false
