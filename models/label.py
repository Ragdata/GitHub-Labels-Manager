import os
import json


class label:
    name = "Label Name"
    description = "Label Description"
    color = "#ffffff"

    def default():
        return label("Label Name", "Label Description", "#ffffff")

    def __init__(self, name, description, color):
        self.name = name
        self.description = description
        self.color = color

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def fromJson(self):
        tmp = json.loads(
            self,
            object_hook=lambda d: label(d['name'], d['description'], d['color']),
        )
        return label(tmp.name, tmp.description, tmp.color)


class action:
    option = str()  # create, edit, delete
    name = str()
    label = label.default()

    def __init__(self, option, name, label):
        self.option = option
        self.name = name
        self.label = label

    def execute(self, owner, repo):
        cmd = f'gh label {self.option}'
        repo = f'-R {owner}/{repo}'

        append = str()

        if self.option == 'create':
            label = f'\"{self.name}\" --description \"{self.label.description}\" --color {self.label.color.replace("#", "")}'
            append = f'-f {label}'
        elif self.option == 'edit':
            nameChanged = self.name != self.label.name
            append = f'\"{self.name}\" --description \"{self.label.description}\" --color {self.label.color.replace("#", "")}'
            if nameChanged:
                append += f' --name \"{self.label.name}\"'
        elif self.option == 'delete':
            append = f'\"{self.name}\" --yes'

        fullCommand = f'{cmd} {repo} {append}'

        print(os.system(fullCommand))


def getLabels(owner, repo):
    # example cmd: gh label list -R Crequency/KitX --json name,description,color --jq ".[]"

    cmd = 'gh label list'
    repo = f'-R {owner}/{repo}'
    condition = '--json name,description,color'
    jq = '--jq \".[]\"'

    fullCommand = f'{cmd} {repo} {condition} {jq}'

    process = os.popen(fullCommand)
    output = process.read().splitlines()
    process.close()

    return [label.fromJson(x) for x in output if x != '']


if __name__ == "__main__":
    print([x.toJson() for x in getLabels('Crequency', 'KitX')])
