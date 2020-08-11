# CDK Python workshop

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (`cdk_workshop_stack`)
which contains an Amazon SQS queue that is subscribed to an Amazon SNS topic.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project. The initialization process also creates
a virtualenv within this project, stored under the .env directory. To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```bash
python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```bash
source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```bash
.env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```bash
pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code. I have added a bash script to wrap the cdk command and add a stage parameter to the stack. So the command line sintax will be like this: `./cdk.sh <command> <stage>`. If stage is not specified, the `dev` stage is used by default.

```bash
./cdk.sh synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```bash
pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

* `./cdk.sh ls`     list all stacks in the app
* `./cdk.sh synth`    emits the synthesized CloudFormation template
* `./cdk.sh deploy`   deploy this stack to your default AWS account/region
* `./cdk.sh diff`    compare deployed stack with current state
* `./cdk.sh docs`    open CDK documentation

Enjoy!

## Participating to this repository

### Development Practices

Developers on this repository must follow the following coding practices:

* No commit to Master branch: the only way to publish code is via feature branches, then PRs to master.
* Signed Commits: Developers must have a PGP key setup and sign their commits using `git commit -s -m "my commit"`
* Pre Commit Hook: this project uses pre-commit to validate that code follows best practices. Developers must run `pre-commit install` at the root of their repository to activate it, after installing for their machine.

### Requirements

This project uses python3 and serverless framework, all of which must be installed locally on the developer machines.

* Python 3: [https://www.python.org/download/releases/3.0/](https://www.python.org/download/releases/3.0/)
* Pre-commit: [pre-commit](https://pre-commit.com/) is an abstraction layer on top of Git Hooks to organize the execution of tests at different moments of the lifecycle of a repository. It must be installed via the official [install procedure](https://pre-commit.com/#install)

### Testing Pre Commit Hooks

Once installed, pre-commmit will operate each time `git commit` is run. It is however possible to run it on all files via

```bash
$ pre-commit run --all-files
Check for added large files..............................................Passed
Check for case conflicts.................................................Passed
Check that executables have shebangs.................(no files to check)Skipped
Check JSON...............................................................Passed
Check for merge conflicts................................................Passed
Trim Trailing Whitespace.................................................Passed
Tabs remover.............................................................Passed
Check markdown files.....................................................Passed
Test shell scripts with shellcheck...................(no files to check)Skipped
Python lintern...........................................................Passed
Python unit tests........................................................Passed
```

to validate that an untracked change will pass before trying to commit it.

## References

* [https://cdkworkshop.com](https://cdkworkshop.com)
