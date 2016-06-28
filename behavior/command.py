from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass

class Team(object):

    def __init__(self, name):
        self.name = name

    def complete_project(self, requirement):
        msg = "team {} done with requirements {}".format(self.name, requirement)
        print(msg)

class HeroDev(object):
    def do_all_work(self, project_name):
        print("Hi. I'm hero dev. So I done {}".format(project_name))

class YouAsProjectManagerCommand(ICommand):

    def __init__(self, team, requirement):
        self.team = team
        self.requirement = requirement

    def execute(self):
        self.team.complete_project(self.requirement)

class HeroDeveloperCommand(ICommand):

    def __init__(self, hero_developer, project_name):
        self.hero_developer = hero_developer
        self.project_name = project_name

    def execute(self):
        self.hero_developer.do_all_work(self.project_name)

class Customer(object):

    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def sign_contract_with_boss(self):
        for command in self.commands:
            command.execute()

if __name__ == '__main__':
    customer = Customer()

    team = Team("Z")
    requirement = ["req1", "req2", "req3"]
    command_x = YouAsProjectManagerCommand(team, requirement)

    hero_dev = HeroDev()
    command_a = HeroDeveloperCommand(hero_dev, 'projectX')

    customer.add_command(command_x)
    customer.add_command(command_a)

    customer.sign_contract_with_boss()
