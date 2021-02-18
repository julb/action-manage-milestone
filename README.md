![Build](https://github.com/julb/action-manage-milestone/workflows/Build/badge.svg)

# GitHub Action to manage Milestones

The GitHub Action for managing milestones of the GitHub repository.

- Create a new milestone
- Edit an existing milestone
- Closing an existing milestone.
- Deleting a milestone.

## Usage

### Example Workflow file

An example workflow to authenticate with GitHub Platform:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Manage the milestone
        uses: julb/action-manage-milestone@latest
        with:
          title: Some title
          state: open
          description: Some description
          due_on: "2022-01-01"
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Inputs

| Name          | Type   | Default   | Description                                                           |
| ------------- | ------ | --------- | --------------------------------------------------------------------- |
| `title`       | string | `Not set` | Title of the milestone. **Required**                                  |
| `state`       | string | `open`    | State of the milestone. Valid values are `open`, `closed`, `deleted`  |
| `description` | string | `Not set` | Description of the milestone of the milestone.                        |
| `due_on`      | string | `Not set` | ISO8601 representation of the due date of the milestone. `yyyy-MM-dd` |

### Outputs

| Name     | Type   | Description                                                   |
| -------- | ------ | ------------------------------------------------------------- |
| `number` | number | ID of the milestone, or `0` in case the milestone is deleted. |

## Contributing

This project is totally open source and contributors are welcome.

When you submit a PR, please ensure that the python code is well formatted and linted.

```
$ make install.dependencies
$ make format
$ make lint
```
