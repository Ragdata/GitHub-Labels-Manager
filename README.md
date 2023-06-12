# About

> This is a fork of the repository at [Paraphory/GitHub-Labels-Manager](https://github.com/Paraphory/GitHub-Labels-Manager) which is slowly but surely being corrupted with stuff that I want it to do.  If you're interested in using this repo, I'd suggest you fork a copy of the original (above).
> 
> -- Rags

Labels Manager is a tool to manage GitHub labels. It can be used to create, update, delete, and sync labels across multiple repositories.

# Use

Run this to generate the default templates:

```shell
py main.py --generate-default-templates
```

which will save the templates to `templates/` folder.

## Apply Template

Run this to apply the template to a repository:

```shell
py main.py --apply-template labels.json --target <owner/repo>
```

If only owner is provided, it will apply the template to all the repositories under the owner.

`labels.json` in this command is the template file. You can also set to other file, but make sure the file is in the `templates/` folder. When this argument is not provided, it will use the default template (`templates/labels.json`).

Pattern: `--apply-template [<template>] --target <owner/repo>`

- `<template>`: The template file name. When ignored use default: `labels.json`
- `<owner/repo>`: The target repository. When `<repo>` ignored, it will apply to all the repositories under the owner.
  - example: Paraphory/GitHub-Labels-Manager    ->  Apply only to `Paraphory/GitHub-Labels-Manager` repo.
  - example: Paraphory/                         ->  Apply to all the repositories under `Paraphory` owner.
  - example: Paraphory                          ->  Apply to all the repositories under `Paraphory` owner.

