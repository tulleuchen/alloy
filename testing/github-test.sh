#!/bin/bash
# install github CLI
# curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg && sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null && sudo apt update && sudo apt install gh -y

export BEANSTALK_APP="someappname"
export BEANSTALK_ENV="devoooops"

# authenticate
# run gh auth login before running this, you'll need username and gh_token generated via https://github.com/settings/tokens

if [[ "${1}" == "manual" ]] && [[ "${2}" == "action" ]]; then
    gh --repo parachutehome/skunk-works workflow run test-composite-action.yaml \
        -f BEANSTALK_APP=${BEANSTALK_APP} \
        -f BEANSTALK_ENV=${BEANSTALK_ENV}

    gh --repo parachutehome/skunk-works run list --workflow=test-composite-action.yaml
else
    printf "Missing arguments"
    printf "Usage: bash ./buildscripts/github-test.sh \"manual\" \"action\"\n"
    exit 1
fi
